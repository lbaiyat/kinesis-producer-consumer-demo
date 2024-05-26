<h1>Kinesis Producer and Consumer Demo</h1>
<hr>

<div style="border-left: 1px solid #ccc; padding-left: 12px;">
<h2>Overview:</h2>
<p style="font-size: 15px">
This is a demo to programmatically manage a Kinesis Data Stream in AWS, with a stream producer and consumer.
The data being sent with the producer can be modified to send different payloads, and the consumer logic
can be modified to process the incoming payload in different manners.
</p>
</div>

<div style="border-left: 1px solid #ccc; padding-left: 12px;">
<h2>About AWS Kinesis Data Streams:</h2>
<p style="font-size: 15px">
AWS Kinesis Data Streams is a scalable real-time data streaming service designed to handle streams of data per second, enabling real-time data processing and analytics. It allows applications to continuously ingest and process large amounts of streaming data, such as log and event data, from various sources.
</p>
</div>

<div style="border-left: 1px solid #ccc; padding-left: 12px;">
<h2>Instructions:</h2>

<p style="font-size: 15px">
Getting the Data Stream up and running requires a few steps outlined below.
</p>


<h3>
Setup virtual environment
</h3>
<pre><code class="language-bash">
python3 -m venv venv;
pip install -r requirements.txt;
</code></pre>

<h3>
Export AWS Access Key and Secret Key to environment variables
</h3>
<pre><code class="language-bash">
export AWS_ACCESS_KEY_ID="{ACCESS_KEY_ID_STRING}";
export AWS_SECRET_ACCESS_KEY="{AWS_SECRET_ACCESS_KEY_STRING}";
</code></pre>


<h3>
Create the Kinesis Data Stream with the Stream Manager Script
</h3>
<p style="font-size: 13px; padding-left: 5px;">
Note: The 'create' keyword after the script is needed. Creating this Data Stream will incur AWS charges
</p>
<pre><code class="language-bash">
python3 kinesis_stream_manager.py create;
</code></pre>

<h3>
Run the stream producer
</h3>
<pre><code class="language-bash">
python3 producer.py;
</code></pre>
<p style="font-size: 13px; padding-left: 5px;">
Once the stream producer is running, you should see logs of the data being produced to the stream:
</p>

<div style="border: 1px solid #ccc; padding: 10px; margin: 10px 0;">
Put record: {'ShardId': 'shardId-000000000000', 'SequenceNumber': '49652411685917646928842325588740043300897428992379846658', 'ResponseMetadata': {'RequestId': 'd2178a59-a07c-325b-8cda-0734be33d144', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'd2178a59-a07c-325b-8cda-0734be33d144', 'x-amz-id-2': 'kufC0GJv4s1nZpdCYcj5BFQbc9YmRsDUhI65rQNBi6Dp3bP8+tNco8IJuGzUuIdfdSA52rapo2xft9+5uVDZZzhVEHHBIABp', 'date': 'Sun, 26 May 2024 19:19:09 GMT', 'content-type': 'application/x-amz-json-1.1', 'content-length': '110', 'connection': 'keep-alive'}, 'RetryAttempts': 0}}
</div>

<h3>
Run the stream consumer
</h3>
<pre><code class="language-bash">
python3 consumer.py;
</code></pre>
<p style="font-size: 13px; padding-left: 5px;">
Once the stream consumer is running, you should see logs of the data being consumed from the stream:
</p>

<div style="border: 1px solid #ccc; padding: 10px; margin: 10px 0;">
Received record: {'event': 'sample_event', 'value': 'sample_value', 'timestamp': 1716751145}
Received record: {'event': 'sample_event', 'value': 'sample_value', 'timestamp': 1716751146}
Received record: {'event': 'sample_event', 'value': 'sample_value', 'timestamp': 1716751147}
Received record: {'event': 'sample_event', 'value': 'sample_value', 'timestamp': 1716751148}
Received record: {'event': 'sample_event', 'value': 'sample_value', 'timestamp': 1716751149}
Received record: {'event': 'sample_event', 'value': 'sample_value', 'timestamp': 1716751150}
Received record: {'event': 'sample_event', 'value': 'sample_value', 'timestamp': 1716751151}
</div>
</div>


<div style="border-left: 1px solid #ccc; padding-left: 12px;">
<h2>Cleanup:</h2>
<p style="font-size: 15px">
Once you are done with the Kinesis Data Stream, you may wish to delete the instance to stop incurring further charges.
</p>

<h3>
Delete the Kinesis Data Stream with the Stream Manager Script
</h3>
<p style="font-size: 13px; padding-left: 5px;">
Note: The 'delete' keyword after the script is needed. The CloudFormation stack will be deleted as well as the Kinesis Stream defined by it.
</p>
<pre><code class="language-bash">
python3 kinesis_stream_manager.py delete;
</code></pre>

</div>



