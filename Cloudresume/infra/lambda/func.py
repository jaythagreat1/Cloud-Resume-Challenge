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

def smoke_test():
    try:
        event = {}
        context = {}
        result = lambda_handler(event, context)
        print("Smoke test passed.")
    except Exception as e:
        print(f"Smoke test failed. Error: {str(e)}")

if __name__ == '__main__':
    smoke_test()
