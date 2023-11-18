import random
import time

print(f"\n Welcome to the Rock paper scissors game \n"
      + "\t'Developed by Arqam'\n")
time.sleep(1)

while True:
    
    print("Choices: \n1.Rock \n2.Paper \n3.Scissor\n")
    

    # User Input

    user_choice = int(input("Enter your choice please: "))
    
    while user_choice > 3 or user_choice < 1:
        user_choice = int(input("Enter a valid choice plase :) : "))
                      
    if user_choice == 1:
        choice_name = 'Rock'

    elif user_choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissor'

    print("\nUser Choice is: ",choice_name)
    print("\nNow its Computers Turn....")

        

    # Computer Input 
    
    time.sleep(2)

    computer_action = random.randint(1,3)
    if computer_action == 1:
        comp_choice = 'Rock'

    elif computer_action == 2:
        comp_choice = 'Paper'
    else:
        comp_choice = 'Scissor'

    print("\nComputer Choice is: ", comp_choice  )
    print("\n")
    time.sleep(2)


    # In case of draw
    if user_choice == computer_action:
        print('Its a Draw\n',end="")
        result="DRAW"


    # In case of winning

    if (user_choice ==1 and computer_action==2):
        print('<== Paper wins ==>\n',end="")
        result='papeR'
    elif (user_choice ==2 and computer_action ==1):
        print('== Paper wins ==>\n',end="")
        result='Paper'
    

    
    if (user_choice ==2 and computer_action==3):
        print('<== Scissor wins ==>\n',end="")
        result='scissoR'
    elif (user_choice ==3 and computer_action ==2):
        print('== Scissor wins ==>\n',end="")
        result='Scissor'


    if (user_choice ==1 and computer_action==3):
        print('<== Rock wins ==>\n',end="")
        result='rock'
    elif (user_choice ==3 and computer_action ==2):
        print('== Rock wins ==>\n',end="")
        result='RocK'
    

    # Printing who won

    if result == 'DRAW':
        print("<== Its a tie ==>\n")
    if result == choice_name:
        print("<== User wins ==>\n")
    elif result != choice_name:
        print("<== Computer wins ==>\n")
    print("Do you want to play again? (Y/N)")

    ans = input("")
    print("\n")
    if ans == "n":
        time.sleep(1)
        print("\nThanks For Playing :) ")
        break
        
    else:
        continue



