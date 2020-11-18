import boto3

#documentName = 'data/seg_pred/seg_pred/3.jpg'
documentName = '3.jpg'
bucketName = 'intelimages'

client = boto3.client('rekognition', 'us-west-1', aws_access_key_id = 'AKIAQOSDAUHZKRALOVHY', aws_secret_access_key = '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')
response = client.detect_labels(
        Image = {
            'S3Object': {'Bucket': bucketName, 'Name': documentName}
        },
        MaxLabels = 10,
        MinConfidence = 60)

for elabel in response["Labels"]:
    print("Label: {}, Confidence: {}%".format(elabel["Name"], elabel["Confidence"]))

