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
