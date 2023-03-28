#########################################################################
# Program: m7 Class exercise #7a Dictionary Challenge Exercise #2
# Programmer: Isaiah Vann
# Class: CMPR 114 Spring 2023
# Instructor: Professor Durendal Huynh
# Date: 3/27/23
#########################################################################

def main():
    food = ['Pizza', 'Burgers', 'Chips']

    print('Here are the food items in the list')

    print(food)

    item = input("Which items in the list do you want to change?: ")

    try: #the try statement will try the batch of code below
        itemIndex = food.index(item) # gets the item in the list

        newItem = input("Enter the new value: ") # Entering the value to replace with

        food[itemIndex] = newItem # replace the old item with the new item

        print("Here is the revided list.")
        print(food)

    except ValueError: #if an error is found it will print the error
        print("The item was not found in the list.")
main()

