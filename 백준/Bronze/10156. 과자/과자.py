price, num, money = map(int,input().split())
pay = price*num
if pay > money:
    print(pay-money)
if pay <= money:
    print(0)