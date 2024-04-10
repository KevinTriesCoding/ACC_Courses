import random
def main():
    lottery = []
    for num in range (7):
        lottery.append(random.randint(0, 9))
    print ("Winning numbers are: ")
    for num in lottery:
        print (num)

main()