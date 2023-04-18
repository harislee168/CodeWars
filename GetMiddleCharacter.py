def get_middle(s):
    #first get the length
    str_len = len(s)
    
    #get the middle index as a base to retrieve the mid character(s)
    mid_index = str_len//2
    
    #check if is even
    even_or_odd = str_len % 2
    if even_or_odd == 0:
        return s[mid_index - 1: mid_index + 1]
    else:
        return s[mid_index]