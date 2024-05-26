import uuid

import json
import time
from aws_util import create_boto_session
from config import KINESIS_STREAM_NAME

kinesis_client = create_boto_session().client('kinesis')

def put_records():
    while True:
        data = {
            'event': 'sample_event',
            'value': 'sample_value',
            'timestamp': int(time.time()),
        }

        response = kinesis_client.put_record(
            StreamName=KINESIS_STREAM_NAME,
            Data=json.dumps(data),
            PartitionKey=str(uuid.uuid4())
        )

        print(f'Put record: {response}\n')
        time.sleep(1)

if __name__ == '__main__':
    put_records()