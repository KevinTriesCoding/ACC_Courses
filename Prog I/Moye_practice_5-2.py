
#global variable for kilometer to miles conversion and user input
conversion_factor = .6214
user_km = 0

def main():
    #asks the user for distance in kilometers for conversion
    global user_km
    user_km = float(input("Please enter a distance in kilometers to be converted: "))
    print (f"{user_km} kilometers is equal to {km_to_mi(): .2f} miles.")

def km_to_mi():
    #converts the given kilometer amount into miles
    converted_miles = user_km * conversion_factor
    return converted_miles


main()
