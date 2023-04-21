from collections import Counter
def grabscrab(said, possible_words):
    #create list to store the words of match result
    word_list = []
    #use counter to store each char and the no of occurence to match the list
    said_counter = Counter(said)
    for word in possible_words:
        #store the word into the counter as well to check against said_counter
        word_counter = Counter(word)        
        if said_counter == word_counter:
            word_list.append(word)
    
    return word_list