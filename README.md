# AlgoCert – Blockchain-Based Certificate Verification System

## Overview

AlgoCert is a Python-based blockchain application built on the Algorand TestNet.  
The project demonstrates how blockchain can be used to securely verify digital certificates by storing a cryptographic proof on-chain.

Instead of storing the entire certificate, the system stores a SHA256 hash of the certificate text in the transaction note field. This ensures immutability while keeping the original data private.


## Problem Statement

Digital certificates can be forged, edited, or duplicated.  
In most cases, verification requires manually contacting the issuing authority.

This creates dependency, delay, and trust issues.



## Proposed Solution

AlgoCert solves this problem by using blockchain as a verification layer:

1. The user enters certificate details (for example: name, course, date).
2. The system generates a SHA256 cryptographic hash of that text.
3. The hash is stored in an Algorand TestNet transaction note.
4. During verification, the hash is recomputed and compared with the stored blockchain record.

Since blockchain data is immutable, the stored proof cannot be altered.


## Technologies Used

- Python 3
- Algorand Python SDK
- SHA256 Cryptographic Hashing
- Algorand TestNet
- AlgoExplorer (for transaction verification)


## Project Structure


Algorand-Learning-Project/
│
├── src/
│   ├── create_wallet.py
│   ├── hash_utils.py
│   ├── store_certificate.py
│   └── verify_certificate.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```
git clone https://github.com/laasyakavuri/Algorand-Learning-Project.git
cd Algorand-Learning-Project
```

Create a virtual environment:


python3 -m venv venv
source venv/bin/activate


Install dependencies:


pip install -r requirements.txt
```



## How to Run the Project

Navigate to the source directory:

```
cd src


### 1. Create Wallet


python create_wallet.py
```

This generates a new Algorand wallet and displays the mnemonic phrase.



### 2. Store Certificate on Blockchain


python store_certificate.py
```

- Enter your wallet mnemonic.
- Enter the certificate text.
- The system generates a hash and stores it on Algorand TestNet.
- A transaction ID will be displayed.

You can view the transaction at:

https://testnet.algoexplorer.io



### 3. Verify Certificate


python verify_certificate.py
```

- Enter the transaction ID.
- Enter the original certificate text.
- The system compares hashes and confirms whether the certificate is valid.



## Example Output

```
Transaction ID: ABC123XYZ
Certificate Hash: a9f5d9c2...
Verification Result: VALID
```



## Key Learning Outcomes

- Understanding blockchain immutability
- Working with Algorand TestNet
- Transaction creation and signing
- Cryptographic hashing using SHA256
- Building a simple real-world blockchain use case



## Author

Laasya Kavuri  
GitHub: https://github.com/laasyakavuri