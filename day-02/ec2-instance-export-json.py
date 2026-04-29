import boto3 
import json

session = boto3.Session(profile_name="demo-user1")
ec2 = session.client('ec2')

paginator = ec2.get_paginator('describe_instances')

instances = []

def get_name_tag(tags):
    if tags:
        for tag in tags:
            if tag['Key'] == 'Name':
                return tag['Value']
    return "N/A"

for page in paginator.paginate():
    for reservation in page['Reservations']:
        for instance in reservation['Instances']:
            instances.append({
                "InstanceId": instance.get('InstanceId'),
                "Name": get_name_tag(instance.get('Tags')),
                "VPC": instance.get('VpcId'),
                "InstanceType": instance.get('InstanceType'),
                "State": instance.get('State', {}).get('Name'),
                "PrivateIP": instance.get('PrivateIpAddress'),
                "PublicIP": instance.get('PublicIpAddress'),
                "AvailabilityZone": instance.get('Placement', {}).get('AvailabilityZone')
            })

with open('ec2_instances.json', 'w') as f:
    json.dump(instances, f, indent=4)

print("JSON exported: ec2_instances.json")