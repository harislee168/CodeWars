def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    #to store array1 ** 2
    array3 = [num*num for num in array1]       
    array2.sort()
    array3.sort()
    return array2 == array3