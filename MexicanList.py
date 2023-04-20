def wave(people):
    len_people = len(people)
    mexican_list = []
    for index in range(len_people):
        left = people[:index]
        char_upper = people[index]
        right = people[index+1:]
        
        #if space then skip
        if char_upper == ' ':
            continue
        else:
            word = left + char_upper.upper() + right
            mexican_list.append(word)
    return mexican_list
    
    
        