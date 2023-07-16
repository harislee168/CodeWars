def buy_tofu(cost, box):
    split_box = box.split()
    dict_box = {}
    for split_b in split_box:
        counter = dict_box.get(split_b)
        if counter is None:
            dict_box.update({split_b:1})
        else:
            dict_box.update({split_b:counter+1})
    
    total = 0
    exact_coin = 0 
    
    total_monme = dict_box.get('monme')
    if total_monme is not None:
        total = total + (total_monme * 60)
        for monme in range(total_monme):
            if cost > 60:
                cost = cost - 60
                exact_coin = exact_coin + 1
            else:
                break
    
    total_mon = dict_box.get('mon')
    if total_mon is not None:
        total = total + total_mon
        for mon in range(total_mon):
            if cost != 0:
                cost = cost - 1
                exact_coin = exact_coin + 1
            
    if cost != 0:
        exact_coin = 0
    
    if total < cost:
        return 'leaving the market'
    else:
        if exact_coin:
            return [total_mon, total_monme, total, exact_coin]
        else:
            return 'leaving the market'
        