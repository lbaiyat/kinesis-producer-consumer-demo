import config

from aws_util import (
    create_boto_session,
    create_kinesis_stream,
)

if __name__ == '__main__':
    stack_name = config.CLOUDFORMATION_STACK_NAME
    template_file = 'app-kinesis.yaml'
    session = create_boto_session()
    response = create_kinesis_stream(stack_name, template_file, session)
    print("Stack creation initiated. Stack ID:", response['StackId'])
