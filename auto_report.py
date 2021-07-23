import pandas as pd
import json
import io
import boto3
import xlsxwriter

def lambda_handler(event, context):
    data = get_data()
    dataframe = clean_data(data)
    upload_to_s3(dataframe)

    return {
        'status code': 200,
        'body': json.dumps('lambda executed succesfully')
    }

def get_data():
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    table = dynamodb.Table('Movies')
    response = table.query(
        KeyConditionExpression=Key('year').eq(year)
    )
    return response

def clean_data(response):
    df = pd.read_csv(io.BytesIO(response['Body'].read()), encoding='utf8')
    df = df.dropna()
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    df = df.reset_index(drop=True)

    return df

def upload_to_s3(df):
    bucket = 'reports-bucket'
    filepath = 'reports/daily-report.xls'
    s3 = boto3.resource('s3')

    with io.BytesIO() as output:
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, 'report')
        data = output.getvalue()
    
    s3.Bucket(bucket).put_object(Key=filepath, Body=data)





