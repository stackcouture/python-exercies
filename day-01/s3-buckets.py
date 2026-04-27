import boto3
session = boto3.Session(profile_name="demo-user1")
s3 = session.client('s3')

response = s3.list_buckets()

for bucket in response['Buckets']:
    print(bucket['Name'])


