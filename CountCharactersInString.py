def count(s):
    my_dict  = {}
    for char in s:
        total_char = my_dict.get(char)
        if total_char is None:
            total_char = 0
        
        total_char += 1
        my_dict.update({char:total_char})
    return my_dict