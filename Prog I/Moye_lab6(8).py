def main():
        try:
        
            file = open("random_num.txt", "r")

            total = 0
            count = 0

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
            average = (total / count)
            print(f"Sum of random numbers: {total}")
            print(f"Total random numbers generated: {count}")
            print(f"Average of the random numbers: {average}")
        except IOError:
             print ("IO Error: problem opening random_num.txt")
        except Exception as err:
             print(err)
             

main()
