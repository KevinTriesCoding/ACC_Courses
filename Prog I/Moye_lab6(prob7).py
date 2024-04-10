import random

#initialize random_num.txt
try:
    file = open("random_num.txt", "w")
except IOError:
        print("IO Error: Problem while initializing random_num.txt")
except Exception as err:
        print(err)

def main():
# allows user to declare how many numbers to be generated and then randomly generates said amount of numbers
    try:
        num_count = int(input("How many numbers would you like to be generated: "))
    except ValueError:
    #input validation
        print ("Value Error: Please enter an integer")
    except Exception as err:
        print(err)

    while (num_count != 0):
        random_num = random.randint(1, 500)
        print (random_num)
        file_write(random_num)
        num_count -= 1

def file_write (num):
# opens random_num in append mode to add generated numbers from main()
#parameter "num" allows me to pass random_num generated in main() to be appeneded to .txt file
    try:
        file = open("random_num.txt", "a")
        file.write(f"{num}\n")
    except IOError:
        print("IO Error: Problem while writing to random_num.txt")
    except Exception as err:
        print(err)

main()