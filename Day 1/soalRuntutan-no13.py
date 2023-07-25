# ali, budi, susi membuka usaha bersama dengan pembagian keuntungan masing-masing 20%, 30%, dan 50%.
# buatlah algoritma menghitung keuntungan setiap orang (uali, ubudi, ususi) jika diketahui masukan omset penjualan (omset) dan total pengeluaran (luar) perusahaan?
totPengeluaran = int(input("total pengeluaran perusahaan: "))
omset = int( input ("Omset perusahaan: "))
omsetBersih = omset - totPengeluaran
uali = 0.2 * omsetBersih
ubudi = 0.3 * omsetBersih
ususi = 0.5 * omsetBersih
print(f"Uang Ali: Rp. {round(uali)}")
print(f"Uang Budi: Rp. {round(ubudi)}")
print(f"Uang Susi: Rp. {round(ususi)}")