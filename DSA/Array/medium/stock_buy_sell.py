l=[5,1,4,7,3]

# def stock_buy_sell(l):
#     for i in range(len(l)):
#         min=l[i]
#         for j in range (i+1,len(l)):
#             if l[j]<min:
#                 min=l[j]
#                 ll=l[j:]

#     for i in range(len(ll)):
#         max=l[i]
#         if l[i]>max:
#             max=l[i]
#             print(max)
    
#     profit=max-min
#     return profit

# print(stock_buy_sell(l))



def stock_sell_buy(l):
    maxp=0
    for i in range(len(l)):
        for j in range(i,len(l)):
            p=l[j]-l[i]
            if p>maxp:
                maxp=p

    return maxp

print(stock_sell_buy(l))