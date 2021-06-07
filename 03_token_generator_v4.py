import random

# main routine

STARTING_BALANCE = 100

balance = STARTING_BALANCE

# testing loop to generate 100 tokens
for item in range (0, 100):
    # generates random number that is wthen assigned to tokens
    chosen_num = random.randint(1,100)

    # adjust balance based on random number drawn
    # between 1 & 5 user gets unicorn and $4
    if 1 <= chosen_num <= 5:
        chosen ="unicorn"
        balance +=4
    # if between 6 and 36 user gets donkey and loses $1
    elif 6>= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1
    else:
        # if even number outside the above ranges a horse is drawn .50c increase
        if chosen_num % 2 == 0:
            chosen = "horse "
        # every other situation will draw a zebra
        else:
            chosen = "zebra"
        balance -= 0.5

    print("you got a {}. Your balance is {:.2f}".format(chosen,balance))

print("Start Balance: ${:.2f} \n Final Balance: ${:.2f} ".format(STARTING_BALANCE, balance))

