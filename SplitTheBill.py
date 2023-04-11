def split_the_bill(x):
    # Code Away!
    average = sum(x.values())/len(x)
        
    for key in x.keys():
        x[key] = x[key] - average
    return x