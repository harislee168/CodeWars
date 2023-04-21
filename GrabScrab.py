def grabscrab(said, possible_words):
    format_said = sorted(said.lower())
    return_list = []
    for word in possible_words:
        format_word = sorted(word.lower())
        if format_said == format_word:
            return_list.append(word)
    return return_list