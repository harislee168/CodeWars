import re
def make_password(phrase):
    split_phrase = phrase.split()
    word = ''
    for small_phrase in split_phrase:
        word += small_phrase[0]

    #replace i, 0, s
    word = re.sub('i|I', '1', word)
    word = re.sub('o|O', '0', word)
    word = re.sub('s|S', '5', word)
    return word