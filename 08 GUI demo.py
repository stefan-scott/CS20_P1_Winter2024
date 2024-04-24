# PySimple GUI Demo
# Mr. Scott
# April 22, 2024
# Reading String Data + Displaying Text

import random
import PySimpleGUI as sg

# Display Text on the Screen
sg.popup("Testing?")

# Request input from the user (str)
name = sg.popup_get_text("Enter name: ")
grade = sg.popup_get_text("Grade: ")

if grade == None or grade == "":  #indicates 'cancel', or 'x'
    grade = "9" #give a default value if none was given

sg.popup(f"Welcome, {name}. You will be in grade {grade}")
