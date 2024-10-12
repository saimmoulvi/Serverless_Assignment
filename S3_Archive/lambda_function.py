import boto3
import datetime

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Set the S3 bucket name and the Glacier storage class
    bucket_name = 'your-bucket-name'
    glacier_storage_class = 'GLACIER'

    # List objects in the S3 bucket
    objects = s3.list_objects(Bucket=bucket_name)

    # Identify files older than 6 months
    for obj in objects['Contents']:
        obj_date = datetime.datetime.fromtimestamp(obj['LastModified'].timestamp())
        if (datetime.datetime.now() - obj_date).days > 180:  # 180 days = 6 months
            # Change the storage class of identified files to Glacier
            s3.copy_object(CopySource={'Bucket': bucket_name, 'Key': obj['Key']},
                            Bucket=bucket_name,
                            Key=obj['Key'],
                            StorageClass=glacier_storage_class)

            # Log the archived files
            print(f"Archived file: {obj['Key']}")

    return {
        'statusCode': 200,
        'statusMessage': 'Files archived successfully'
    }
