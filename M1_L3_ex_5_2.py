import random
def drop_coin():
    coin_a = random.randint(1,2)
    if coin_a == 1:
        coin = "Орёл"
    else:
        coin = "Решка"
    print("Выпала сторона:",coin)
