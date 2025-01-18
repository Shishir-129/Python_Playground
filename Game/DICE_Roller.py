import random

dice_art={1:("┌─────────┐",
             "│         │",
             "│    ●    │",
             "│         │",
             "└─────────┘"),
          2:("┌─────────┐",
             "│  ●      │",
             "│         │",
             "│      ●  │",
             "└─────────┘"),
          3:("┌─────────┐",
             "│  ●      │",
             "│    ●    │",
             "│      ●  │",
             "└─────────┘"),
          4:("┌─────────┐",
             "│  ●   ●  │",
             "│         │",
             "│  ●   ●  │",
             "└─────────┘"),
          5:("┌─────────┐",
             "│  ●   ●  │",
             "│    ●    │",
             "│  ●   ●  │",
             "└─────────┘"),
          6:("┌─────────┐",
             "│  ●   ●  │",
             "│  ●   ●  │",
             "│  ●   ●  │",
             "└─────────┘")}

dice=[]
total=0
num_dice=int(input("Enter number of dice : "))
for die in range(num_dice):     #starts from 0 to num_dice-1
    dice.append(random.randint(1,6))  #includes both 1 and 6

for die in range(num_dice):
    total+=dice[die]
    for line in dice_art.get(dice[die]):
        print(line)
print(f"Total = {total}")