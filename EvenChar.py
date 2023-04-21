def even_chars(st): 
    st_len = len(st)
    if st_len < 2 or st_len > 100:
        return 'invalid string'
    else:
        char_list = []
        for each_char in st[1::2]:
            char_list.append(each_char) 
    return char_list