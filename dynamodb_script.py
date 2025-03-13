import boto3

# Initialize DynamoDB Client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Students')

# Insert Data
table.put_item(Item={
    'StudentID': 'S002',
    'Name': 'Jane Smith',
    'Age': 22,
    'Department': 'Mathematics'
})

# Retrieve Data
response = table.get_item(Key={'StudentID': 'S002'})
print(response['Item'])
