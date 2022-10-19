# dagsterproj

This is a dagster project that is designed to work with a dbt project in another Git repository.

Commits to both this repository and the dbt project repository will trigger a deployment to Dagster Cloud. PRs on this repository or the dbt project repository will create a branch deployment in Dagster Cloud.

The GitHub actions have been adapted to clone the repo `https://github.com/slopp/dbtproj` and then deploy the result to Dagster Cloud. To use these actions in your own project, be sure to modify the GitHub actions "Clone DBT" step to refer to the proper repository. 

The `repository.py` file has an example of how to tell Dagster where to find the dbt project. Update this code based on the local location of your dbt project relative to the dagster project. The GHA clones the dbt project into a sub-directory of the dagster repository.

