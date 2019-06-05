import io
from google.oauth2 import service_account
from google.cloud import vision
from google.cloud.vision import types

# import os
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "notes-all.json"

cread = service_account.Credentials.from_service_account_file('notes-all.json')

# Instantiates a client
client = vision.ImageAnnotatorClient(credentials=cread)

# Loads the image into memory
with io.open('test.jpg', 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')
for label in labels:
    print(label.description)
