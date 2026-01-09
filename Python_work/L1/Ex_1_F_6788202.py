""" 
Student Name: Chavanon Opaspakkthon
Student ID: 6788202
Exercise No: 1
Part: F
Date of work: January 9, 2026
"""

# TASK 1.1
students = {
 'Alice': 82,
 'Bob': 67,
 'Charlie': 90
}

for name,score in students.items():
  print("Name: " + name + "\nScore: " + str(score))

count = 0
for scores in students.values():
  if scores >= 70:
    count += 1

print("Number of student who passed: ", (count))












