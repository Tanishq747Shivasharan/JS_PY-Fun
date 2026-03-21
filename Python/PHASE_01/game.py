import random
import os  
import getpass

def welcome():
    print("=" * 40)
    print("         NETWORK CLASH  ")
    print("=" * 40)
    print("5-way Cybersecurity Battle Game!")
    print("Each element beats 2, loses to 2.")
    print("=" * 40)

elements = ["virus", "firewall", "packet", "encryption", "hacker"]

rules = {
    "virus":      ["packet", "encryption"],
    "firewall":   ["virus", "hacker"],
    "packet":     ["firewall", "encryption"],
    "encryption": ["hacker", "virus"],
    "hacker":     ["packet", "firewall"]
}

flavor = {
    ("virus", "packet"):         "🦠 Virus corrupts the Packet!",
    ("virus", "encryption"):     "🦠 Virus breaks Encryption!",
    ("firewall", "virus"):       "🧱 Firewall blocks the Virus!",
    ("firewall", "hacker"):      "🧱 Firewall stops the Hacker!",
    ("packet", "firewall"):      "📦 Packet slips through Firewall!",
    ("packet", "encryption"):    "📦 Packet bypasses Encryption!",
    ("encryption", "hacker"):    "🔐 Encryption locks out the Hacker!",
    ("encryption", "virus"):     "🔐 Encryption neutralizes the Virus!",
    ("hacker", "packet"):        "👨‍💻 Hacker intercepts the Packet!",
    ("hacker", "firewall"):      "👨‍💻 Hacker breaks the Firewall!"
}

def one_time_setup():
    p1 = input("\nEnter Player 1 name: ").strip()

    while True:
        print("\n  1. Player vs Player")
        print("  2. Player vs Computer")
        mode_input = input("  Choose mode (1 or 2): ").strip()
        if mode_input in ["1", "2"]:
            mode = int(mode_input)
            break
        print("  ❌ Invalid! Enter 1 or 2 only.")

    if mode == 1:
        p2 = input("Enter Player 2 name: ").strip()
    else:
        p2 = "Computer"

    return p1, p2, mode

def get_round_count(p1, p2):
    print(f"\n  🎮 {p1}  vs  {p2}")   
    while True:
        rounds_input = input("  Enter number of rounds: ").strip()
        if rounds_input.isdigit() and int(rounds_input) > 0:
            return int(rounds_input)
        print("  ❌ Invalid! Enter a positive number.")

def get_choice(player_name):
    print(f"\n  Elements: {', '.join(elements)}")
    while True:
        choice = getpass.getpass(
            f"  {player_name}, enter your choice (hidden): "
        ).lower().strip()
        if choice in elements:
            return choice
        print(f"  ❌ '{choice}' is invalid! Choose from the list.")

def get_computer_choice():
    pick = random.choice(elements)
    print("  🤖 Computer is thinking...")
    return pick

def decide_winner(p1_choice, p2_choice):
    if p1_choice == p2_choice:
        return "draw"
    elif p2_choice in rules[p1_choice]:  
        return "player1"
    else:
        return "player2"                 

def show_scoreboard(p1, p2, p1_score, p2_score, draws, current, total):
    print("\n" + "-" * 40)
    print(f"  📊 SCOREBOARD  |  Round {current} of {total}")
    print("-" * 40)
    print(f"  {p1:<20} {p1_score} pts")
    print(f"  {p2:<20} {p2_score} pts")
    print(f"  {'Draws':<20} {draws}")
    print("-" * 40)

def play_one_session(p1, p2, mode):
    rounds   = get_round_count(p1, p2)  # ← only asks rounds
    p1_score = 0
    p2_score = 0
    draws    = 0

    for i in range(rounds):
        print(f"\n{'='*40}")
        print(f"  ⚔️  ROUND {i+1} of {rounds}")
        print(f"{'='*40}")

        p1_choice = get_choice(p1)

        if mode == 2:
            p2_choice = get_computer_choice()
        else:
            input(f"\n  ✅ {p1} locked in! Press Enter to pass to {p2}...")
            os.system('cls' if os.name == 'nt' else 'clear')
            p2_choice = get_choice(p2)

        print(f"\n  {p1:<20} → {p1_choice.upper()}")
        print(f"  {p2:<20} → {p2_choice.upper()}")

        result = decide_winner(p1_choice, p2_choice)

        if result == "draw":
            print("\n  ⚡ It's a Draw!")
            draws += 1
        elif result == "player1":
            print(f"\n  {flavor.get((p1_choice, p2_choice), '')}")
            print(f"  🎉 {p1} wins this round!")
            p1_score += 1
        else:
            print(f"\n  {flavor.get((p2_choice, p1_choice), '')}")
            print(f"  🎉 {p2} wins this round!")
            p2_score += 1

        show_scoreboard(p1, p2, p1_score, p2_score, draws, i+1, rounds)

    # Final Result
    print(f"\n{'='*40}")
    print("       🏆 FINAL RESULT 🏆")
    print(f"{'='*40}")
    print(f"  {p1:<20} {p1_score} pts")
    print(f"  {p2:<20} {p2_score} pts")
    print(f"  {'Draws':<20} {draws}")
    print(f"{'='*40}")

    if p1_score > p2_score:
        print(f"\n  🥇 {p1} is the Network Champion!")
    elif p2_score > p1_score:
        print(f"\n  🥇 {p2} is the Network Champion!")
    else:
        print("\n  🤝 Overall Draw! Evenly matched!")

def main():
    welcome()
    p1, p2, mode = one_time_setup()   

    while True:                       
        play_one_session(p1, p2, mode)

        while True:                    
            again = input("\n  🔁 Play again? (y/n): ").lower().strip()
            if again == 'y':
                print(f"\n  Welcome back {p1} & {p2}! 👊")
                break                  
            elif again == 'n':
                print(f"\n  👋 Thanks for playing, {p1} & {p2}!")
                print("  See you in the next Cyber Battle! 🌐")
                return                 
            else:
                print("  ❌ Please type y or n only.")

if __name__ == '__main__':
    main()