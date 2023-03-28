#########################################################################
# Program: m7 Class exercise #7a Dictionary Challenge Exercise #5
# Programmer: Isaiah Vann
# Class: CMPR 114 Spring 2023
# Instructor: Professor Durendal Huynh
# Date: 3/27/23
#########################################################################

# RAINFALL APP: 
# Design a program that let’s the user to enter the total rainfall 
# for each of the 12 months into a list. 
# The program should calculate and display the total rainfall 
# for the year, the average monthly rainfall, 
# the months with the highest and lowest amounts of rainfall. 
# Plus output the results into a text file as well as the console.

# Constants
year = 12

def main():
    # List of rainfall for each month
    monthly_rainfall = []

    # For Loop variables
    annual_rainfall = 0
    highest_rainfal = 0
    lowest_rainfall = 0

    # Month Accumulator
    month_count = 1

    # User Input for rainfall for each month of the year
    for month in range(year):
        rainfall = float(input(f"Enter the amount of rainfall for month number {month_count}: "))
        
        # Appending rainfall to list
        monthly_rainfall.append(rainfall)

        # CALCULATIONS:
        # Total Rainfall for the year
        annual_rainfall += rainfall

        # Highest amount of rainfall
        highest_rainfal = max(monthly_rainfall)

        # Lowest amount of rainfall
        lowest_rainfall = min(monthly_rainfall)

    # Average Monthly Rainfall
    avg_monthly_rainfall = (annual_rainfall / year)
    
    # Calling Functions:
    DisplayRainFallData(annual_rainfall, avg_monthly_rainfall, highest_rainfal, lowest_rainfall)
    WriteRainfall(monthly_rainfall, annual_rainfall, avg_monthly_rainfall, highest_rainfal, lowest_rainfall)

# Displaying Rainfall Data
def DisplayRainFallData(annual_rainfall, avg_monthly_rainfall, highest_rainfal, lowest_rainfall):
    # Display Rainfall Data
    print(f"\nThe total amount of rainfall is: {annual_rainfall} inches.")
    print(f"The Average Monthly Rainfall is: {avg_monthly_rainfall: ,.2f} inches.")
    print(f"The highest amount of rainfall is: {highest_rainfal} inches.")
    print(f"The lowest amount of rainfall is: {lowest_rainfall} inches.")

# Outputting the Rainfall data into a text file
def WriteRainfall(monthly_rainfall, annual_rainfall, avg_monthly_rainfall, highest_rainfal, lowest_rainfall):
    # Opening Text File
    output = open('Rainfall.txt', 'w')

    # Outputting all Rainfall data to Text File
    # Rainfall for each month
    for month in monthly_rainfall:
        output.writelines(str(month) + ' inches\n')

    # Outputting Calculations into text file
    output.writelines(f"\nThe total amount of rainfall is: {annual_rainfall} inches.\n")
    output.writelines(f"The Average Monthly Rainfall is: {avg_monthly_rainfall: ,.2f} inches.\n")
    output.writelines(f"The highest amount of rainfall is: {highest_rainfal} inches.\n")
    output.writelines(f"The lowest amount of rainfall is: {lowest_rainfall} inches.\n")

# Calling main
main()