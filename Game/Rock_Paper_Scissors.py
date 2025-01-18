import random

print("----------------------------------------------------------------------")
print("                Welcome to ROCK PAPER SCISSORS!")
print("----------------------------------------------------------------------")
comp_value={"r":"Rock","p":"Paper","s":"Scissor"}
user_value={"r":"Rock","p":"Paper","s":"Scissor"}
running=True

while running:
    print()
    comp=random.choice(["r","p","s"])
    print("Computer chose.Now its your turn.")
    print()
    user=input("Choose 'r' for Rock , 'p' for Paper or 's' for Scissor : ").lower()

    if (user=='r' or user=='p' or user=='s'):
        if (user=='r' and comp=='p'):
            print(f"You Lost! ")
            print(f"You chose {user_value.get(user)} while computer chose {comp_value.get(comp)}.")
        elif (user=='r' and comp=='s'):
            print(f"You Won! ")
            print(f"You chose {user_value.get(user)} while computer chose {comp_value.get(comp)}.")
        elif (user=='p' and comp=='r'):
            print(f"You Won! ")
            print(f"You chose {user_value.get(user)} while computer chose {comp_value.get(comp)}.")
        elif (user=='p' and comp=='s'):
            print(f"You lost! ")
            print(f"You chose {user_value.get(user)} while computer chose {comp_value.get(comp)}.")
        elif (user=='s' and comp=='r'):
            print(f"You lose! ")
            print(f"You chose {user_value.get(user)} while computer chose {comp_value.get(comp)}.")
        elif (user=='s' and comp=='p'):
            print(f"You Won! ")
            print(f"You chose {user_value.get(user)} while computer chose {comp_value.get(comp)}.")
        else:
            print("Its a Draw!")
            print(f"You chose {user_value.get(user)} while computer also chose {comp_value.get(comp)}.")

    else:
        print("Invalid input.Try again!")

    opt=input(f"\nPress 'c' to Continue or 'e' to Exit : ").lower()

    if(opt=='e'):
        running=False

print("\nThank You! for playing.")