###################### enabling s3 server access logging ##########################

import boto3

session = boto3.Session(profile_name='key-profile')
s3_client = session.client('s3')
s3=session.resource('s3')
my_bucket = []
for bucket in s3.buckets.all():
    my_bucket.append(bucket.name)


 #############Grant S3logdelivery group read_acp" permissions#######################
response = s3_client.put_bucket_acl(
    Bucket='target bucket',                                              # bucket where the logs will be stored
    AccessControlPolicy={
        'Owner': {
            'ID': 'Canonical ID',  #specific to account
            'DisplayName': 'owner'
        },
        'AccessControlList': {                                                          #grant Read permissions for log delivery Group
            'Grant': {
                'Grantee': {
                    'URI': 'http://acs.amazonaws.com/groups/s3/LogDelivery'
                },
                'Permission': 'READ_ACP'
            }
        }
    }
)

count = 0
for bucket in my_bucket:                                        # defining source and target bucket with prefix where the bucket server access logs will be stored
# #
 response= s3_client.get_bucket_logging(Bucket=bucket)

 if "LoggingEnabled" in response:
    print (bucket, "yes, string available")
    count +=1
 else:

  try:
   print (bucket, "no, string not found")

   response = s3_client.put_bucket_logging(
    Bucket=bucket,
    BucketLoggingStatus={
        'LoggingEnabled': {
            'TargetBucket': 'target-bucket',
            'TargetPrefix': bucket + "/" + bucket
        }
     }
    )
  except:
       pass
