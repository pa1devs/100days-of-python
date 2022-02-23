rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
list = [rock,paper,scissors]
if choice >=3 or choice < 0:
  print("You chose wrong option, You Lost")
else:
  print("Your Choice")
  print(list[choice])
#list = [rock,paper,scissors]


computer = random.randint(0,2)

print("Computer Choice")
print(list[computer])

if choice == computer :
  print("It is a Draw.")
elif choice == 0 and computer == 1:
  print ("You Lost!")
elif choice == 0 and computer == 2:
  print ("You Won!")
elif choice == 1 and computer == 0:
  print ("You Won!")
elif choice == 1 and computer == 2:
  print ("You Lost!")
elif choice == 2 and computer == 0:
  print ("You Lost!")
elif choice == 2 and computer == 1:
  print ("You Won!")

