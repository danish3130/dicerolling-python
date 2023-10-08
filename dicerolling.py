print ('Hello World')
import random

print("Let's play Dice Rolling!")

# loop until the user chooses to quit
while True:
    # get user input for the number of dice to roll
    num_dice = int(input("How many dice do you want to roll? "))

    # check if the user input is valid
    if num_dice <= 0:
        print("Invalid input. Please try again.")
        continue

    # roll the dice and print the results
    print("Rolling the dice...")
    total = 0
    for i in range(num_dice):
        result = random.randint(1, 6)
        print(f"Dice {i+1}: {result}")
        total += result

    # print the total score
    print(f"Total score: {total}")

    # ask the user if they want to play again
    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() != 'y':
        break

print("Thanks for playing!")


