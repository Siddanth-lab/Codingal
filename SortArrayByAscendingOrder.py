import numpy as np
data_type=[("name", "S15"), ("class", int), ("height", float)]
data_type2=[("name", "S15"), ("marks", int)]
student_details=[("James", 5, 48.5), ("Nail", 6, 52.5), ("Paul", 5,42.10), ("Pit", 5, 40.11)]
student_marks=[("James",7), ("Nail",8), ("Paul", 4)]
students=np.array(student_details, dtype=data_type)
students2=np.array(student_marks, dtype=data_type2)
print("Original array: ")
print(students)
print("Sort by height")
print(np.sort(students, order="height"))
print(np.sort(students2, order="marks"))
