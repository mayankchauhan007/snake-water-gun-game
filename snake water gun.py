""" It is a text-based Game, which you'll play against computer.
It takes an input from user as snake, water or gun.
You will get 10 attempts, after that it will display final score of the game.
You will also see the result of each strike.
"""
import random
choices = ['snake', 'water', 'gun']
game_counter = 0    # it will count number of strike to exit from the game
cpu = 0             # It will keep score of computer
player = 0          # It will keep score of player
print("\n", '\t'*5, "Welcome to Snake-Water-Gun game:\n")
while game_counter < 10:
    cpu_choice = random.choice(choices)     # It will select value from choices list randomly
    user_choice = input("Enter your selection: snake/water/gun: ").lower()  # It takes value from user and convert into lower case
    if user_choice in choices:
        if cpu_choice == "snake" and user_choice == 'gun':
            print(f"Player: {user_choice}\tComputer: {cpu_choice}\tPlayer won this strike\n")
            player += 1
        elif cpu_choice == "snake" and user_choice == 'water':
            print(f"Player: {user_choice}\tComputer: {cpu_choice}\tComputer won this strike\n")
            cpu += 1
        elif cpu_choice == "gun" and user_choice == 'water':
            print(f"Player: {user_choice}\tComputer: {cpu_choice}\tPlayer won this strike\n")
            player += 1
        elif cpu_choice == "gun" and user_choice == 'snake':
            print(f"Player: {user_choice}\tComputer: {cpu_choice}\tComputer won this strike\n")
            cpu += 1
        elif cpu_choice == "water" and user_choice == 'snake':
            print(f"Player: {user_choice}\tComputer: {cpu_choice}\tPlayer won this strike\n")
            player += 1
        elif cpu_choice == "water" and user_choice == 'gun':
            print(f"Player: {user_choice}\tComputer: {cpu_choice}\tComputer won this strike\n")
            cpu += 1
        elif cpu_choice == user_choice:
            print(f"Player: {user_choice}\tComputer: {cpu_choice}\tOops! Same guess, no one won this strike\n")
    else:
        print("invalid input, Try again\n")
    game_counter += 1

if player == cpu:
    print(f"Match tied: Player: {player}\tComputer: {cpu}")
elif player > cpu:
    print(f"Finally Player won the game: Player: {player}\tComputer: {cpu}\tTie: {10-player-cpu}")
else:
    print(f"Finally Computer won the game: Computer: {cpu}\tPlayer: {player}\tTie: {10-player-cpu}")