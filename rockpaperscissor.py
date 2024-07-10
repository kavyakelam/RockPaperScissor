import random
while True:
    
   user = input("what's ur choice? 'r' --> rock,'p' -->  paper,'s' --> scissor\n")
   computer= random.choice(['r','p','s'])
   if user == computer: 
     print("It's a Tie")
   elif user=='r' and computer=='p':
     print("you lose")
   elif user =='r' and computer=='s':
     print("you win") 
   elif user =='p' and computer=='s':
     print("you lose")  
   else :
     print("Please try again!")
   play_again = input("play again? (y/n):")  
   if not play_again == 'y':
       print ("Thanks for Playing")
       break
