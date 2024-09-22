## 1. EC2 Setup
- Create EC2 Instances:    
In the AWS Management Console, navigate to the EC2 dashboard and launch two new t2.micro instances (or any free-tier instance type).    
- Tag the instances:   
For the first instance, add a tag with the key Action and value Auto-Stop.   
For the second instance, add a tag with the key Action and value Auto-Start.   
## 2. Create a Lambda IAM Role   
- IAM Role Creation:   
Go to the IAM dashboard and create a new role for Lambda.   
Choose Lambda as the trusted entity.    
Attach the AmazonEC2FullAccess policy (in production, restrict permissions for security).   
Complete the role creation and note down the role name.    
## 3. Create the Lambda Function   
- Lambda Function Creation:      
Open the Lambda dashboard and click "Create Function."    
Select "Author from scratch," give it a name, and choose Python 3.x as the runtime.     
Assign the IAM role you just created.        
Add the following code to your `start_stop_ec2.py` to your Lambda Function   

## 4. Manual Invocation   
- Deploy the Function:   
Save and deploy the Lambda function.   
- Test the Function:   
Manually trigger the Lambda function from the "Test" tab in the Lambda console.    
Go to the EC2 dashboard and verify that:   
Instances tagged with Auto-Stop are stopped.   
Instances tagged with Auto-Start are started.   
