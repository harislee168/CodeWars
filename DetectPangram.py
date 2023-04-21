import re
def is_pangram(s):
    my_list  = re.findall('[a-z]', s.lower())   
    my_set = set(my_list)
    return len(my_set) == 26