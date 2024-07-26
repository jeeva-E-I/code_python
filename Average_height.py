# Input a Python list of student heights

student_heights = input().split()
sum_heights = 0

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  sum_heights += student_heights[n]
  
total_students = len(student_heights)
average_height = sum_heights / total_students
average_height = round(average_height)

print(f"total height = {sum_heights}")
print(f"number of students = {total_students}")
print(f"average height = {average_height}")
