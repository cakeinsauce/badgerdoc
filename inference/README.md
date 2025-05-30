# Fastapi microservice for integrating inference pipelines with other Badgerdoc services

## Description

This microservices makes running inference pipelines easier. It works as facade service that enables users to run inference on documents without communicating with other BadgerDoc services directly.

## API endpoints

- **/models** (GET): Get list of available ML models with their parameters
- **/upload_files** (POST): Upload form files data to BadgerDoc
- **/start** (POST): Start inference job with submitted parameters
- **/result/{job_id}** (GET): Get result of inferece job

More information about endpoints and their parameters can be found on autogenerated **/inference/docs#/** page.

## How to run

1. Make sure you have python>=3.12, pip and poetry>=2.0 installed
1. From the root of the service ('inference' folder) install dependencies with poetry in editable mode

    ```bash
    poetry install --no-root --only main
    ```

1. Project needs dependencies from artifactory base image specified in Dockerfile.  

    To run app locally you should also install 'tenant_dependency' from **lib/tenants** folder

1. Run uvicorn application

    ```bash
    uvicorn inference.main:app --reload
    ```