# Lucky Unicorn Base code
import random

# Function goes here
def yes_no(question):
    valid = False
    while not valid:
        # Ask user if they have played before
        response = input(question).lower().strip()

        # If  yes, output 'program continues'
        if response == "yes" or response == "y":
            response = "yes"
            return response

        # If no output 'display instructions'
        elif response == "no" or response == "n":
            response= "no"
            return response

        else:
            print("Please enter yes or no")


def instructions():
    statement_gen("How to play", "*")
    print()
    print("""Choose a starting amount, between $1 and $10.
Press <enter> to play.
Each round costs $1.
You will recieve a Zebra, Horse, Donkey or Unicorn.
Depending on what you get you may win some money. 
Unicorn: $5 
Horse: $0.50 
Zebra: $0.50
Donkey: Nothing""" )
    print()
    return""

def num_check(question,low,high):
    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            #ask the question
            response = int(input(question))

            # if amount is too low/high give error
            if low < response <= high:
                return response
            # output and error
            else:
                print(error)
        except ValueError:
            print(error)


def statement_gen(statement, decoration):

    sides = decoration * 3
    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return""
# Main routine goes here ...

statement_gen("Welcome to the Lucky Unicorn Game", "*")

played_before = yes_no("Have you played the game before? ")
if played_before == "no":
    instructions()
    print()


#Ask user how much they want to play with
how_much = num_check("How much do you want to play with? ", 0, 10)
print("You will be spending ${}".format(how_much))

STARTING_BALANCE = how_much
balance = STARTING_BALANCE

for item in range (0, 100):
# generates random number that is wthen assigned to tokens
    chosen_num = random.randint(1,100)

    # adjust balance based on random number drawn
    # between 1 & 5 user gets unicorn and $4
    if 1 <= chosen_num <= 5:
        chosen ="unicorn"
        prize_decoration = "!"
        balance +=4
    # if between 6 and 36 user gets donkey and loses $1
    elif 6>= chosen_num <= 36:
        chosen = "donkey"
        prize_decoration = "D"
        balance -= 1
    else:
        # if even number outside the above ranges a horse is drawn .50c increase
        if chosen_num % 2 == 0:
            chosen = "horse "
            prize_decoration = "H"
        # every other situation will draw a zebra
        else:
            chosen = "zebra"
            prize_decoration ="Z"
        balance -= 0.5

    outcome = "You got a {}.  Your balance is ${:.2f}".format (chosen,balance)

    statement_gen(outcome, prize_decoration)
    print ()

