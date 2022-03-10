def balckjack(a,b,c):
    # CHECK IF SUM<=21
    sum = a+b+c   # could hav eused build in sum func-- sum([a,b,c])
    if sum <=21:
        return sum
    # CHECK IS SUM >21 AMD 11 IS THERE?
    elif 11 in [a,b,c] and sum -10 <= 21:  # ??????????
        return sum - 10
    else:
        return "bust"
