def split_the_bill(x):
    # Code Away!
    average = sum(x.values())/len(x)
        
    for key in x.keys():
        x[key] = round(x[key] - average, 2)
    return x