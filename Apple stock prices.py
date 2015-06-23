stock_prices_yesterday = {'60': 500, '120': 501, '250':520, '20': 489}
answer = 0

def isLargest(pal):
    if (pal > answer):
        #print pal
        return pal
    else:
        return answer

for moment in stock_prices_yesterday:
    for i in stock_prices_yesterday:
        if int(moment) < int(i):
            temp = str(stock_prices_yesterday[i] - stock_prices_yesterday[moment])
            answer = isLargest(temp)


print answer
