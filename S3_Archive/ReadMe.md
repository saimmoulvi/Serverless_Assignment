## 1. S3 Setup

- Navigate to the S3 dashboard and create a new bucket.   
- Upload a mix of old and new files to this bucket.   
## 2. Lambda IAM Role

- In the IAM dashboard, create a new role for Lambda.   
- Attach the `AmazonS3FullAccess` policy to this role. This policy grants the necessary permissions for the Lambda function to access and modify the S3 bucket.   
## 3. Lambda Function   

- Navigate to the Lambda dashboard and create a new function.   
- Choose Python 3.x as the runtime.   
- Assign the IAM role created in the previous step.
## 4. Testing

- Manually trigger the Lambda function or set it to run periodically using a CloudWatch event trigger.   
- Confirm that older files in the S3 bucket are moved to the Glacier storage class.   
