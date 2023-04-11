def is_flush(cards):
    # Write your code in here
    flushList = list()
    for card in cards:
        flushList.append(card[-1])
    return len(set(flushList)) == 1