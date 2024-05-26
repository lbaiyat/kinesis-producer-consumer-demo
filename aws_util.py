import boto3
import os

def create_boto_session():
    """ Make sure ACCESS_KEY_ID, and SECRET_ACCESS_KEY environment variables are exported"""
    access_key_id = os.environ['AWS_ACCESS_KEY_ID']
    secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
    region = "us-east-1"

    session = boto3.Session(
        aws_access_key_id=access_key_id,
        aws_secret_access_key=secret_access_key,
        region_name=region
    )
    return session

def create_kinesis_stack(stack_name, template_file, session):
    cloudformation = session.client('cloudformation')

    with open(template_file, 'r') as file:
        template_body = file.read()

    response = cloudformation.create_stack(
        StackName=stack_name,
        TemplateBody=template_body,
        Capabilities=['CAPABILITY_NAMED_IAM']
    )

    return response

def delete_kinesis_stack(stack_name, session):
    cloudformation = session.client('cloudformation')
    response = cloudformation.delete_stack(
        StackName=stack_name
    )
    return response
