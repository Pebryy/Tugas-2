# Greedy Coin Change

coins = [1000, 500, 200, 100]
jumlah = 2700

for coin in coins:
    count = jumlah // coin
    jumlah = jumlah % coin

    if count > 0:
        print(coin, ":", count)