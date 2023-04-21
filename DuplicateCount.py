def duplicate_count(text):
    lower_text = text.lower()
    my_set = set(lower_text)
    no_duplicate = 0
    for each_char in my_set:
        if lower_text.count(each_char) > 1:
            no_duplicate +=1
    return no_duplicate