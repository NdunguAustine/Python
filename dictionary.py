#a dict consists of key-value pairs
# dict = {"name":"Austine","color":"blue"}
import random
def get_choices():
    player_choice = input("Enter a choice (rock,paper,scissors: )")
    #create a list to choose from using the random library we have imported
    options = ["rock","paper","scissors"]
    computer_choice = random.choice(options)

    choices = {"player":player_choice,"computer":computer_choice}
    return choices

choices=get_choices()
print(choices)

#lists are used to store multiple items in a single variable
# Example  food = ["pizza","carrot","rice"]
#          dinner = random.choice(food)