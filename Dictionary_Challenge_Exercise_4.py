#########################################################################
# Program: m7 Class exercise #7a Dictionary Challenge Exercise #4
# Programmer: Isaiah Vann
# Class: CMPR 114 Spring 2023
# Instructor: Professor Durendal Huynh
# Date: 3/27/23
#########################################################################

# TOTAL SALES APP: 
# Design a program that asks the user to enter a store’s sales for each day of the week. 
# The amount should be stored in a list. 
# Use loop to calculate the total sales for the week and display the result. 
# Plus output the results into a text file as well as the console.

def main():
    days_in_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    week_sales = []

    print('Enter the sales for the week.\n')

    index = 0
    for i in days_in_the_week:
        sale = float(input(f'Enter the sales for {i}: '))
        week_sales.insert(index, sale)
        index += 1

    total_sales = total(week_sales)
    print(f'The total sales of the week is ${total_sales: ,.2f}')

    write('week_sales.txt', week_sales, total_sales)

def total(numbers):
    sum = 0
    for value in numbers:
        sum += int(value or 0)
    return sum
    
def write(name, sales, total):
    output = open(name, 'w')
    for money in sales:
        output.writelines(str(money) + '\n')
    output.writelines(f'Total sales: ${total: ,.2f}')

main()