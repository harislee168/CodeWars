def top_3_words(text):
    punctuation='~!@#$%^&*()_+`-={}|[]\:";<>?,./"'
    text = text.lower()
    text = [t if t not in punctuation else ' ' for t in text]
    text = ''.join([t for t in text])
    split_text = text.split()
    store_dict = {}
    for split_t in split_text:
        counter = store_dict.get(split_t)
        if counter is None:
            store_dict.update({split_t:1})
        else:
            store_dict.update({split_t:counter+1})
    
    return_list = []
    for i in range(3):
        if (len(store_dict) != 0):
            max_values = max(store_dict.values())
            for key, value in store_dict.items():
                if value == max_values and \
                    not (key.startswith('\'') and key.endswith('\'')):
                    return_list.append(key)
                    store_dict.pop(key)
                    break
    return return_list