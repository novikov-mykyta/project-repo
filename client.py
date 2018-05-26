import json, boto3, uuid

sqs = boto3.resource('sqs', region_name="us-east-1")

tweets = sqs.get_queue_by_name(QueueName='python-queue')
response = tweets.send_message(MessageBody='Hello World', MessageAttributes={
    'Author': {
        'StringValue': 'NikitaN',
        'DataType': 'String'
    }
})
