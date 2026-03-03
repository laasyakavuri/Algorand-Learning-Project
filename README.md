# AlgoCert – Blockchain Certificate Verification System

## Overview:
AlgoCert is a Python-based blockchain project built on Algorand TestNet.
It allows users to generate a cryptographic hash of certificate text and store it immutably on blockchain.

## Problem:
Digital certificates can be forged or edited.
There is no simple way to verify authenticity.

## Solution:
1. Convert certificate text into SHA256 hash.
2. Store hash in Algorand transaction note field.
3. Verify authenticity by comparing hashes

## How To Run:

### Create Wallet-
python create_wallet.py

### Store Certificate-
python store_certificate.py

### Verify Certificate-
python verify_certificate.py

## Blockchain Explorer:
https://testnet.algoexplorer.io

## 👩‍💻 Author:
Laasya Kavuri


