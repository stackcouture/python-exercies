import boto3
import json
from datetime import datetime, UTC

session = boto3.Session(profile_name="demo-user1")

ec2 = session.client('ec2')
s3 = session.client('s3')

s3_bucket = "instannce-list-bucket"
s3_key = f"reports/ec2/ec2_report_{datetime.now(UTC).strftime('%Y-%m-%d_%H-%M-%S')}.json"

regions = [r['RegionName'] for r in ec2.describe_regions()['Regions']]

all_data = {}

def get_name_tag(tags):
    if tags:
        for tag in tags:
            if tag['Key'] == 'Name':
                return tag['Value']
    return "N/A"

for region in regions:
    regional_ec2 = session.client('ec2', region_name=region)
    paginator = regional_ec2.get_paginator('describe_instances')

    instances = []

    for page in paginator.paginate():
        for reservation in page['Reservations']:
            for instance in reservation['Instances']:
                instances.append({
                    "InstanceId": instance.get('InstanceId'),
                    "Name": get_name_tag(instance.get('Tags')),
                    "InstanceType": instance.get('InstanceType'),
                    "State": instance.get('State', {}).get('Name'),
                    "PrivateIP": instance.get('PrivateIpAddress'),
                    "PublicIP": instance.get('PublicIpAddress'),
                    "AZ": instance.get('Placement', {}).get('AvailabilityZone'),
                    "LaunchTime": str(instance.get('LaunchTime'))
                })

    all_data[region] = instances

json_data = json.dumps(all_data, indent=4)

s3.put_object(
    Bucket=s3_bucket,
    Key=s3_key,
    Body=json_data,
    ContentType='application/json'
)

print(f"Uploaded to s3://{s3_bucket}/{s3_key}")