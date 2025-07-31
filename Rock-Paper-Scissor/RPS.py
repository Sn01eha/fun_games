import random
choices=["rock","paper","scissors"]
def get_comp_choice():
    return random.choice(choices) #random.choice() picks one choice from list randomly

def get_user_choice():
    while True:
        user_input= input("choose rock paper scissors: ").lower()
        if user_input in choices:
            return user_input
        else:
            print("Invalid choice. Please enter valid choice.")

def determine_winner(user_choice, comp_choice):
    print(f"\n Your choice: {user_choice}") 
    print(f"\n Computer choice: {comp_choice}")
    if user_choice == comp_choice:
        return "It's a tie!!"
    elif (user_choice=="rock" and comp_choice=="scissors") or  (user_choice=="paper" and comp_choice=="rock") or (user_choice=="scissors" and comp_choice=="paper"):
        return "You win!!"
    else: 
        return "Computer wins!!"

def play_game():
    user_score=0
    computer_score=0
    rounds_played=0
    print("Welcome to Rock-papper-scissors!!")
    while True:
        rounds_played+=1
        print(f"\n --- Round {rounds_played}----")
        user_choice = get_user_choice()
        computer_choice = get_comp_choice()
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if "You win" in result:
            user_score+=1
        elif "Computer wins" in result:
            computer_score+=1
        print(f"Score: You {user_score} -- Computer {computer_score}")
        play_again = input("Play again? (y/n)").lower()
        if play_again!= 'y':
            print("\n Thanks for playing!!")
            break

if __name__ == "__main__":
    play_game()
