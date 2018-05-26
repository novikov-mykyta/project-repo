import boto3, time

sqs = boto3.resource('sqs', region_name="us-east-1")

tweets = sqs.get_queue_by_name(QueueName='python-queue')

while True:
  for message in tweets.receive_messages(MessageAttributeNames=['Author']):
    author_name = message.message_attributes.get('Author').get('name')
    print('Message body: %s' % message.body)
    message.delete()
  time.sleep(1)
