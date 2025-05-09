import boto3
import json

kinesis = boto3.client("kinesis")

# Sample data to send
data = {
    "user": "abc",
    "event": "login",
    "timestamp": "2025-05-08T14:00:00Z"
}

# Send to Kinesis
response = kinesis.put_record(
    StreamName="stream-demo",
    Data=json.dumps(data),
    PartitionKey="1"
)

print("Record sent:", response)
