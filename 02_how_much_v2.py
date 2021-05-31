# Function goes here
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

# Main routine goes here
how_much = num_check("How much do you want to play with? ", 0, 10)

print("You will be spending ${}".format(how_much))

