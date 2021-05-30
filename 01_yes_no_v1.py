# Ask user if they have played before
show_instructions = input("Have you played Lucky Unicorn before?") .lower()

# If  yes, output 'program continues'
if show_instructions.lower() == "yes":
    print("Program continues")

elif show_instructions.lower() == "y":
    print("Display Instructions")

# If no output 'display instructions'
elif show_instructions.lower() == "no":
    print("Display Instructions")

elif show_instructions.lower() == "n":
    print("Display Instructions")

else:
    print("Please enter yes or no")
