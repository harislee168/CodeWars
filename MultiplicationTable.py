def multiplication_table(size):
    return_list = []
    for index_1 in range(1, size+1):
        sub_list = []
        for index_2 in range(1, size+1):
            sub_list.append(index_1 * index_2)
        return_list.append(sub_list)
    return return_list