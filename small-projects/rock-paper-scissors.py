# This script allows you to play rock-paper-scissors against the computer
# It asks for user input, displays randomly-generated output and keeps track of the score

# Import necessary packages
import random

# Create player class with name input and game input
class Player:

    def __init__(self):
        self.name= input('Hello there, what is your name?')
        self.score= 0


    def play(self):
        values={'r':'Rock','p':'Paper','s':'Scissors'}
        choice = 'x'
        possible_choices=['r','p','s']
        while choice.lower() not in values:

            choice = input('Please select r for rock, p for paper or s for scissors')
        print(f"You picked {values[choice]}")
        return possible_choices.index(choice.lower())

# Create computer class
class Computer:

    def __init__(self):
        self.score = 0

    def choice(self):
        values=['Rock','Paper','Scissors']
        computer_choice=random.randint(0,2)
        print(f"Computer picked {values[computer_choice]}!")
        return computer_choice

def winner(player_choice, computer_choice, player_score, computer_score):
    match = (player_choice, computer_choice)
    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice==0:
        if match==(0,2):
            player.score+=1
            print( f"{player.name} wins!")
        else:
            computer.score+=1
            print( "Computer wins!")
    elif player_choice ==1:
        if match==(1,2):
            computer.score+=1
            print( "Computer wins!")
        else: 
            player.score+=1
            print( f"{player.name} wins!" )
    else:
        if match==(2,0):
            computer.score+=1
            print( "Computer wins!")
        else: 
            player.score+=1
            print( f"{player.name} wins!" )
    print(f"{player.score}, {computer.score}")


player = Player()
computer = Computer()
game_on = True
while game_on ==True:   
    while computer.score < 3 and player.score < 3:
        winner(player.play(),computer.choice(),player.score,computer.score)
        print(f"**********\n Scores:\n {player.name}: {player.score}\n Computer: {computer.score}\n**********")
    if computer.score<player.score:
        print(f"{player.name} has won the game!")
    else:
        print("Computer has won the game!")
    if input("Play another round? y/n").lower()=='y':
        player.score = 0
        computer.score = 0
        game_on
    else:
        print("Ok bye!")
        game_on=False
