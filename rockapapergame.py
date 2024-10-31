import random

def get_userchoice():
    userchoice = input("Enter your choice (rock, paper, scissors): ").lower()
    while userchoice not in ["rock", "paper", "scissors"]:
        userchoice = input("Invalid choice.\n Please enter (rock, paper, or scissors): ").lower()
    return userchoice

def get_computerchoice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper") :
        return "You win"
    else:
        return "Computer wins"

def display_result(user, computer, result):
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")
    print(result)

def main():
    userscore = 0
    computerscore = 0

    while True:
        userchoice = get_userchoice()
        computerchoice = get_computerchoice()
        result = determine_winner(userchoice, computerchoice)
        display_result(userchoice, computerchoice, result)

        if "You win" in result:
            userscore += 1
        elif "Computer wins" in result:
            computerscore += 1

        print(f"\nScores => You: {userscore} | Computer: {computerscore}")

        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    main()
