# !/user/bin/env python3

# Created by Kevin Csiffary
# Date: Oct. 11, 2022
# This program asks the user to input an integer
# then checks if it is greater than, less than or equal to zero


def main():
    # Asks the user for their integer
    user_int = int(input("What is your integer? "))

    # Adds extra line
    print("")

    # Checks if their number is greater than, less than or equal to zero
    # Then displays the result
    if user_int > 0:
        print(str(user_int) + " is a positive number")
    elif user_int < 0:
        print(str(user_int) + " is a negative number")
    else:
        print("Your number is zero")


if __name__ == "__main__":
    main()
