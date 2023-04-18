def longest(a1, a2):
    # create a set to store a1 + a2. Use set to make sure no duplicate
    char_set = set()
    #loop each char in aq and a2 and store it into a set
    for char_a1 in a1:
        char_set.add(char_a1)
    for char_a2 in a2:
        char_set.add(char_a2)
    
    #convert the set into the list so that we can sort it
    char_list  = list(char_set)
    char_list.sort()
    
    return ''.join(char_list)