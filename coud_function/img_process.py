import os
import tempfile
from google.cloud import storage
from PIL import Image

storage_client = storage.Client()

def hello_gcs(event, context):
     """  event (dict): Event payload.
     context (google.cloud.functions.Context): Metadata for the event.
     """

     file = event
     print('file data:',file)
     file_name = file['name']
     bucket_name = file['bucket']
     print(file_name)
     # downloading source file blob

     blob = storage_client.bucket(bucket_name).get_blob(file_name)

     # creating tempary file with data
     _, temp_local_filename = tempfile.mkstemp()
     temp_local_filename = temp_local_filename + file_name


     blob.download_to_filename(temp_local_filename)

     # resizing image
     img = Image.open(temp_local_filename)
     img.thumbnail((300, 300))
     img.save(temp_local_filename)


     # uploading file to new bucket
     bucket = storage_client.bucket('cloud_fun_res_test2654')
     new_blob = bucket.blob('res_'+file_name)
     new_blob.upload_from_filename(temp_local_filename)


     # Delete the temporary file.
     os.remove(temp_local_filename)
