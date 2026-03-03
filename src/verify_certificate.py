#Added verification module
from hash_utils import generate_hash

text = input("Enter certificate text: ")
stored_hash = input("Enter blockchain hash: ")

if generate_hash(text) == stored_hash:
    print("VALID certificate")
else:
    print("INVALID certificate")