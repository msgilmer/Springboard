import boto3

documentName = '3.jpg'
bucketName = 'intelimages'

client = boto3.client('rekognition', 'us-west-1', aws_access_key_id = '', aws_secret_access_key = '')
response = client.detect_labels(
        Image = {
            'S3Object': {'Bucket': bucketName, 'Name': documentName}
        },
        MaxLabels = 10,
        MinConfidence = 60
)

for elabel in response["Labels"]:
    print("Label: {}, Confidence: {}%".format(elabel["Name"], elabel["Confidence"]))

