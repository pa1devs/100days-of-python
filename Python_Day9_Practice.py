#day9 Ex 9.1
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
#student_grades = [Harry, Ron, Hermione, Draco, Neville]
#keyList = ["Harry", "Ron", "Hermione", "Draco", "Neville"]
student_grades =  {}

#TODO-2: Write your code below to add the grades to student_grades.👇
#for names in student_grades:
  #student_grades[names]
for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student]= "Outstanding"
  elif score > 80:
    student_grades[student]= "Exceeds Expectations"
  elif score > 70:
    student_grades[student]= "Acceptable"
  elif score <= 70:
    student_grades[student]= "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)

#day9 Ex 9.2

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
# cn =input("Enter the Name of the country: \n").lower()
# vs =input (("Enter Number of visits to the country: \n"))
# ct =input("Enter the Name of cities of that country: \n").lower()



def add_new_country(country, visits, cities):
  travel_log.append({"country":country, "visits":     visits,"cities":cities })
  
  




#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
add_new_country("India", 5, ["Delhi", "Hyd"])
print(travel_log)









