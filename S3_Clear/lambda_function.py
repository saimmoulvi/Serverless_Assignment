import boto3
from datetime import datetime, timezone, timedelta

# Initialize the S3 client
s3 = boto3.client('s3')

# Define the bucket name
BUCKET_NAME = 'your-bucket-name'

def lambda_handler(event, context):
    # Get the current time and the time 30 days ago
    current_time = datetime.now(timezone.utc)
    cutoff_time = current_time - timedelta(days=30)
    
    # List all objects in the bucket
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    
    if 'Contents' in response:
        for obj in response['Contents']:
            # Get the object's last modified date
            last_modified = obj['LastModified']
            
            # If the object is older than 30 days, delete it
            if last_modified < cutoff_time:
                print(f"Deleting {obj['Key']} (Last modified: {last_modified})")
                s3.delete_object(Bucket=BUCKET_NAME, Key=obj['Key'])
    else:
        print("No objects found in the bucket.")

    return {
        'statusCode': 200,
        'body': f"Cleanup completed. Checked {len(response.get('Contents', []))} objects."
    }
