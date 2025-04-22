from datetime import datetime, timedelta
import boto3

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

# Get timestamp for 7 days ago
seven_days_ago = datetime.now() - timedelta(days=7)
timestamp_seven_days_ago = int(seven_days_ago.timestamp())

# Set the UserID you want to query (required for KeyConditionExpression)
user_id = "user123"  # Replace with an actual UserID from your table

# Query the table using UserID and Timestamp
response = table.query(
    KeyConditionExpression="UserID = :uid AND #ts >= :val",
    ExpressionAttributeNames={
        "#ts": "Timestamp",
        "#nm": "Name"
    },
    ExpressionAttributeValues={
        ":uid": user_id,
        ":val": timestamp_seven_days_ago
    },
    ProjectionExpression="UserID, #nm, LastLogin"
)

# Print results
for item in response['Items']:
    print(item)
