from easygui import *
import sys

list1=[]
sum=0

while 1:
    msgbox("Welcome to e bazar")

    msg ="In which category you want to buy items?"
    title = "Rohit Honde's Bazaar"
    choices=["Smartphones", "Clothes", "Stationary"]
    choice = choicebox(msg, title, choices)
     
    #msgbox("You chose: " + str(choice), "Confirm your choice")

    msg = "Do you want to continue?"
    title = "Please Confirm"
    if choice=="Smartphones":
        msgbox("Welcome to Smartphone bazaar")
        msg="Which Smartphone?"
    	title= "Rohit Honde's Smartphone Bazaar"
    	choices= ["RH 1---price=1000", "RH 2---price=2000", "RH 3---price=3000", "RH 4---price=4000"]
    	choice= choicebox(msg, title, choices)

        #msgbox("You chose: " + str(choice), "Confirm your choice")
	if choice=="RH 1---price=1000":

         msg = "Would you like to buy another item?"
         title = "Please Confirm"
         msgbox("Thank you for buying at Rohit Honde's Bazaar")
	 list1.append("RH 1---price=1000")
	 sum+=1000
	elif choice=="RH 2---price=2000":

         msg = "Would you like to buy another item?"
         title = "Please Confirm"
         msgbox("Thank you for buying at Rohit Honde's Bazaar")
	 list1.append("RH 2---price=2000")
	 sum+=2000
	elif choice=="RH 3---price=3000":

         msg = "Would you like to buy another item?"
         title = "Please Confirm"
         msgbox("Thank you for buying at Rohit Honde's Bazaar")
	 list1.append("RH 3---price=3000")
	 sum+=3000
	elif choice=="RH 4---price=1000":

         msg = "Would you like to buy another item?"
         title = "Please Confirm"
         msgbox("Thank you for buying at Rohit Honde's Bazaar")
	 list1.append("RH 4---price=4000")
	 sum+=4000

	
	 
    elif choice=="Clothes":
        msgbox("Welcome to Clothes bazaar")
        msg="What type of clothes?"
    	title= "Rohit Honde's Clothes Bazaar"
    	choices= ["Shirt Mens-M size-----Rs 500","Shirt Women-M size-----Rs 500","Jeans Pant forMens-----Rs1000","Jeans Pant for Women-----Rs1000"]
    	choice= choicebox(msg, title, choices)

        #msgbox("You chose: " + str(choice), "Confirm your choice")
	if choice=="Shirt Mens-M size-----Rs 500":
	 msg = "Would you like to buy another item?"
         title = "Please Confirm"
         msgbox("Thank you for buying at Rohit Honde's Bazaar")
	 list1.append("Shirt Mens-M size-----Rs 500")
	 sum+=500
	elif choice=="Shirt Women-M size-----Rs 500":
	 msg = "Would you like to buy another item?"
         title = "Please Confirm"
         msgbox("Thank you for buying at Rohit Honde's Bazaar")
	 list1.append("Shirt Women-M size-----Rs 500")
	 sum+=500
	elif choice=="Jeans Pant forMens-----Rs1000":
	 msg = "Would you like to buy another item?"
         title = "Please Confirm"
         msgbox("Thank you for buying at Rohit Honde's Bazaar")
	 list1.append("Jeans Pant forMens-----Rs1000")
	 sum+=1000
	elif choice=="Jeans Pant for Women-----Rs1000":
	 msg = "Would you like to buy another item?"
         title = "Please Confirm"
         msgbox("Thank you for buying at Rohit Honde's Bazaar")
	 list1.append("Jeans Pant for Women-----Rs1000")
	 sum+=1000
	 
	msg = "Would you like to buy another item?"
        title = "Please Confirm"
        msgbox("Thank you for buying at Rohit Honde's Bazaar")
    
    elif choice=="Stationary":
        msgbox("Welcome to Stationary bazaar")
        msg="Choose your item?"
    	title="Rohit Honde's Smartphone Bazaar"
    	choices= ["Parker Pens Special Edition pack of 5 ---- price=Rs1000 ", "Scissors Pack of 10----- price=Rs500"]
    	choice= choicebox(msg, title, choices)
	if choice=="Parker Pens Special Edition pack of 5 ---- price=Rs10000 ":
	 msg = "Would you like to buy another item?"
         title = "Please Confirm"
         msgbox("Thank you for buying at Rohit Honde's Bazaar")
	 list1.append("Parker Pens Special Edition pack of 5 ---- price=Rs1000 ")
	 sum+=1000
	elif choice=="Scissors Pack of 10----- price=Rs500":
	 msg = "Would you like to buy another item?"
         title = "Please Confirm"
         msgbox("Thank you for buying at Rohit Honde's Bazaar")
	 list1.append("Scissors Pack of 10----- price=Rs500")
	 sum+=500

        #msgbox("You chose: " + str(choice), "Confirm your choice")

        msg = "Would you like to buy another item?"
        title = "Please Confirm"
        msgbox("Thank you for buying at Rohit Honde's Bazaar")

    if ccbox(msg, title):    
        #list1.append(choice)
	pass
    else:
	textbox(msg='You have to pay',title='Final bill',text=str(list1)+str("You have to pay Rs")+str(sum),codebox=0)
	
	sys.exit(0)	
