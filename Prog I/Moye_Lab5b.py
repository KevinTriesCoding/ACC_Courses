# Kevin Moye, Complete
# This program calculates and displays the distance an object falls under gravity over the first 10 seconds of its fall

import distance  

def main():
    # Creates a tabe to display where an object is at each second (1-10) of its fall.

    print("Time\tFalling Distance (meters)")
    print("-" * 30)  
    for second in range(1, 11):  # Looping through seconds 1 to 10
        total_fd = distance.falling_distance(second)  
        print(f"{second}\t {total_fd:.2f}")

main()
