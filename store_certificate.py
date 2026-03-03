#Blockchain storage logic
from algosdk.v2client import algod
from algosdk import transaction, mnemonic, account
from hash_utils import generate_hash

algod_address = "https://testnet-api.algonode.cloud"
algod_token = ""

client = algod.AlgodClient(algod_token, algod_address)

mn = input("Enter mnemonic: ")
private_key = mnemonic.to_private_key(mn)
sender = account.address_from_private_key(private_key)

text = input("Enter certificate text: ")

cert_hash = generate_hash(text)

params = client.suggested_params()

txn = transaction.PaymentTxn(
    sender=sender,
    sp=params,
    receiver=sender,
    amt=0,
    note=cert_hash.encode()
)

signed_txn = txn.sign(private_key)
txid = client.send_transaction(signed_txn)

print("Stored on blockchain!")
print("Transaction ID:", txid)
print("Certificate Hash:", cert_hash)