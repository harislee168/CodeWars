def spacey(array):
    len_array = len(array)
    return_list = []

    for index in range(len_array):
        return_word = ''.join(array[:index+1])
        return_list.append(return_word)
    return return_list