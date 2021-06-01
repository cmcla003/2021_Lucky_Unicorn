import random

# main routine

tokens = ["horse", "zebra", "donkey", "unicorn"]

# testing loop to generate 20 tokens
for item in range (0, 20):
    chosen = random.choice(tokens)
    print(chosen, end='\t')


