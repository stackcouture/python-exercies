import boto3
import json

session = boto3.Session(profile_name="demo-user1")
ec2 = session.client('ec2')

response = ec2.describe_instances()

instances = []
for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append({
                "InstanceId": instance['InstanceId'],
                "InstanceType": instance['InstanceType'],
                "State": instance['State']['Name'],
                "PrivateIP": instance.get('PrivateIpAddress')
            })

print(json.dumps(instances, indent=4))
    
