import boto3

# Initialize EC2 client
ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    # Describe instances with Auto-Stop and Auto-Start tags
    response = ec2.describe_instances(Filters=[
        {'Name': 'tag:Action', 'Values': ['Auto-Stop', 'Auto-Start']}
    ])

    # Stop Auto-Stop instances and start Auto-Start instances
    stopped_instances = []
    started_instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            if instance['Tags'][0]['Value'] == 'Auto-Stop':
                ec2.stop_instances(InstanceIds=[instance['InstanceId']])
                stopped_instances.append(instance['InstanceId'])
            elif instance['Tags'][0]['Value'] == 'Auto-Start':
                ec2.start_instances(InstanceIds=[instance['InstanceId']])
                started_instances.append(instance['InstanceId'])

    # Print instance IDs that were affected for logging purposes
    print(f'Stopped instances: {stopped_instances}')
    print(f'Started instances: {started_instances}')

    return {
        'statusCode': 200,
        'statusMessage': 'Instances stopped and started successfully'
    }
