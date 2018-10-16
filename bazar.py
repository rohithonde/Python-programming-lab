from easygui import *
import sys

while 1:
    msgbox("Welcome to e bazar")

    msg ="In which category you want to buy items?"
    title = "Rohit Honde's Bazaar"
    choices = ["Elctronics", "Kapde", "Khau", "Chasme"]
    choice = choicebox(msg, title, choices)
     
  # note that we convert choice to string, in case
    # the user cancelled the choice, and we got None.
    msgbox("You chose: " + str(choice), "Confirm your choice")

    msg = "Do you want to continue?"
    title = "Please Confirm"
    if choices==Electronics:

    if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:
        sys.exit(0)


