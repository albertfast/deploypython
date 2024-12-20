# read a score from the keyboard 
grade = input("What is your grade? [A, B, C, D, or F]: ").lower()
  
# check for passing grade 
if grade == 'a' or grade == 'b' or grade == 'c': 
  print("Really execllent work!") 
elif grade == 'd' or grade == 'f':
  print("Yikes -- you failed...")
else:
  print("No, that's an invalid entry")
    



