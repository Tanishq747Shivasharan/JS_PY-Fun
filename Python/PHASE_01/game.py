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

# Main Game Loop
def play_game():
    p1, p2, rounds, mode = gameplay_setup()

    p1_score1 = 0
    p2_score2 = 0

    for i in range(rounds):
        print(f"\nRound {i+1}")

        p1_choice = input(f"{p1} choose: ").lower()

        if mode == 2:
            p2_choice = random.choice(elements)
            print(f"{p2} choose: {p2_choice}")
        else:
            p2_choice = input(f"{p2} choose: ").lower()

        result = decide_winner(p1_choice, p2_choice)

        if result == "player1":
            p1_score1 += 1
            print(f"{p1} wins this round!")
        elif result == "player2":
            p2_score2 += 1
            print(f"{p2} wins this round!")
        else:
            print("Draw!")

    print("\n--- Final Result ---")
    print(p1, ":", p1_score1)
    print(p2, ":", p2_score2)

    print("\n--- Winnner ---")
    if p1_score1 > p2_score2:
        print(f"{p1} wins!")
    else:
        print(f"{p2} wins!")

    print("---Thanks for playing---")

    restart = input("Would you like to play again? (y/n): ")
    if restart == 'y':
        play_game()
    else:
        print("See you soon!")

if __name__ == '__main__':
    welcome()
    play_game()
