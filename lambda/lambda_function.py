import json
import boto3
import base64
from decimal import Decimal
from datetime import datetime
from boto3.dynamodb import conditions
from boto3.dynamodb.conditions import Key
import decimal


def lambda_handler(event, context):
    # TODO implement
    dbClient=boto3.resource("dynamodb")
    table_name="ResumeVisitCounter"
    # Replace 'your_aws_region' with the actual AWS region where your DynamoDB table is located
    aws_region = 'us-east-1'
    
    # Create a DynamoDB resource
    dynamodb = boto3.resource('dynamodb', region_name=aws_region)
    
    # Specify the DynamoDB table
    table = dynamodb.Table(table_name)
    composite_key = {
    'id': '0'
    }
    response = table.get_item(Key=composite_key)
    if 'Item' in response:
        visits=response['Item']['visitscounter']
        visits=visits + 1
        # item = response['Item']
        
        # print("Item  found.")
        # print("Item:", item)
    else:
        print("Item not found.")
    

    # Insert data into DynamoDB
    try:
            response = table.put_item(Item={
            'id':'0',
            'visitscounter': visits
        })

    except Exception as e:
        print("Error:", e)
        return {
            'statusCode': 500,
            'body': json.dumps('Error inserting data into DynamoDB')
        }
    # return visits
    return {
         'statusCode': 200,
         'headers': {
             'Access-Control-Allow-Headers': '*',
             'Access-Control-Allow-Origin': '*',
             'Access-Control-Allow-Methods': '*'
         },
         'body': json.dumps({'visit_count': str(visits)})
    }