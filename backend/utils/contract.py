from web3 import Web3
import json

abi_path = '/home/kevin/blockchain/Authentium-R-D/contracts/solidity/build/contracts/'
address = '0xdBE998575E41934EF700dE5aa92FEF2Cf5BB695D'
private_key = '0xe4e829db5a206fddbb5a4df01f5413e71ccdae37e44a7531acb580dfae13b98c'

def get_contract():
    w3 = Web3(Web3.HTTPProvider('https://kovan.infura.io/v3/0db1e82f224a4fa5b282f92a37e96988'))
    w3.eth.default_account = w3.eth.account.from_key(private_key).address

    token = json.loads(open(abi_path + 'AuthentiumToken.json', 'r').read())
    return w3, w3.eth.contract(address=address, abi=token['abi'])

def transact(fn_name):
    w3, contract = get_contract()
    nonce = w3.eth.get_transaction_count(w3.eth.default_account)
    contract_txn = contract.get_function_by_signature(fn_name)().buildTransaction({
        'value': 13*(10**15),
        'gas': 8000000,
        'gasPrice': w3.toWei('1', 'gwei'),
        'nonce': nonce,
    })

    signed_txn = w3.eth.account.sign_transaction(contract_txn, private_key=private_key)
    res = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    res = w3.eth.wait_for_transaction_receipt(res)
    
    return res

def call_function(fn_name, *args):
    w3, contract = get_contract()
    res = contract.get_function_by_signature(fn_name)(*args).call()

    return res

def get_balance(address):
    w3, contract = get_contract()

    return w3.eth.get_balance(address)