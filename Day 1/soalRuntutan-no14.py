hNorm = int(input ("Harga Normal: "))
hKredit = hNorm+(0.2*hNorm)
uMuka = 0.3 * hKredit
uCicil = (hKredit - uMuka)/12
print(f"Jadi komputer dijual secara kredit dengan \nHarga kredit: {hKredit}\nUang muka: {uMuka}\nCicilan: {uCicil} perbulan")
print("Cicilan dibayar 12x selama 1 tahun")