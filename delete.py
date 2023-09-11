import boto3
r = boto3.resource('s3')
r.Object('cloud-computing-bucket-2023', 'lion.jpeg').delete()
