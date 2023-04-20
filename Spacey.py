def spacey(array):
    len_array = len(array)
    return_list = []
    
    for index in range(len_array):
        return_word = ''
        for second_index in range(index+1):
            return_word += array[second_index]
        return_list.append(return_word)
    return return_list
    