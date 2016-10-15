

import math
n= int(raw_input())
coins = list()

for i in range(n):
    coins.append(int(raw_input()))



def arrangeCoins(Coins):
    for i in Coins:
        k = int((-1+math.sqrt(1+8*i))/2)
        print k

arrangeCoins(coins)