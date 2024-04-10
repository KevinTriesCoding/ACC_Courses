#inittialize and opens my_name in write mode
file = open("my_name.txt", "w")

#add two names and age
file.write("Kevin Moye\nDevin Foye\n")
file.write("25")

file.close()

print ("Data written to my_name.txt")
