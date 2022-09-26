# A python application console that allow a user to play Rock,Paper and Scissors against a computer
from random import randint
import re 
play_option = ['Rock','Paper','Scissors']

#assign a random play_option to the computer
computer = play_option[randint(0,2)] # randint returns a random int value from 0-2 from the play_option list

# input check function

def input_check(player_input):
    # check if the player input is not empty
    if player_input != '':
        # if it is not empty perform a regex to make the that the value are correct
        if re.search(r'^rock$',player_input,flags=re.IGNORECASE) or re.search(r'^scissors$',player_input,flags=re.IGNORECASE) or re.search(r'^paper$',player_input,flags=re.IGNORECASE):
            print('looks good - go ahead and play')
        else:
            print("Not a valid Play - check your input'")


# By default set the Player to False. I.e we will only exist the loop when the player is set to True
player = False
while player == False:
    #set player to True
    player = input('Enter Rock, Paper or Scissors?')
    input_check(player)
    if player == computer: # if player chooses and computer have the same play - it results into a tie game
        print('TIE!')
    elif player == 'Rock': # if the player chooses Rock, the computer has only two choices Paper and Scissors
        if computer == 'Paper':
            print('You lose!', computer, 'covers', player)
        else:
            print('you win!', player, 'smashes', computer)
    elif player == 'Scissors': # if the player chooses Scissors , the computer has only two options Rock and Paper
        if computer == 'Rock':
            print('You lose', computer, 'smahes', player)
        else:
           print('You win!',player,'smashes', computer)
    elif player == 'Paper': # if the player chooses Paper , the computer has only two options Scissors and Rock
        if computer == 'Scissors':
            print('You lose!', computer, 'cuts', player)
        else:
            print('You win', player, 'covers', computer)     
    #else:
        #print('Not a valid Play - check your input') # if input arg does not meet any of the criteria then we print this
    player = False # To continue the game after first try we set the player value back to False
    computer = play_option[randint(0,2)] # update the computer value


             
