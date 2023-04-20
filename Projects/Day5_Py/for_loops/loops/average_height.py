#Don't change the code below
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
#Don't change the code above 

#Write your code below this row 
total_heights = 0
for height in student_heights:
  total_heights = total_heights + height
print(total_heights)

number_of_student = 0 
for student in student_heights:
  number_of_student = number_of_student + 1
print(number_of_student)

average_height = round(total_heights / number_of_student)
print(average_height)