def armn(x):       			#This is functiono call
    sum=0           		        # sum is initialised i.e to use it afterwards
    t=x              			#Temporarily put t=x
    while(t>0):      			#initialising while loop for sum of cube all digits
      d=t%10         			#It gives remainder after dividing by 10
      sum+=d**3      			# sum+=  is equal to sum= sum+some value  d**3 is dto power 3 ,it adds d to sum
      t=t//10        			# it gives quotient after dividing by 10, after this we come out of loop and it again goes to 5th line 
    if sum==x:      			# This checks whether sum =x  
      return 'Armstrong number'   	#if yes it prints Armstrong number
    else:                         
      return 'Not A N'            	#else it prints Not A N
x=int(input())         			#This accepts input from user
print(armn(x))      
