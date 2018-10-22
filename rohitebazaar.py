from easygui import *
import sys

while 1:
    msgbox("Welcome to e bazar")

    msg ="In which category you want to buy items?"
    title = "Rohit Honde's Bazaar"
    choices=["Smartphones", "Clothes", "Stationary", "Diamonds"]
    choice = choicebox(msg, title, choices)
     
    msgbox("You chose: " + str(choice), "Confirm your choice")

    msg = "Do you want to continue?"
    title = "Please Confirm"
    if choice=="Smartphones":
        msgbox("Welcome to Smartphone bazaar")
        msg="Which Smartphone?"
    	title= "Rohit Honde's Smartphone Bazaar"
    	choices= ["RH 1---price=100000", "RH 2---price=200000", "RH 3---price=300000", "RH 4---price---400000"]
    	choice= choicebox(msg, title, choices)

        msgbox("You chose: " + str(choice), "Confirm your choice")

        msg = "Is it your final choice(Press continue to deliver at your default address)?"
        title = "Please Confirm"
        msgbox("Thank you for buying at Rohit Honde's Bazaar")
    elif choice=="Clothes":
        msgbox("Welcome to Clothes bazaar")
        msg="What type of clothes?"
    	title= "Rohit Honde's Clothes Bazaar"
    	choices= ["Shirt Mens-M size-----Rs 500","Shirt Women-M size-----Rs 500","Jeans Pant forMens-----Rs1000","Jeans Pant for Women-----Rs1000"]
    	choice= choicebox(msg, title, choices)

        msgbox("You chose: " + str(choice), "Confirm your choice")

        msg = "Is it your final choice(Press continue to deliver at your default address)?"
        title = "Please Confirm"
        msgbox("Thank you for buying at Rohit Honde's Bazaar")
    elif choice=="Diamonds":
        msgbox("Welcome to Diamond bazaar")
        msg="Which Diamond?"
    	title= "Rohit Honde's Diamond Bazaar"
    	choices= ["Pure Ruby price=1000000", "Pure Crystal diamond price=2000000"]
    	choice= choicebox(msg, title, choices)

        msgbox("You chose: " + str(choice), "Confirm your choice")

        msg = "Is it your final choice(Press continue to deliver at your default address)?"
        title = "Please Confirm"
        msgbox("Thank you for buying at Rohit Honde's Bazaar")
    elif choice=="Stationary":
        msgbox("Welcome to Stationary bazaar")
        msg="Choose your item?"
    	title="Rohit Honde's Smartphone Bazaar"
    	choices= ["Parker Pens Special Edition pack of 5 ---- price=Rs10000 ", "Scissors Pack of 10----- price=Rs500"]
    	choice= choicebox(msg, title, choices)

        msgbox("You chose: " + str(choice), "Confirm your choice")

        msg = "Is it your final choice(Press continue to deliver at your default address)?"
        title = "Please Confirm"
        msgbox("Thank you for buying at Rohit Honde's Bazaar")

    if ccbox(msg, title):    
        pass  
    else:
        sys.exit(0)
   
