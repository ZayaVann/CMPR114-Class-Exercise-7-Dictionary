#########################################################################
# Program: m7 Class exercise #7a Dictionary Challenge Exercise #1
# Programmer: Isaiah Vann
# Class: CMPR 114 Spring 2023
# Instructor: Professor Durendal Huynh
# Date: 3/27/23
#########################################################################

import tkinter as tk                # Import the gui interface controls
from tkinter import messagebox      # Imports the messagebox display

win = tk.Tk()                       # Create the window interface
win.geometry("300x200")             # Width x height in pixels
win.title("Students in Sports")     # Label for the title

# This program demonstrates various set operations.
baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])

Label = tk.Label(win, text = "Select a catagory to view its roster of students:").grid(column = 0, row = 0) 

# tkinter-related Function Definitions 
def quit():
    messagebox.showinfo("Information", "Thank you...")
    win.destroy() # closes the interface

# Display Base
def submitBaseballTeam():
    messagebox.showinfo("Baseball Team Members", baseball) 

def submitBasketballTeam():
    messagebox.showinfo("Basketball Team Members", basketball) 

def submitStudentsWhoPlayBoth():
    messagebox.showinfo("Baseball and Basketball Members", baseball.intersection(basketball))

def submitStudentsWhoPlayEither():
    messagebox.showinfo("Unique Team Members", baseball.difference(basketball)) 

def submitStudentsWhoPlayOnlyOne():
    messagebox.showinfo("Exclusive Team Members", baseball.symmetric_difference(basketball)) 

                        # Command Calls the click function
btnBaseBSubmit = tk.Button(win, text = "Baseball Team", command = submitBaseballTeam).grid(column = 0, row = 1) # Button Widget

btnBasketBSubmit = tk.Button(win, text = "Basketball Team", command = submitBasketballTeam).grid(column = 0, row = 2) # Button Widget

btnBaseAndBasketSubmit = tk.Button(win, text = "Baseball And Basketball Members", command = submitStudentsWhoPlayBoth).grid(column = 0, row = 3) # Button Widget

btnBaseOrBasketSubmit = tk.Button(win, text = "Baseball Or Basketball Members", command = submitStudentsWhoPlayEither).grid(column = 0, row = 4) # Button Widget

btnOnlyOneSportSubmit = tk.Button(win, text = "Exclusive Members", command = submitStudentsWhoPlayOnlyOne).grid(column = 0, row = 5) # Button Widget

                        # Command Calls the quit function
btnQuit = tk.Button(win, text = "Quit", command = quit).grid(column = 0, row = 6) # Button Widget

win.mainloop() # Ensure the interfaces stays on window