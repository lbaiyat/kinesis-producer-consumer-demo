import config
import argparse

from aws_util import (
    create_boto_session,
    create_kinesis_stack,
    delete_kinesis_stack,
)

template_file = 'app-kinesis.yaml'

def create_kinesis_data_stream():
    stack_name = config.CLOUDFORMATION_STACK_NAME
    session = create_boto_session()
    response = create_kinesis_stack(stack_name, template_file, session)
    print("Stack creation initiated. Stack ID:", response['StackId'])
def delete_kinesis_data_stream():
    stack_name = config.CLOUDFORMATION_STACK_NAME
    session = create_boto_session()
    response = delete_kinesis_stack(stack_name, session)
    print("Stack deletion initiated. Stack Name:", stack_name)

def get_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command', help='Please specify create or delete')

    create_parser = subparsers.add_parser('create', help='Create kinesis data stream')
    create_parser.set_defaults(func=create_kinesis_data_stream)

    delete_parser = subparsers.add_parser('delete', help='Delete kinesis data stream')
    delete_parser.set_defaults(func=delete_kinesis_data_stream)

    return parser


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func()
    else:
        parser.print_help()
