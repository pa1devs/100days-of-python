#day-4-1-exercise
#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
import random

rand = random.random()
print(rand)

if rand >= 0.5:
  print("Heads")
else:
  print("Tails")
#solutionbyAyu
# random_side = random.randint(0, 1)
# if random_side == 1:
#   print("Heads")
# else:
#   print("Tails")



#day-4-2-exercise
# Split string method

import random
names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#print(len.names))

total = int(len(names))
#print(type(total))
rand = random.randint(0, total-1)

bill = (names[rand])

print(f"{bill} is going to buy the meal today!")

#day-4-3-exercise
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?\n")
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
hori = int(position[0])
vert = int(position[1])
map[vert-1][hori-1] ="X"
# row1[1] = "X"
# print(row1[1])
#Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")