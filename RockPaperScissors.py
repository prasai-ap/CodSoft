import random
comp_choice = random.choice(["Rock", "Paper", "Scissors"])

print("Enter your choice")
print("1: Rock")
print("2: Paper")
print("3: Scissors")
u_choice = int(input())
if u_choice == 1:
    u_choice = "Rock"
elif u_choice == 2:
    u_choice = "Paper"
elif u_choice == 3:
    u_choice = "Scissors"
else:
    print("Invalid input, please enter 1, 2, or 3.")
    exit()

print(f"Your choice: {u_choice}")
print(f"Computer choice: {comp_choice}")

if u_choice == comp_choice:
    print("It's a tie!")
elif (u_choice == "Rock" and comp_choice == "Scissors") or (u_choice == "Paper" and comp_choice == "Rock") or (u_choice == "Scissors" and comp_choice == "Paper"):
    print("You win!")
elif (comp_choice == "Rock" and u_choice == "Scissors") or (comp_choice == "Paper" and u_choice == "Rock") or (comp_choice == "Scissors" and u_choice == "Paper"):
    print("Computer wins!")
else:
    print("It's a Tie")

 
