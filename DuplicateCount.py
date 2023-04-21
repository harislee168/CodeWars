def duplicate_count(text):
    my_dict = dict()
    total_duplicate = 0
    for each_char in text.lower():
        char_count = my_dict.get(each_char)
        if char_count is None:
            char_count = 0
        char_count+=1
        my_dict.update({each_char:char_count})
    
    for value in my_dict.values():
        if value > 1:
            total_duplicate += 1
            
    return total_duplicate