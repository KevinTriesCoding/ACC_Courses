import random
import square 

def main():
    side = random.randint(1, 100)  # Generates a random integer between 1 and 100
    area = square.square_area(side)
    perimeter = square.square_perimeter(side)
    print(f"Side = {side}")
    print(f"Area = {area}")
    print(f"Perimeter = {perimeter}")

main()
