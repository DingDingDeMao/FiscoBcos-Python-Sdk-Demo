import sys
sys.path.append("D:\pythonsdk\python-sdk")
from client.bcosclient import BcosClient

client = BcosClient()
abi = [{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"string","name":"newname","type":"string"}],"name":"onset","type":"event"},{"inputs":[],"name":"get","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"n","type":"string"}],"name":"set","outputs":[],"stateMutability":"nonpayable","type":"function"}]

data = client.call("0xadf25f9821019abc8561b3d53fb82a064f1f8f1b",abi,"get")
print(data)
data = client.sendRawTransactionGetReceipt("0xadf25f9821019abc8561b3d53fb82a064f1f8f1b",abi,"set",["aa"])
print(data)
data = client.call("0xadf25f9821019abc8561b3d53fb82a064f1f8f1b",abi,"get")
print(data)

client.finish()