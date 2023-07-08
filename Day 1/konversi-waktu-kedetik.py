# konversi ke detik
jam = int(input("Masukan jumlah jam: "))
konversJamDetik = jam * 60 * 60
menit = int(input("Masukan jumlah menit: "))
konversMenitDetik = menit * 60
print(f"Jam: {konversJamDetik}\nMenit: {konversMenitDetik}")
print(f"Total: {konversJamDetik+konversMenitDetik}")

# konversi Ke jam
detik = int(input("Masukan jumlah detik: "))
konversDetikJam = (detik/60)/60
menit = int(input("Masukan jumlah menit: "))
konversMenitDetik = 60/menit
print(f"Jam: {konversJamDetik}\nMenit: {konversMenitDetik}")
print(f"Total: {konversJamDetik+konversMenitDetik}")