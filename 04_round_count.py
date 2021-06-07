# set balance for testing purposes
balance = 5
rounds_played = 0

play_again = input("Press <enter> to play....")
while play_again == "":
    rounds_played +=1
    print("Rounds Played: " ,rounds_played)

    balance -=1
    print("Balance: $", balance)

    if balance == 0:
        print("Sorry you have run out of money")
        break

    play_again = input("Press <enter> to play again or xxx to quit")
print("Your final balance is ${:.2f}".format(balance))