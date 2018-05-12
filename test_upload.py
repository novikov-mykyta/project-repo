import boto3
s3 = boto3.resource('s3')
bucket = s3.Bucket('nikintan-project-bucket')
my_file = open('to_be_uploaded.txt', 'w+')
my_file.write('Here will be my test content, isint it cool?')
my_file.close()

bucket.put_object(
  Key='test.txt',
  Body=open('to_be_uploaded.txt', 'rb')
)
