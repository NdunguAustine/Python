#a dict consists of key-value pairs
# dict = {"name":"Austine","color":"blue"}
import random
def get_choices():
    player_choice = input("Enter a choice (rock,paper,scissors: )")
    #lists are used to store multiple items in a single variable
    # Example  food = ["pizza","carrot","rice"]
    #          dinner = random.choice(food)
    #create a list to choose from using the random library we have imported
    options = ["rock","paper","scissors"]
    computer_choice = random.choice(options)

    choices = {"player":player_choice,"computer":computer_choice}
    return choices

#FUNCTION ARGUMENTS
def check_win(player,computer):
    #concatenating strings
    print("You chose "+ player+", computer chose "+computer)
    #using formatted strings, it can be written as:
    #print(f"You chose {player}, computer chose {computer}")
    #if, elif and else statements
    if player==computer:
        return "Its a tie"
    elif player=="rock" and computer=="scissors":
        return "Rock smashes scissors, You win!!!"
    elif player == "rock" and computer == "paper":
        return "Paper covers rock!, You lose."
    else:
        return "You haven't played."
    #using refactoring/Nested if to make it simpler and more understandable, we can do:
    #         if player==computer:
    #             return "Its a tie"
    #         elif player=="rock":
    #             if computer=="scissors":
    #                return "Rock smashes scissors, You win!!!"
    #         else:
    #             return "Paper covers rock. You lose."
check_win("rock","paper")

#formatted strings
age=25
print(f"James is {age} years old.")