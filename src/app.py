import json
from web3 import Web3
from config import Environment

try:
    env = Environment()
except:
    raise Exception("Dont have configured the project")

blockchain_address = 'http://127.0.0.1:7545' # ganache network
w3 = Web3(Web3.HTTPProvider(blockchain_address))

w3.eth.defaultAccount = w3.eth.accounts[0]

compiled_contract_path = '../build/contracts/TestContract.json'
deployed_contract_address = '0x49cA3f5E2E6ee5FB8476F68021Fa2888e2628e2B'

with open(compiled_contract_path) as f:
    contract_json = json.load(f)
    contract_abi = contract_json['abi']


contract = w3.eth.contract(address=deployed_contract_address, abi=contract_abi)

result = contract.functions.store(1993).transact()
print(result.hex())
message = contract.functions.retrieve().call()
print(message)