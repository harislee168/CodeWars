from collections import Counter
def duplicate_encode(word):
    lower_word = word.lower()
    counter = Counter(lower_word)
    return_string = ''
    for char in lower_word:
        if counter[char] > 1:
            return_string += ')'
        else:
            return_string += '('
    
    return return_string        