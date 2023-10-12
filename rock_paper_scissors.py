import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_move = input("Choose your fighter: [r]ock, [p]aper or [s]cissors: ")
if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    raise SystemExit("Invalid fighter. Try again...")
print(f"You've chosen your fighter and this is - {player_move}")
computer_random_number = random.randint(1, 3)
computer_move = ""

if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
else:
    computer_move = scissors
print(f"The computer choose his fighter and this is - {computer_move}!")

if (player_move == rock and computer_move == scissors) or (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
    print("You win!")
elif player_move == computer_move:
    print("Draw!")
else:
    print("You lose!")