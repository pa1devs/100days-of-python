
#/day-5-1-exercise


# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total=0
for height in student_heights:
  total += height
#print(total)

stu=0
for num in student_heights:
  stu  += 1
#print(stu)

Avg_Hieght = round(total/stu)
print(Avg_Hieght)







#/day-5-2-exercise
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
#print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
score=0
for marks in student_scores:
  if marks > score:
    score = marks
print (f"The highest score in the class is: {score}")
   

#/day-5-3-exercise
#Write your code below this row 👇
total =0 
for num in range(0,101,2):
  total += num
print(total)
  



