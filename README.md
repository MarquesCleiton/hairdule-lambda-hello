# Hairdule • Lambda Hello World (SAM/CloudFormation) — sem API Gateway

## Build
sam build --template-file infra/template.yaml

## Deploy Homol
sam deploy --config-env homol

## Deploy Prod
sam deploy --config-env prod

## Destroy
sam delete --stack-name hairdule
