from dagster import load_assets_from_package_module, repository, with_resources, asset
from dagster_dbt import load_assets_from_dbt_project, dbt_cli_resource
import os

if os.getenv("DAGSTER_DEPLOYMENT", "prod") == "local":
    DBT_PROFILES_DIR = "../dbtproj"
    DBT_PROJECT_DIR = "../dbtproj"
else:
    DBT_PROFILES_DIR = "./dbtproj"
    DBT_PROJECT_DIR = "./dbtproj"

dbt_assets = load_assets_from_dbt_project(
    project_dir=DBT_PROJECT_DIR,
    profiles_dir=DBT_PROFILES_DIR, 
)

@asset 
def my_asset():
    pass 

@repository
def dagsterproj():
    return [
        with_resources(
            dbt_assets + [my_asset], 
            resource_defs= {
                "dbt": dbt_cli_resource.configured(
                    {"project_dir": DBT_PROJECT_DIR, "profiles_dir": DBT_PROFILES_DIR}
                )
            }
        )
    ]
