# Kevin Moye
# Complete
# A program the shows the gradual rise of the ocean's level by 1.8mm each year

#declaring the ocean level var and setting it at 0
ocean_level = 0

#print statements for headers/formatting
print (f"Year\tRise (in millimeters)")
print("_____________________________")

#for loop starts iterates 25 times and adds 1.8mm to the ocean level each time 
for year in range (1, 26):
    ocean_level += 1.8
    print (f"{year}\t{ocean_level: .1f}")