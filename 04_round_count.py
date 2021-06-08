# set balance for testing purposes
balance = 5
rounds_played = 0

play_again = input("Press <enter> to play....").lower()
while play_again == "":
    rounds_played +=1
    print("*** Round number {} *** ".format(rounds_played))

    balance -=1
    print("Balance: $", balance)

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")

    else:
        play_again = input("Press <enter> to play again or xxx to quit")
print("Your final balance is ${:.2f}".format(balance))