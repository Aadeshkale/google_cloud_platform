# https://cloud.google.com/compute/docs/tutorials/python-guide
import csv
from google.oauth2 import service_account
from googleapiclient import discovery


credentials = service_account.Credentials.from_service_account_file('ce_admin.json')
compute_client = discovery.build('compute','v1',credentials=credentials)
PROJECT = 'xxxx-xxxx-xxx'
ZONE = 'xxx-xxx-xx'

def list_instances(compute, project, zone):
    result = compute.instances().list(project=project, zone=zone).execute()
    return result['items'] if 'items' in result else None

def write_csv(res):

    total_no_of_instance = len(res)
    with open('compute_info.csv', 'w',newline='') as csvfile:
        fieldnames = ['id', 'name','creationTimestamp','status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(total_no_of_instance):
            data_dict = {}
            data_dict['id'] = res[i]['id']
            data_dict['name'] = res[i]['name']
            data_dict['creationTimestamp'] = res[i]['creationTimestamp']
            data_dict['status'] = res[i]['status']
            writer.writerow(data_dict)


res = list_instances(compute=compute_client,project=PROJECT,zone=ZONE)
if res == None:
    print('No instances are there')
else:
    write_csv(res)
    print("Data is written into the file")