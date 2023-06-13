import boto3

def smoke_test():
    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('cloudresume')
        event = {}
        context = {}
        result = lambda_handler(event, context)
        print("Smoke test passed.")
    except Exception as e:
        print(f"Smoke test failed. Error: {str(e)}")

if __name__ == '__main__':
    smoke_test()
