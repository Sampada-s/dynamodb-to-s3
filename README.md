# dynamodb-to-s3
Lambda function to get dynamo db data and upload it as excel on to s3

#### Features
1) Boto3 to interact with s3 and dynamodb
2) Pandas to read, clean and convert data

#### Deployment
Using aws cli
1)Download this package as zip
2) install aws cli and run -

aws lambda create-function --function-name dynamodb-to-s3
--zip-file fileb://archive.zip --handler auto_report.lambda_handler --runtime python3.6
--role arn:aws:iam::12345678:role/lambda-ex
