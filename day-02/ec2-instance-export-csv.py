import boto3 
import csv

session = boto3.Session(profile_name="demo-user1")
ec2 = session.client('ec2')

paginator = ec2.get_paginator('describe_instances')

with open('ec2_instances.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    # Header
    writer.writerow([
        "InstanceId",
        "InstanceType",
        "State",
        "PrivateIP",
        "PublicIP",
        "AZ"
    ])

    for page in paginator.paginate():
        for reservation in page['Reservations']:
            for instance in reservation['Instances']:
                writer.writerow([
                    instance.get('InstanceId'),
                    instance.get('InstanceType'),
                    instance.get('State', {}).get('Name'),
                    instance.get('PrivateIpAddress'),
                    instance.get('PublicIpAddress'),
                    instance.get('Placement', {}).get('AvailabilityZone')
                ])

print("CSV exported successfully: ec2_instances.csv")


