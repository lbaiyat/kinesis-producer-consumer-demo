import boto3
import json
import time
from aws_util import create_boto_session
from config import KINESIS_STREAM_NAME

kinesis_client = create_boto_session().client('kinesis')

def get_records(shard_id, shard_iterator_type):
    response = kinesis_client.get_shard_iterator(
        StreamName=KINESIS_STREAM_NAME,
        ShardId=shard_id,
        ShardIteratorType=shard_iterator_type
    )

    shard_iterator = response['ShardIterator']

    while True:
        response = kinesis_client.get_records(
            ShardIterator=shard_iterator,
            Limit=100
        )

        records = response['Records']

        for record in records:
            data = json.loads(record['Data'])
            print(f'Received record: {data}')

        shard_iterator = response['NextShardIterator']

        time.sleep(1)

if __name__ == '__main__':
    response = kinesis_client.describe_stream(StreamName=KINESIS_STREAM_NAME)
    shard_id = response['StreamDescription']['Shards'][0]['ShardId']

    get_records(shard_id, 'LATEST')