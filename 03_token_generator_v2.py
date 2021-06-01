import random

# main routine

tokens = ["unicorn", "donkey", "horse", "zebra"]
balance = 100

# testing loop to generate 100 tokens
for item in range (0, 100):
    chosen = random.choice(tokens)

    # adjust balance
    if chosen == "unicorn":
        balance +=4
    elif chosen == "donkey":
        balance -= 1
    else:
        balance -= 0.5

    print("Token: {}, Balance: ${:.2f} ".format(chosen, balance))

