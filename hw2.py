import boto3
from datetime import datetime, timedelta
import time

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UserLogins')

# ------------------ Insert Sample Data ------------------

# Helper function to convert datetime to timestamp
def datetime_to_timestamp(dt):
    return int(time.mktime(dt.timetuple()))

# Current time
now = datetime.now()

# Sample users (some last week, some older)
users = [
    {"UserID": "user1", "Name": "Alice", "Email": "alice@outlook.com", "LastLogin": (now - timedelta(days=2)).isoformat()},
    {"UserID": "user2", "Name": "Bob", "Email": "bob@gmail.com", "LastLogin": (now - timedelta(days=10)).isoformat()},
    {"UserID": "user3", "Name": "Charlie", "Email": "charlie@hotmail.com", "LastLogin": (now - timedelta(days=5)).isoformat()},
    {"UserID": "user4", "Name": "Diana", "Email": "diana@yahoo.com", "LastLogin": (now - timedelta(days=15)).isoformat()},
]

# Insert each user into DynamoDB
for user in users:
    timestamp = datetime_to_timestamp(datetime.fromisoformat(user["LastLogin"]))
    table.put_item(
        Item={
            'UserID': user['UserID'],
            'Timestamp': timestamp,
            'Name': user['Name'],
            'Email': user['Email'],
            'LastLogin': user['LastLogin']
        }
    )
print("***Sample data inserted.***")

# ------------------ Query Last 7 Days ------------------

# Calculate timestamp for 7 days ago
seven_days_ago = datetime_to_timestamp(now - timedelta(days=7))

# Scan the table and filter
response = table.scan()
items = response['Items']

print("\n***Users who logged in last 7 days:***\n")
for item in items:
    if item['Timestamp'] >= seven_days_ago:
        print(f"UserID: {item['UserID']}")
        print(f"Name: {item['Name']}")
        print(f"Email: {item['Email']}")
        print(f"LastLogin: {item['LastLogin']}")
        print(f"Timestamp: {item['Timestamp']}") 
        print("-" * 30)
