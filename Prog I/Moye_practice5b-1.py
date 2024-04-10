import random
import circle  

def main():
    radius = random.uniform(1, 100)  # Generates a random float between 1 and 100
    area = circle.circle_area(radius)
    print(f"Radius = {radius:.2f}")
    print(f"Area = {area:.2f}")


main()
