import random

# Welcome Screen and Setpu
def welcome():
    print("----****WELCOM****----")
    print("-----Network Clash-----")
    print("A similar game where each element beats 2 and loses to 2 - perfectly balanced like Rock-Paper-Scissors-Lizard-Spoke!")
    print("-----**********-----")

def gameplay_operators():
    player1_name = input("Enter Player 1 name: ")
    game_mode = input("1. For Player vs Player\n 2. For Player vs Computer\n Enter your choice: ")
    match game_mode:
        case 1:
            print("You have choose Player vs Computer(PvC) mode!")
        case 2:
            print("You have choose Player vs Player(PvP) mode!")

    if game_mode == 2:
        player2_name = input("Enter player 2 name: ")
    else:
        player2_name = "Computer"

    total_rounds = input("How many rounds do you want to play? ")

def game_data():
    elements = [virus, firewall, packet, encryption, hacker]

if __name__ == __main__:
    welcome()