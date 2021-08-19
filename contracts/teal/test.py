from algosdk.v2client import algod
import json

algod_address = "http://localhost:33971"
algod_token = "90d4b56bf73a503142fe63f5dd9878f98715d013cb881ccc08c4541da62c152e"
algod_client = algod.AlgodClient(algod_token, algod_address)
status = algod_client.status()
print(json.dumps(status, indent=4))

private_key = "VCMJKWOY5P5P7SKMZFFOCEROPJCZOTIJMNIYNUBAH7LRO45JMJPQ===="
my_address = "VCMJKWOY5P5P7SKMZFFOCEROPJCZOTIJMNIYNUBAH7LRO45JMJPWQ7ETNM"

account_info = algod_client.account_info(my_address)
print("Account balance: {} microAlgos".format(account_info.get('amount')))