# Function goes here

error = "Please enter a number between 1 and 10\n"

valid = False
while not valid:
    try: 
        #ask the question
        response = int(input("How much do you want to play with? "))

        # if amount is too low/high give error
        if 0< response <= 10:
            print("You have asked to play with ${}". format(response))
        # output and error
        else:
            print(error)
    except ValueError:
        print(error)
# Main routine goes here