from dagster import AssetSelection, define_asset_job, load_assets_from_package_module, repository, with_resources, asset
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
    profiles_dir=DBT_PROFILES_DIR
)


@asset 
def my_asset():
    pass 


dbt_asset_job = define_asset_job(
    name="dbt_assets_local2_target", 
    selection=AssetSelection.groups("mydbt")
)

@repository
def dagsterproj():
    return [
        with_resources(
            dbt_assets + [my_asset], 
            resource_defs= {
                "dbt": dbt_cli_resource.configured({"project-dir": DBT_PROJECT_DIR, "profiles-dir": DBT_PROFILES_DIR})
            }
        ), 
        dbt_asset_job
    ]
