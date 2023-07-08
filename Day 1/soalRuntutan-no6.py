gajiPokok = int(input("Masukan gaji pokok anda: "))
tunjangan = gajiPokok * 0.2
pajak = gajiPokok * 0.05
print(f"Tunjangan anda: Rp. {round(tunjangan)}")
print(f"Pajak: Rp. {round(pajak)}")
print(f"Penghasilan bersih + tunjangan: Rp. ", round(gajiPokok + tunjangan - pajak))