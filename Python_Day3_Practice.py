#day-3-1-exercise
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check?\n"))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if number % 2 == 0:
  print(f"The number {number} is even")
else:
  print(f"The number {number} is odd")


#day-3-2-exercise
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI= (round((weight)/(height**2)))
#BMI=print(int(BMI))

if BMI < 18.5:
  print(f"Your BMI is {BMI}, you are underweight.")
elif BMI > 18.5 and BMI < 25:
  print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI > 25 and BMI < 30:
  print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI > 30 and BMI < 35:
  print(f"Your BMI is {BMI}, you are obese.")
else:
  print(f"Your BMI is {BMI}, you are clinically obese.")

#day-3-3-exercise
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 ==0 and year % 100 !=0 :
  print("Leap year.")
elif year % 100 ==0 and year % 400 ==0:
  print("Leap year.")
else:
  print("Not leap year.")

#day-3-4-exercise
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill =0
if size =="S":
  bill += 15
elif size =="M":
  bill += 20
elif size =="L":
  bill += 25

if add_pepperoni == "N":
  bill == bill
elif add_pepperoni == "Y" and size == "S":
  bill +=2
elif add_pepperoni == "Y" and size == "M" or "L":
  bill +=3

if  extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")


#day-3-5-exercis
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1lower = name1.lower()
name2lower = name2.lower()
#print(name1lower)
#print(name2lower)

count_T= name1lower.count('t') + name2lower.count('t')
count_R= name1lower.count('r') + name2lower.count('r')
count_U= name1lower.count('u') + name2lower.count('u')
count_E= name1lower.count('e') + name2lower.count('e')

true = count_T+count_R+count_U+count_E
#print(true)

count_L= name1lower.count('l') + name2lower.count('l')
count_O= name1lower.count('o') + name2lower.count('o')
count_V= name1lower.count('v') + name2lower.count('v')
count_E= name1lower.count('e') + name2lower.count('e')

love = count_L+count_O+count_V+count_E
score = int(str(true)+str(love))
#print(typ(score))

#print(f"Your score is {score}")

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")





