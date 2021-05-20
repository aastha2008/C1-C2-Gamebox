# guessing Game
# RPS
# Dice Roll
# Fortune teller
import random
def guessgame():
  print("This is the guessing game")
  # cpu will choose a random number between 1-10
  cpt_num= random.randint(1,10)
  # user guesses until they're correct
  user_number= int(input("Please guess a number: "))
  while(cpt_num != user_number):
    user_number= int(input("Sorry wrong number, try again. Please guess a number: "))
  else:
    print("Congrats!You've guessed the number!")


def RPS():
  print("This is rock paper scissors")
  print("1. Rock")
  print("2. Paper")
  print("3. Scissors")
  user_input = int(input("Please choose an option with a number."))
  cpt_number = random.randint(1,3)
  if(user_input == cpt_number):
    print("It's a tie") 
  #Winning Condition    
  #User _ computer  
  # 1    3
  # 2    1
  # 3    2
  elif( (user_input == 1 and cpt_number == 3) or (user_input == 2 and cpt_number == 1) or (user_input == 3 and cpt_number == 2) ):
    print("Congrats, you've won. Your number was " + str(user_input) + " and the computers number was " + str(cpt_number))

  #Losing Condition
  #User computer 
  #1       2
  #2       3
  #3       1
  elif( (user_input == 1 and cpt_number == 2) or (user_input == 2 and cpt_number == 3) or (user_input == 3 and cpt_number == 1) ):
    print("Sorry you've lost. Your number was " + str(user_input) + " and the computers number was " + str(cpt_number))

  else:
    print("Sorry this is an invalid input")

  

def diceRoll():
  print("This is the dice roll")
  
  number_result= random.randint(1,6)
  print("Your dice number is " + str(number_result))


def fortuneTeller():
  print("This is the fortune teller")
  #using a list, add 5 fortunes and randomly choose one to output to the user
  fortune_list= ["You'll have a great day", "You'll get good grades this week", "You'll get a ton of compliments today", "Be cautious of getting hurt by any physical activity", "You'll recieve a reward today"]
  
  #for x in fortune_list:
   # print("Your fortune is " + str(x))
  
  randomFortune= random.randint(0,len(fortune_list)-1)
  print("Your fortune is: " + fortune_list[randomFortune]) 

# 'main' filter
# this is where we define how we want our program to run

def main():
  print("This is the main function")

  # Tell the user their game options
  print(" 1. Guessing game")
  print(" 2. Rock paper scissors")
  print(" 3. Dice roll")
  print(" 4. Fortune teller")
  # Ask the user to choose one
  user_choice= int(input("Which one would you like to choose. Please specify a number: "))
  # Call the correct function based on user input
  if(user_choice == 1):
    guessgame()
  elif(user_choice == 2):
    RPS()
  elif(user_choice == 3):
    diceRoll()
  elif(user_choice == 4):
    fortuneTeller()
  else:
    print("Sorry this is an invalid input")
  

  #guessgame()
  #RPS()
  #diceRoll()
  #fortuneTeller()

# This controls the execution of our code
if __name__=="__main__":
  main()