student_file = open("students.txt", "r")

print ("Name\t\tScore")
print("_" * 20)

for line in student_file:
    name = line.strip()
    score = int(student_file.readline().strip())
    print(f"{name}\t{score}")

student_file.close()