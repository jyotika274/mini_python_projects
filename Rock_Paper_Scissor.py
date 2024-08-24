import random

user_wins = 0
computer_wins = 0

option = ["rock","paper","scissor"]
print("Welcome to rock paper scissor game")

while True:
    user_input = input("Type Rock/Paper/Scissor or q to Quit : ").lower()

    if user_input == "q" :
        break
    if user_input not in option :
        continue

    random_number = random.randint(0,2)
    # rock = 0 paper= 1 scissor= 2
    computer_guess = option[random_number]

    if user_input == "rock" and computer_guess =="scissor":
        print("You Win!")
        user_wins +=1
    elif user_input == "paper" and computer_guess =="rock":
        print("You Win!")
        user_wins +=1
    elif user_input == "scissor" and computer_guess =="paper":
        print("You Win!")
        user_wins +=1
    elif user_input == "rock" and computer_guess =="rock":
        print("Game tied!")
    elif user_input == "rock" and computer_guess =="rock":
        print("Game tied!")
    elif user_input == "rock" and computer_guess =="rock":
        print("Game tied!")
    else:
        print("You Lost")
        computer_wins += 1
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")
    
        