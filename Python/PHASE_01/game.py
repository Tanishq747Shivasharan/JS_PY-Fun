import random

# Welcome Screen and Setpu.
def welcome():
    print("----****WELCOM****----")
    print("-----Network Clash-----")
    print("A game where each element beats 2 and loses to 2\n- perfectly balanced like Rock-Paper-Scissors-Lizard-Spoke!")
    print("-----**********-----")

# Setup Game
def gameplay_setup():
    player1 = input("Enter Player 1 name: ")
    
    game_mode = int(input("1. PvP\n2. PvC\nEnter choice: "))

    if game_mode == 1:
        player2 = input("Enter Player 2 name: ")
    else:
        player2 = "Computer"

    rounds = int(input("Enter number of rounds: "))

    return player1, player2, rounds, game_mode

# Game Data
elements = ["virus", "firewall", "packet", "encryption", "hacker"]

rules = {
    "virus": ["packet", "encryption"],
    "firewall": ["virus", "hacker"],
    "packet": ["firewall", "encryption"],
    "encryption": ["hacker", "virus"],
    "hacker": ["packet", "firewall"]
}

# Decide Winner
def decide_winner(p1_choice, p2_choice):
    if p1_choice == p2_choice:
        return "draw"
    elif p2_choice in rules[p1_choice]:
        return "player1"
    else:
        return "player2"

if __name__ == __main__:
    welcome()
    gameplay_operators()
    game_data()
