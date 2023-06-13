import json
import boto3
from unittest import mock
from functions import lambda_handler

# Mock the DynamoDB resource and table
@mock.patch('my_module.boto3.resource')
def test_unit_lambda_handler(mock_resource):
    # Mock the DynamoDB response
    mock_table = mock_resource.return_value.Table.return_value
    mock_table.get_item.return_value = {'Item': {'id': '1', 'views': 5}}

    # Invoke the lambda_handler function
    result = lambda_handler(None, None)

    # Assert the expected views count
    assert result == 6

    # Assert DynamoDB resource and table methods were called
    mock_resource.assert_called_once_with('dynamodb')
    mock_resource.return_value.Table.assert_called_once_with('cloudresume')
    mock_table.get_item.assert_called_once_with(Key={'id': '1'})
    mock_table.put_item.assert_called_once_with(Item={'id': '1', 'views': 6})


def test_end_to_end_lambda_handler():
    # Set up the test environment
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.create_table(
        TableName='test_table',
        KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
        AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
        ProvisionedThroughput={'ReadCapacityUnits': 1, 'WriteCapacityUnits': 1}
    )
    table.put_item(Item={'id': '1', 'views': 5})

    # Invoke the lambda_handler function
    result = lambda_handler(None, None)

    # Verify the result
    assert result == 6

    # Retrieve the updated item from the DynamoDB table
    response = table.get_item(Key={'id': '1'})
    assert response['Item']['views'] == 6

    # Clean up the test environment
    table.delete()
