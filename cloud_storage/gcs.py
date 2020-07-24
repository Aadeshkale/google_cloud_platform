from google.oauth2 import service_account
from google.cloud import storage

credentials = service_account.Credentials.from_service_account_file('cloud_storage.json')
storage_client = storage.Client(project='info1-284008',credentials=credentials)

# Download file from GCS


def download_file(bucket_name,filename):
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.get_blob(filename)
    # creating tempary file with data
    temp_local_filename =  filename
    blob.download_to_filename(temp_local_filename)

# download_file('mybuck-284008','download.jpeg')


# upload file to GCS
def upload_file(bucket_name,filename):

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(filename)
    blob.upload_from_filename(filename)
    # blob.make_public() for makeing file public


# upload_file('mybuck-284008', 'down_121.jpeg')

