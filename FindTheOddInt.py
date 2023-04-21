from collections import Counter
def find_it(seq):
    my_counter = Counter(seq)
    my_set = set(seq)
    
    for num in my_set:
        if my_counter[num] % 2 == 1:
            return num