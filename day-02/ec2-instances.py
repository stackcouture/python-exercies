import boto3
import json

session = boto3.Session(profile_name="demo-user1")
ec2 = session.client('ec2')

response = ec2.describe_instances()

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(f"Instance ID: {instance['InstanceId']}")
        print(f"Instance Type: {instance['InstanceType']}")
        print(f"State: {instance['State']['Name']}")
        print(f"Private IP: {instance.get('PrivateIpAddress')}")
        print("-" * 40)


    
