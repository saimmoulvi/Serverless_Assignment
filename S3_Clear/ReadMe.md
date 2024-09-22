## 1. S3 Setup   
- Navigate to the S3 dashboard:    
Go to the AWS Management Console and open the S3 service.   
Click "Create Bucket" and follow the prompts to create a new bucket.    
- Upload files:   
Upload multiple files to the bucket. If necessary, adjust your system's date or use old files to simulate files older than 30 days.   
## 2. Create Lambda IAM Role    
- Navigate to IAM:   
Open the IAM dashboard from the AWS console.   
Click "Roles" and then "Create Role."   
Choose Lambda as the trusted entity.   
- Attach S3 permissions:   
Attach the AmazonS3FullAccess policy.   
(In production, you’d narrow down the permissions to only allow operations on the specific S3 bucket).   
Complete the role creation process and note down the role’s name.   
## 3. Create Lambda Function   
- Navigate to the Lambda dashboard:   
In the AWS console, open the Lambda service.   
Click "Create Function" and choose "Author from scratch."   
- Configuration:   
Name your function, and choose Python 3.x as the runtime.   
Assign the IAM role you created in the previous step.   
Write the `lambda_function.py` code   
Replace your-bucket-name with the actual name of your S3 bucket.
## 4. Manual Invocation   
- Deploy the function:   
Save and deploy your Lambda function.   
- Test the function:   
Go to the "Test" tab in the Lambda console and manually trigger the function.   
- Confirm results:   
Navigate to your S3 bucket and confirm that only files newer than 30 days remain.   

