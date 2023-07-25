lamaSewa = int(input("Lama Sewa: "))
total = 0

for waktu in range(1, lamaSewa+1):
    if waktu > 3:
        total += 4000
    elif waktu <= 3:
        total += 5000
print(total)