def open_or_senior(data):
    return_list = []
    for list_data in data:
        age, handicap = list_data[0], list_data[1]
        if age >= 55 and handicap > 7:
            return_list.append('Senior')
        else:
            return_list.append('Open')
    return return_list