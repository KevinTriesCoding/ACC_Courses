file = open("number_list.txt", "w")

for num in range (50, 101):
#range of numbers 50-100
#adds each number to .txt file as str on a new line    
    file.write(str(num) + "\n")
print ("Data written to number_list.txt")