def main ():
    try:
        #opens number_list.txt
        file = open('number_list.txt', 'r')

        total = 0
        count = 0

        # check each line for number inputs, clearing whitespace
        for line in file:
            file_line = line.strip()
            try:
                # converts line text into ints
                number = int(file_line)
                total += number  # Add to total
                count += 1  # Keeping track of the numbers processed
            except ValueError:
                # error handling for non-numbers
                print(f"Error -- This is not a number: {file_line}")

        file.close()
        if count == 0:
            print("No numbers processed")
        else:
            average = total / count
            print(f"Sum of number list: {total}")
            print(f"Average of number list: {average}")

    except IOError:
        print ("IO Error: problem opening numbers_list.txt")
    except Exception as err:
             print(err)




main()