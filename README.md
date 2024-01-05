a## Cloud Resume Challenge built on AWS Services. 

This is my attempt to build my online resume in AWS as part of the Cloud Resume Challenge defined by  <a href="https://cloudresumechallenge.dev/docs/the-challenge/aws/" target="_blank">  Forrest Brazeal</a> <a href="https://www.seshadri-resume.net/index.html> My Resume </a>

## Project Highlights

* Build HTML/CSS resume and host as S3 static website
* Setup github repo and github actions to define CI/CD pipeline
* Author a lambda function to calculate the page visits and store in dynamodb
* Registered domain in route53 and configured cloudfront 
* API gateway to trigger the lambda function 
* Python lambda function to increment page visit counter and store in dynamodb

## Architecture

![Architecture](img/CloudArchitecture.png)

## AWS Services 

1. S3 Static Website
2. Route53
3. CloudFront
4. DynamoDB
5. Lambda
6. API Gateway
7. CloudWatch

