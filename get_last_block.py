# get_last_block.py
# problem description is in the README of the github repository 'blockchain_practice"

import hashlib as hl

def sha1(text):
    s = hl.sha1()
    s.update(text.encode('utf-8'))
    return s.hexdigest()

# remove all invalid transactions
def clean_transactions(balances, transactions):
    transactions_to_remove = []
    for t in transactions:
        if balances[t[0]] < t[2]:
            transactions_to_remove.append(t)
        else:
            balances[t[0]] -= t[2]
            balances[t[1]] += t[2]
    for t in transactions_to_remove:
        transactions.remove(t)
    return transactions

class Block:
    # each block will be based on the previous_hash and its transactions
    def __init__(self, previous_hash, transactions):
        self.previous_hash = previous_hash
        self.transactions = transactions
        nonce = 0
        block_to_string = previous_hash+", "+str(nonce)+", "+str(transactions)
        self.hash = sha1(block_to_string)
        while self.hash[0:4] != "0000":
            nonce += 1
            block_to_string = previous_hash+", "+str(nonce)+", "+str(transactions)
            self.hash = sha1(block_to_string)

def getLastBlock(startBalances, pendingTransactions, blockSize):
    pass

# creat genesis block
genesis_block = Block("0000000000000000000000000000000000000000", [[0, 1, 5], [1, 2, 5]])

# test the clean_transactions() method (DONE)
#print(clean_transactions([5, 0, 0], [[0, 1, 5], [0, 1, 1], [1, 2, 5]]))