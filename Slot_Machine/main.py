import random

def spin_row(bet):
    symbols=['🛡️','🔔','💎','🔱','👑']
    row=[]
    for i in range(3):
        row.append(random.choice(symbols))
    print("**************************")
    print(end="      ")
    for i in row:
        print(f"{i}",end=" | ")
    print()
    print("**************************")
    if (row[0]==row[1]==row[2]):
        if(row[0]=='🛡️'):
            print("Congratulations!")
            print(f"You won ${bet*2}.")
            return bet*2
        elif(row[0]=='🔔'):
            print("Congratulations!")
            print(f"You won ${bet*4}.")
            return bet*4
        elif(row[0]=='💎'):
            print("Congratulations!")
            print(f"You won ${bet*7}.")
            return bet*7
        elif(row[0]=='🔱'):
            print("Congratulations!")
            print(f"You won ${bet*10}.")
            return bet*10
        else:
            print("Congratulations!")
            print(f"You won ${bet*13}.")
            return bet*13

    else:
        print("You lost!")
        return 0

def get_payout():
    pass

def main():
    print("***************************************")
    print("     Welcome! Welcome! Welcome!")
    print("***************************************")
    deposit=100
    is_running=True
    print(f"Your current balance : ${deposit}\n")
    print("Symbols : '🛡️','🔔','💎','🔱','👑'\n")

    while is_running:
        bet=input("Place your bet : $") 

        if not bet.isdigit():
            print("Enter valid input!")
            continue
        else:
            bet=int(bet)
            if (bet>deposit):
                print("Insufficient balance!")
                break
            else:
                deposit-=bet
        
        deposit+=spin_row(bet)
        print(f"Your current balance : ${deposit}\n")
        cont=input("Do you want to continue (y/n) : ")
        if (not cont.lower() == 'y'):
            print(f"Your Current Balance : ${deposit}")
            print("Thank you!")
            is_running=False
        print()

if __name__=="__main__":
    main()