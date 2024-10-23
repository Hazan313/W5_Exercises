Asset1 = 500
Asset2 = 1000
Asset3 = 50000

Debt1 = 100
Debt2 = 3000
Debt3 = 20000

networth = ((Asset1 + Asset2 + Asset3) - (Debt1 + Debt2 + Debt3))
networth = round(networth, 2)
print('Your networth is $' + str(networth))
