import random

# main routine

tokens = ["unicorn", "donkey", "donkey","donkey",
          "horse", "horse", "horse",
          "zebra", "zebra", "zebra"]
STARTING_BALANCE = 100

balance = STARTING_BALANCE

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

print("Start Balance: ${:.2f} \n Final Balance: ${:.2f} ".format(STARTING_BALANCE, balance))

