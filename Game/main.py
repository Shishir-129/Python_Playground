import random 
computer=random.randint(1,101)
user=int(input("Guess the number : "))
print("")
attempt=1
while(computer!=user):
    if(user>computer):
        print("Lower number please !\n")
        user=int(input("Guess the number : "))
        print("")
    else:
        print("Higher number please !\n")
        user=int(input("Guess the number : "))
        print("")
    attempt+=1

if(computer==user):
    print(f"You have guessed it in {attempt} attempts.")
