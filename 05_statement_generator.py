# set decoration in function
def statment_gen(statement, decoration):

    sides = decoration * 3
    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return""

# main routine goes here
statment_gen("Welcome to the Lucky Unicorn Game", "*")
print()
statment_gen("Congratulations, you got a Unicorn", "!")