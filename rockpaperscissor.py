import random
while True:
    
   user = input("what's ur choice? 'r' --> rock,'p' -->  paper,'s' --> scissor\n")
   computer= random.choice(['r','p','s'])
   if user == computer: 
     print("its a tie")
   elif user=='r' and computer=='p':
     print("you lose!")
   elif user =='r' and computer=='s':
     print("you win!") 
   elif user =='p' and computer=='s':
     print("you lose!")  
   else :
     print("please try again!")
   play_again = input("play again? (y/n):")  
   if not play_again == 'y':
       print ("thanks for playing")
       break
