# read a score from the keyboard 
grade = input("What is your grade? [A, B, C, D, or F]: ") 
  
# check for passing grade 
if grade == 'A' or grade == 'a' or grade == 'B' or grade == 'b' or  grade == 'C' or grade == 'c' or grade == 'D' or grade == 'd': 
  print("Really execllent work!") 
elif grade == 'F' or grade == 'f': 
  print("Yikes -- you failed...") 
else:
  print("No, that's an invalid entry") 
