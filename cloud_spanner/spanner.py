from google.cloud import spanner
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('spanner_admin.json')

PROJECT_ID = 'info1-284008'
DATABASE_NAME = 'infodb'
SPANNER_INSTANCE = 'mydb-inst'

spanner_client = spanner.Client(project=PROJECT_ID,credentials=credentials)
instance = spanner_client.instance(SPANNER_INSTANCE)
database = instance.database(DATABASE_NAME)

# creating table inside database
query = '''CREATE TABLE Singers (
            SingerId     INT64 NOT NULL,
            FirstName    STRING(1024),
            LastName     STRING(1024),
            SingerInfo   BYTES(MAX)
        ) PRIMARY KEY (SingerId)
'''

database.update_ddl([query],'info')
print('table is created')

# inserting data into table
def insert_singers(transaction):
    row_ct = transaction.execute_update(
        "INSERT Singers (SingerId, FirstName, LastName) VALUES "
        "(12, 'Melissa', 'Garcia'), "
        "(13, 'Russell', 'Morales'), "
        "(14, 'Jacqueline', 'Long'), "
        "(15, 'Dylan', 'Shaw')"
    )
    print("{} record(s) inserted.".format(row_ct))

database.run_in_transaction(insert_singers)


# accessing data
with database.snapshot() as snapshot:
    results = snapshot.execute_sql('SELECT SingerId, FirstName, LastName FROM Singers')
    for row in results:
        print(u'SingerId: {}, FirstName: {}, LastName: {}'.format(*row))

# updating data
def update_singer(transaction):
    row_ct = transaction.execute_update(
        """UPDATE Singers
        SET FirstName = 'Raju'
        WHERE SingerId = 12"""
    )
    print("{} record(s) updated.".format(row_ct))
database.run_in_transaction(update_singer)


# delete Record
def delete_singer(transaction):
    row_ct = transaction.execute_update(
        """DELETE Singers
        WHERE SingerId = 15"""
    )
    print("{} record(s) Deleted.".format(row_ct))
database.run_in_transaction(delete_singer)






