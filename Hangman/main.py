import random
from seaofwords import words

hangman_art={0:("     ",
                "     ",
                "     "),
             1:("  o  ",
                "     ",
                "     "),
             2:("  o  ",
                "  |  ",
                "     "),
             3:("  o  ",
                " /|  ",
                "     "),
             4:("  o  ",
                " /|\\ ",
                "     "),
             5:("  o  ",
                " /|\\ ",
                " /   "),
             6:("  o  ",
                " /|\\ ",
                " / \\ ")}

def display_man(wrong_guess):
    print("****************************************")
    for line in hangman_art[wrong_guess]:
        print(f"{line:>15}")
    print("****************************************")

def diplay_answer(hint,answer):
    correct=0
    for i in range(len(answer)):
        if(hint[i]==answer[i]):
            correct+=1
    if (correct==len(answer)):
        print("---------------------------------------")
        print("              You Won!")
        print("---------------------------------------")
        return True
    return False

def main():
    print("---------------------------------------")
    print("       Welcome to Hangman Game!")
    print("---------------------------------------")
    answer=random.choice(words)
    hint=["_"]*len(answer)
    print(hint)
    wrong_guess=0
    is_running=True
    guessed_letters=""
    while is_running:
        guess=input("Enter a letter : ").lower()
        print()

        if len(guess)!=1 or not guess.isalpha():
            print("Invalid input!")
            continue

        elif guess in guessed_letters:
            wrong_guess+=1
            print(f"'{guess}' is already guessed!")
            print(hint)
            display_man(wrong_guess)
            if (wrong_guess==6):
                print("---------------------------------------")
                print("             You lost!")
                print("---------------------------------------")
                print(f"Original Word : {answer}")
                is_running=False

        elif guess in answer:
            guessed_letters+=guess
            for i in range(len(answer)):
                if answer[i]==guess:
                    hint[i]=guess
            print(hint)

        else:
            print("Wrong guess!")
            wrong_guess+=1
            print(hint)
            display_man(wrong_guess)
            if (wrong_guess==6):
                print("---------------------------------------")
                print("             You lost!")
                print("---------------------------------------")
                print(f"Original Word : {answer}")
                is_running=False

        if  diplay_answer(hint,answer):
            print(f"Original Word : {answer}")
            is_running=False
            
if __name__=="__main__":
    main()