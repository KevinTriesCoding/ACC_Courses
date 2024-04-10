def main ():

    list1 = [1, 2, 3, 4, 5]
    list2 = [11, 13, 17, 19, 23]
    merged_list = list1 + list2
    max_value = max(merged_list)
    min_value = min(merged_list)


    print(merged_list)
    print (total_list(merged_list))
    print (f"Highest value: {max_value}")
    print (f"Lowest value: {min_value}")


def total_list(x):
    listA = x
    sum = 0
    
    for num in listA:
        sum += num
    return sum

main()