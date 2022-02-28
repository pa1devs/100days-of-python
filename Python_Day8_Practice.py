#Write your code below this line 👇







#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
def paint_calc(height, width, cover):
  Area_of_wall= (height*width)
  No_of_Cans = round(Area_of_wall/cover)
  print(f"You'll need {No_of_Cans} cans of paint.")
paint_calc(height=test_h, width=test_w, cover=coverage)



  
      