#opens my_name in read mode to process data
name_file = open("my_name.txt", "r")

#processes first two lines of file and removes whitespace
name1 = name_file.readline().strip()
name2 = name_file.readline().strip()

#reads third line and converts str to int
age = int(name_file.readline())
name_file.close()

print(f"Name 1:  {name1}")
print(f"Name 2: {name2}")

half_age = (age/2)

print (f"Age: {age}")
print (f"Age divided by 2: {half_age}")