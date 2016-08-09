#!/usr/bin/env python3
# HW05_ex00_logics.py


##############################################################################



def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines  if even or odd
        Prints determination
        returns None
    """
    user_input = input("Give me your integer: ")
    try:
        user_input = int(user_input)
    except:
        print("Seems like it's not an integer. Try again")
    if user_input%2 == 0:
        print("It's even \n")
    else:
        print("It's odd \n")
    return None




def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    grid = list(range(1, 101))
    end_number = 0
    for i in range(10):
        if i in range(end_number+10) and i <=100:
            line = grid[end_number:end_number+10]
            print(str(line)+ '\n')
            end_number+=10





def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    average = 0
    list_of_nums = []
    print("\n Let's calculate the average. Throw me your numbers, one at a time. Type in 'done' when done:")
    while True:
        user_input = input("")
        if user_input == 'done':
            return sum(list_of_nums)/len(list_of_nums)
        else:
            try:
                user_input = float(user_input)
            except:
                print("It's not a number. Try again")
            list_of_nums.append(user_input)

    




##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    even_odd()
    ten_by_ten()
    print(find_average())

if __name__ == '__main__':
    main()
