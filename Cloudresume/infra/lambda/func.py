import json
import boto3

# Specify the AWS region where your DynamoDB table is located
region = 'us-east-1'

def lambda_handler(event, context):
    # Create the DynamoDB resource with the specified region
    dynamodb = boto3.resource('dynamodb', region_name=region)
    table = dynamodb.Table('cloudresume')

    response = table.get_item(Key={'id': '1'})
    if 'Item' in response:
        views = response['Item'].get('views', 0)
        views += 1
        print(f"The website has been viewed {views} times.")
        response = table.put_item(Item={'id': '1', 'views': views})
    else:
        views = 1
        print(f"The website has been viewed {views} time.")

    return views
