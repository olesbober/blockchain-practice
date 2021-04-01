# get_last_block.py
# problem description is in the README of the github repository 'blockchain_practice"

import hashlib as hl

def sha1(text):
    s = hl.sha1()
    s.update(text.encode('utf-8'))
    return s.hexdigest()

# remove all invalid transactions
def cleanTransactions(balances, transactions):
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
        self.nonce = 0
        block_to_string = previous_hash+", "+str(self.nonce)+", "+str(transactions)
        self.hash = sha1(block_to_string)
        while self.hash[0:4] != "0000":
            self.nonce += 1
            block_to_string = previous_hash+", "+str(self.nonce)+", "+str(transactions)
            self.hash = sha1(block_to_string)
    
    # hash getter
    def getHash(self):
        return self.hash

    # previous hash getter
    def getPreviousHash(self):
        return self.previous_hash

    # nonce getter
    def getNonce(self):
        return self.nonce

    # transaction getter
    def getTransactions(self):
        return self.transactions

    # print method
    def print(self):
        print("\""+self.hash+", "+self.previous_hash+", "+str(self.nonce)+", "+str(self.transactions)+"\"")

def getLastBlock(startBalances, pendingTransactions, blockSize):
    if blockSize > 5:   # max 5 blockSize
        blockSize = 5
    pendingTransactions = cleanTransactions(startBalances, pendingTransactions) # remove illegal transactions
    blockchain = [] # create empty blockchain
    while len(pendingTransactions) != 0:
        if len(pendingTransactions) >= blockSize:
            transactions = pendingTransactions[0:blockSize]
            pendingTransactions = pendingTransactions[blockSize:]
        else:
            transactions = pendingTransactions
            pendingTransactions = []
        if len(blockchain) == 0:    # genesis block
            blockchain.append(Block("0000000000000000000000000000000000000000", transactions))
        else:
            blockchain.append(Block(blockchain[-1].getHash(), transactions))
    # print the entire blockchain by block "hash, previous_hash, nonce, transactions"
    for i, b in enumerate(blockchain):
        print("Block "+str(i)+": ", end="")
        b.print()
    return blockchain[-1]

# test block creation (DONE)
#test_block = Block("Buy BAT, not BTC", [[0, 1, 5], [1, 2, 5]])

# test the cleanTransactions() method (DONE)
#print(cleanTransactions([5, 0, 0], [[0, 1, 5], [0, 1, 1], [1, 2, 5]]))

# test the example from the README.md (DONE)
#getLastBlock([5, 0, 0], [[0, 1, 5], [1, 2, 5]], 2)

# play around with input/output
startBalances = [5, 30, 7, 69, 34, 12, 100]
pendingTransactions = [[0, 1, 5],
                       [1, 2, 5],
                       [2, 0, 12],
                       [1, 3, 1],
                       [6, 4, 80],
                       [1, 5, 13],
                       [4, 2, 8],
                       [4, 2, 0],
                       [3, 6, 9],
                       [5, 1, 0],
                       [2, 3, 17]]
blockSize = 3
getLastBlock(startBalances, pendingTransactions, blockSize)