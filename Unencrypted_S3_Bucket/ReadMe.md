## 1. S3 Setup   
- Create S3 Buckets:    
Navigate to the AWS S3 dashboard and create several buckets. Make sure that some of these buckets do not have server-side encryption enabled.   
## 2. Create a Lambda IAM Role   
- IAM Role Creation:   
Go to the IAM dashboard and create a new role for Lambda.   
Choose Lambda as the trusted entity.   
Attach the AmazonS3ReadOnlyAccess policy to allow Lambda to read bucket information.   
## 3. Create the Lambda Function       
- Lambda Function Creation:     
In the Lambda dashboard, click "Create Function."
Choose "Author from scratch," select Python 3.x as the runtime, and assign the IAM role created earlier.   
Add `lambda_function.py` to lambda    
## 4. Manual Invocation   
- Deploy and Test:   
Deploy the Lambda function and manually trigger it from the "Test" tab in the Lambda console.   
- Check Logs:   
After execution, check the Lambda logs to identify any unencrypted buckets. The log will indicate which buckets lack server-side encryption.   

*Since there are no unencrypted s3 bucket it is showing as all buckets are unencrypted*   
