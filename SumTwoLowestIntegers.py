def sum_two_smallest_numbers(numbers):
    list_two = [0] * 2
    for number in numbers:
        #If first index is 0 then assign number
        if list_two[0] == 0:
            list_two[0] = number
            #print('list_two[0]:', list_two[0])
            continue
        #if first index is already has a number and second index is still 0 then assign a number
        if list_two[1] == 0:
            list_two[1] = number
            #print('list_two[1]:', list_two[1])
            continue
        
        #check if first index is greater than number then process
        if list_two[0] > number:
            #check second index is greater first index, if yes need to replace the second index value to first index value
            #before reassign the new number to the first index to make sure that the second index is also updated as the second lowet value
            if list_two[1] > list_two[0]:
                list_two[1] = list_two[0]
            list_two[0] = number
        #if first index is less than the number then just check second index
        else:
            if list_two[1] > number:
                list_two[1] = number
    return sum(list_two)