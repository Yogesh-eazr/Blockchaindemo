import hashlib

class NeuralBlockCoin:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list
        self.block_data = "-".join(transaction_list)+"-"+previous_block_hash

        #### hashlib.sha256 is used to cal hash value and we passs the transaction list into it
        ### than we use hexdigest() in order to get a string value out of the hash value.
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "Yog sends 3 NC to yogita"
t2 = "Yog sends 9 NC to raj"
t3 = "raj sends 3.9 NC to yog"
t4 = "rahul sends 5.7 NC to raj"
t5 = "Yog sends 10 NC to rahul"
t6 = "rahul sends 6.3 NC to Yog"

initial_block = NeuralBlockCoin("Innitial", [t1,t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = NeuralBlockCoin(initial_block.block_hash, [t3,t4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = NeuralBlockCoin(second_block.block_hash, [t5,t6])

print(third_block.block_data)
print(third_block.block_hash)



