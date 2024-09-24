import boto3

# Initialize S3 client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    # List all S3 buckets
    response = s3.list_buckets()
    buckets = response['Buckets']

    unencrypted_buckets = []
    
    # Check each bucket for encryption
    for bucket in buckets:
        bucket_name = bucket['Name']
        try:
            # Try to retrieve the bucket encryption configuration
            enc = s3.get_bucket_encryption(Bucket=bucket_name)
            print(f"Bucket '{bucket_name}' has encryption enabled.")
        except s3.exceptions.ClientError as e:
            # If error is raised, bucket likely has no encryption
            error_code = e.response['Error']['Code']
            if error_code == 'ServerSideEncryptionConfigurationNotFoundError':
                print(f"Bucket '{bucket_name}' does not have encryption.")
                unencrypted_buckets.append(bucket_name)
            else:
                print(f"Error checking encryption for bucket '{bucket_name}': {e}")
    
    # Log the unencrypted buckets
    if unencrypted_buckets:
        print("Unencrypted buckets found:", unencrypted_buckets)
    else:
        print("All buckets have server-side encryption enabled.")
    
    return {
        'statusCode': 200,
        'body': unencrypted_buckets
    }
