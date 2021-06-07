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
    print("*** How to play ***")
    print()
    print("The rules of the game go here")
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


# Main routine goes here ...
played_before = yes_no("Have you played the game before? ")
if played_before == "no":
    instructions()

print("Program continues")

#Ask user how much they want to play with
how_much = num_check("How much do you want to play with? ", 0, 10)
print("You will be spending ${}".format(how_much))

STARTING_BALANCE = how_much
balance = STARTING_BALANCE

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

