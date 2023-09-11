import boto3
r = boto3.resource('s3')
b = r.Bucket("cloud-computing-bucket-2023")
b.upload_file("static/lion.jpeg", "lion.jpeg")
