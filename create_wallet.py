#Initial wallet generation code
from algosdk import account, mnemonic
private_key, address = account.generate_account()
mn=mnemonic.from_private_key(private_key)
print("Address: {}".format(address))
print("Mnemonic: {}".format(mn))