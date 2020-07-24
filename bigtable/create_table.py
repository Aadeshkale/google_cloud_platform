import uuid
from google.cloud import bigtable
from google.oauth2 import service_account


cred = service_account.Credentials.from_service_account_file('bigtable_admin.json')
PROJECT_ID = 'info1-284008'
bigtable_client = bigtable.Client(project=PROJECT_ID,credentials=cred,admin=True)


INSTANCE_ID = 'biginst'
TABLE_NAME = 'student'
COLUMNN_FAMILY = 'info'


# creating instance for bigtable database oprations
instance = bigtable_client.instance(INSTANCE_ID)
table = instance.table(TABLE_NAME)

if not table.exists():
    table.create()
    print(f'Table with name {TABLE_NAME} is created ')

# creating column family
try:
    col_fam = table.column_family(COLUMNN_FAMILY)
    col_fam.create()
    print(f'Column family with name {COLUMNN_FAMILY} is created')

except Exception as e:
    print('Exception:',e)


# adding data into col_fam columns
key = str(uuid.uuid4())

row = table.row(key.encode('utf-8'))
row.set_cell(COLUMNN_FAMILY,'name','raju')
row.set_cell(COLUMNN_FAMILY,'roll_no',354)
row.set_cell(COLUMNN_FAMILY,'address','Pune warje c215/12')
row.commit()

print('row is added')

# accessing data
row_key = 'f07cd5b5-29e2-4f78-8ba6-d58f2b3f51dc'
row = table.read_row(row_key.encode('utf-8'))

res = row.cells['info'][b'name'][0]
# print(row.cells)
print(res.value)


# updating data
row_key = 'f07cd5b5-29e2-4f78-8ba6-d58f2b3f51dc'
row = table.row(row_key)
row.set_cell(COLUMNN_FAMILY,'name','kavita')
row.commit()

# deleting complate row data
row_key = 'f07cd5b5-29e2-4f78-8ba6-d58f2b3f51dc'
row = table.row(row_key)
row.delete()
row.commit()

# deleting column family column
row = table.row(row_key)
row.delete_cell(COLUMNN_FAMILY,'address')
row.commit()

