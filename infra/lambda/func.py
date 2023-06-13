import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('cloudresume')

def lambda_handler(event, context):
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