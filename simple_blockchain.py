# simple_blockchain.py
# a blockchain is a chain of blocks, where every block is a list of transactions
# blocks are connected through hashing, where the hashes are based on the previous block's hash and the current transactions

import hashlib as hl

class Block:
    # each block will be based on the previous block's hash and its transactions
    def __init__(self, previous_hash, transactions):
        self.previous_hash = previous_hash
        self.transactions = transactions
        block_to_string = previous_hash + "".join(transactions) # with string transactions
        self.hash = hl.sha256(block_to_string.encode()).hexdigest()

class Blockchain:
    # initialize blockchain with genesis block
    def __init__(self, genesis_block):
        self.blockchain = [genesis_block]

    # method to add a set of transactions
    def add_transactions(self, transactions):
        temp_block = Block(self.blockchain[-1].hash, transactions)
        self.blockchain.append(temp_block)

    # print all blocks
    def print_blocks(self):
        for (i, b) in enumerate(self.blockchain):
            print("Block "+str(i)+": "+b.hash)

# create a simple hash
hash = hl.sha1("cryptocurrency is cool".encode('utf-8')).hexdigest()
#print(hash)

# create genesis block
genesis_block = Block("Buy BAT, not BTC", ["Oles bought 100 BAT", "Oles send Isaiah 40 BAT", "Rod bought 400 BAT", "Ailan bought 60 BAT"])
#print(genesis_block.hash)

# create blockchain
twinken_coin = Blockchain(genesis_block)
twinken_coin.add_transactions(["Oles bought 300 BAT", "Rod sent Ailan 70 BAT", "Isaiah sold 10 BAT"])
twinken_coin.add_transactions(["Roman bought 2000 BAT"])
twinken_coin.print_blocks()