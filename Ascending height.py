import numpy as np

data_type = [('name', "S15"), ('grade', int), ('height', float)]

student_details = [('James', 5, 48.7), ('Webanyama', 6, 130.5),('Paul', 5, 42.10), ('Pit', 5, 40.11)]

students = np.array(student_details, dtype=data_type)

print("Original array: ")
print(students)
print("Sort by height")
print(np.sort(students, order='height'))