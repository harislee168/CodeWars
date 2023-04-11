def paint_letterboxes(start, finish):
    # your code
    #create dictionary to store the char_num as key and total painted as value
    letter_box_dictionary = dict()
    #loop from the start to finish
    for temp_num in range(start, finish+1):
        #convert to string
        str_num = str(temp_num)
        #loop each string and add to dictionary
        for character in str_num:
            total_painted = letter_box_dictionary.get(character)
            if total_painted is None:
                letter_box_dictionary.update({character:1})
            else:
                letter_box_dictionary.update({character:total_painted+1})
    return processDictionary(letter_box_dictionary)

def processDictionary(letter_box_dictionary):
    my_list = list()
    for i in range(10):
        if letter_box_dictionary.get(str(i)) is None:
            my_list.append(0)
        else:
            my_list.append(letter_box_dictionary.get(str(i)))
    return my_list