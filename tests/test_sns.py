import boto3
import os

endpoint_url = os.getenv("AWS_ENDPOINT_URL", "http://localhost:4566")

def test_sns_creation_deletion():
    sns_client = boto3.client('sns', endpoint_url=endpoint_url)
    
    topic_arn = sns_client.create_topic(Name="test-topic")["TopicArn"]
    assert sns_client.get_topic_attributes(TopicArn=topic_arn)

    sns_client.delete_topic(TopicArn=topic_arn)
