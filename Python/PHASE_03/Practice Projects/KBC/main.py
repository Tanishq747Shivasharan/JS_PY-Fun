# - Create a list of prize amounts (money ladder), e.g. 1000, 2000, 5000 ... 1 crore
prize_amounts = [1000, 2000, 5000, 10000, 20000, 150000, 250000, 300000, 600000, 1000000]

# - Create a list/collection of questions, each with:
#     - the question text
#     - 4 options
#     - the correct option
questions = [
    "A TCP connection has a congestion window (cwnd) of 16 MSS. A packet loss is detected via three duplicate ACKs. Assuming standard TCP Reno behavior, what will the new cwnd be immediately after fast retransmit?",
    "8 MSS",
    "1 MSS",
    "16 MSS",
    "4 MSS",
    1,

    "A router receives an IPv4 packet with TTL = 1. What does the router normally do with the packet?",
    "Forward it normally and decrement TTL to 0",
    "Drop it and send an ICMP Time Exceeded message",
    "Drop it and send an ICMP Destination Unreachable message",
    "Forward it without modifying the TTL",
    2,

    "Which mechanism prevents a Layer 2 Ethernet switching loop when redundant paths exist between switches?",
    "ARP",
    "DHCP",
    "STP",
    "NAT",
    3,

    "A host has an IPv4 address of 192.168.10.130/26. Which subnet does this host belong to?",
    "192.168.10.0/26",
    "192.168.10.64/26",
    "192.168.10.128/26",
    "192.168.10.192/26",
    3,

    "Two routers establish an OSPF adjacency. Which OSPF packet type is primarily used to exchange summaries of the link-state database after the adjacency begins forming?",
    "Hello",
    "Database Description (DBD)",
    "Link-State Request (LSR)",
    "Link-State Acknowledgment (LSAck)",
    2,

    "A TCP client sends a SYN with an initial sequence number of 1000. The server responds with a SYN-ACK. What acknowledgment number should the server use if it successfully received the SYN?",
    "999",
    "1000",
    "1001",
    "1002",
    3,

    "Which BGP attribute is primarily used to influence outbound traffic from an autonomous system by making one path more preferred within that AS?",
    "MED",
    "LOCAL_PREF",
    "AS_PATH",
    "NEXT_HOP",
    2,

    "A switch receives an Ethernet frame whose destination MAC address is not present in its MAC address table. What will the switch normally do?",
    "Drop the frame immediately",
    "Send the frame only to the default gateway",
    "Flood the frame out all ports except the incoming port",
    "Send an ARP request for the destination MAC address",
    3,

    "A DNS resolver receives a response with a CNAME record instead of the requested A record. What will the resolver typically do next?",
    "Immediately return the CNAME as the final IPv4 address",
    "Query for the record pointed to by the CNAME",
    "Convert the CNAME into an MX record",
    "Discard the response because CNAME records are invalid",
    2,

    "A network uses NAT overload (PAT). Multiple internal hosts simultaneously access the same external web server using TCP port 443. How does the NAT device distinguish the different connections?",
    "By assigning each host a different destination IP address",
    "By modifying the Ethernet MAC address only",
    "By using different source port numbers in the translated connections",
    "By creating a separate DNS zone for every internal host",
    3
]
# - Set starting score/winnings = 0
score = 0 
# - Set current question number = 0
current_question_number = 0

# STEP 3: Main game loop
# - Loop through questions one by one (from easy to hard)
for question in range(0,60,6):
#   - Print current question number and prize for this level
    print(f"This is question {current_question_number} for {prize_amounts[score]}")

#   - Show the question and its 4 options
    print(f"{questions[question]}")
    print(f"1. {questions[question + 1]}")
    print(f"2. {questions[question + 2]}")
    print(f"3. {questions[question + 3]}")
    print(f"4. {questions[question + 4]}")

#   - Take input from player (which option they choose)
    answer_choice = int(input("Enter your choice: "))
#
#   - Check if chosen option == correct option
    if answer_choice == questions[question + 5]:
#       - If correct:
#           - Update winnings to current prize level
#           - Move to next question
        print("Correct answer!")
        score += 1
        current_question_number += 1 
    else:
#       - If wrong:
#           - Show correct answer
#           - Reduce winnings to nearest "safe" checkpoint (if any)
#           - End the game (break out of loop)
        print("Wrong answer!")
        print(f"The correct option was: {questions[question + 5]}")
        if score >= 5:
            score = 5
        elif score >= 3:
            score = 3
        else:
            score = 0

        print(f"You take home ₹{prize_amounts[score]}")
        break


# STEP 4: Safe checkpoints (optional, for later)
# - Decide certain question numbers as "safe" (e.g. Q5, Q10)
# - If player fails after crossing a safe checkpoint, they still keep that amount
# - If player fails before reaching first checkpoint, they get 0

# STEP 5: Lifelines (optional, add later once basic game works)
# - 50-50: remove two wrong options, leaving 2 to choose from
# - Audience poll: simulate a random weighted guess
# - Phone a friend: simulate a mostly-correct random guess
# - Each lifeline usable only once — track this with a flag/variable

# STEP 6: End of game
# - If player answers all questions correctly:
#     - Congratulate them, they won the full amount
if score == len(prize_amounts):
    print("Congratulations! You answered all questions correctly!")
    print(f"You won ₹{prize_amounts[-1]}")
# - If player quits or answers wrong:
#     - Show final winnings amount
else:
    print("Game over!")
    print(f"Your final winnings: ₹{prize_amounts[score]}")

# STEP 7 (optional extension):
# - Save player name + winnings to a file/list (leaderboard/history)