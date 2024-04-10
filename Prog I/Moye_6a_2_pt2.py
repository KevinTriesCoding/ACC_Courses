num_file = open("number_list.txt", "r")

for line in num_file:
    num = int(line.strip())
    print(num)

num_file.close()