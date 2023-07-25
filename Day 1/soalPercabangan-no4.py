import math
a = int(input("Masukan variabel X^2: "))
b = int(input("Masukan variabel X: "))
c = int(input("Masukan konstanta: "))
diskriminan = ((b**2) - (4*a*c))
print("Maka akar-akar persamaannya adalah")

if diskriminan > 0:
    # memiliki 2 akar persamaan kuadrat
    rmsPositif = (-b + math.sqrt(diskriminan))/(2*a)
    rmsNegatif = (-b - math.sqrt(diskriminan))/(2*a)
    print(f"X1 = {rmsPositif} V X2 = {rmsNegatif}")
elif diskriminan == 0:
    # memiliki 1 akar persamaan kuadrat
    akar = -b/(2*a)
    print(f"X1 = {akar}")
else:
    print("Tidak memiliki akar persamaan kuadrat")