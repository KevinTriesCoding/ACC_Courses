# Kevin Moye, Complete
# This module sets up the formule d = (1/2)gt^2 to calculate the distance of a falling object 

def falling_distance(second):
    # function to calculate the falling distance of an object over a given time.
    
    GRAVITY_CONSTANT = 9.8 
    distance = 0.5 * GRAVITY_CONSTANT * second**2
    return distance