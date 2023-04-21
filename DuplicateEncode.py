def duplicate_encode(word):
    lower_word = word.lower()
    return_string = ''
    for char in lower_word:
        if lower_word.count(char) > 1:
            return_string += ')'
        else:
            return_string += '('
    return return_string