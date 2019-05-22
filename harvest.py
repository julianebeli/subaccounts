import __init__
from api.requestor2 import API
import csv

# create a database of the subaccount details at our institution.
# GET / api/v1/accounts/: account_id/sub_accounts

cache_time = 60 * 60 * 24 * 30
api = API('beta', cache=cache_time)
params = dict(methodname='get_sub_accounts_of_account', account_id=1, recursive=True)
api.add_method(**params)
api.do()


headers = ['id', 'parent_account_id', 'name', 'sis_import_id', 'workflow_state']
with open('subaccount_data.csv', 'w', newline="\n") as f:
    writer = csv.DictWriter(f, fieldnames=headers, extrasaction='ignore')
    writer.writeheader()

    for a in api.results:
        writer.writerow(a)
