import uuid
from google.cloud import firestore
from google.oauth2 import service_account

PROJECT_ID = 'firepro--284008'
credentials = service_account.Credentials.from_service_account_file('firepro_admin.json')

firestore_client = firestore.Client(project=PROJECT_ID,credentials=credentials)
collection = firestore_client.collection('infodb')


# inserting data into collection

uid = str(uuid.uuid4())
data = {
    'uuid':uid,
    "username":"dhannu125",
    "email":"dhannu@gmail.com"
}
doc = collection.document(uid).set(data)
print('data is inserted')


# update document from collection

doc = collection.document('BAIA39ramEqiSRqjojGg')
doc.update({
    "name":"kunal_padalkar123"
})
print('document is updated')

# delete document from collection

doc = collection.document('BAIA39ramEqiSRqjojGg')
doc.delete()
print('document is deleted')


# query documents
docs = collection.where('username', u'==', 'dhannu125').stream()
for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')
