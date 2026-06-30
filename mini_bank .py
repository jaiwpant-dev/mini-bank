## mini bank 
 
print("welcome to HRD Bank")
pin=int(input("Entre you pin :"))


 
for i in range(1,4,1):
 	if pin ==1234:
 		print("access granted")
 		login=True
 		break
 	if pin != 1234:
 		x=(int(input("try again :")))
 	if x==1234:
 		print("access granted")
 		login=True
 		break
 	elif x!=1234:
 		print("incorrect")
 		login=False
 	elif x==1234:
 			print("Correct")
 			login=True
 			

if login!=True:
     print("access denied")
     exit()
 			
if login==True:
 	  print("Welcome How can we help you")
 	  print("(1)Check balance")
 	  print("(2)Deposite")
 	  print("(3)Transfer")
 	  print("(4)Cibil score")
 	  print("(5)Exit")
 	  
 	  
 	  
 	  def balance():
 	    balance=10000	
 	    print("Your balance is ",balance)
 	    
 	  def deposite():
 	   	deposite=int(input("Entre Amount :"))
 	   	total=deposite+10000
 	   	print("You current balance :",total)              
 	  def transfer():
 	   	go=int(input("Entre amount :"))
 	   	if go > 10000:
 	   		print("Low balance Unable to transfer")
 	   	elif go<= 10000:
 	   		withdraw=10000-go
 	   		print("transition successful, Amount left :",withdraw)
 	   	 
 	               
 	   		
 	  def cibil_score ():
 	    	print("Your cibil score is 800")
 	    	print("excellence")
 	    
 	  def exit():
 	  	print("Thanks for visiting have a nice day :) ")
 
 	    		
 	    		 
 	    	
print("Press 1 to check your balance")
print("press 2 to deposite")
print("press 3 to transfer ")
print("press 4 to check Cibil score")
print("press 5 to Exit")
 	    
menu=int(input(" Tap any no for menu :"))

 	   
if menu == 1:
 	    balance()
 	    print("Thanks for visting have a nice day :)")
elif menu==2:
 	    deposite()
 	    print("Thanks for visiting have a nice day :)")
elif menu ==3:
 	    transfer()
 	    print("Thanks for visiting have a nice day :)")
elif menu==4:
 	    cibil_score()
 	    print("Thanks for visiting have a nice day :)")
elif menu==5:
 	   
 	    exit()
 	    