
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


print(student_heights)

total_height = 0
for height in student_heights:
  total_height += height
number_of_students =0 
for student in student_heights:
  number_of_students += 1
print(f"Students: {number_of_students}")  

avarage = round(total_height / number_of_students)
print(f"Avarage height is: {avarage}")







