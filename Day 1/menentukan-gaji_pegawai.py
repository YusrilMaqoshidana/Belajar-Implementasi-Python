masaKerja = int(input("Masa Kerja: "));
print ("1. Senior")
print ("2. Junior")
senior = 15000000
junior = 5000000
jabatan = int(input ("Jabatan Anda: "))
if masaKerja >= 3:
    match (jabatan):
        case 1:
            senior = senior + (0.2*senior)
            print(f"Gaji + Tunjangan: {senior}")
        case 2:
            junior = junior + (0.2*junior)
            print(f"Gaji + Tunjangan: {junior}")


elif masaKerja > 0 and masaKerja < 3:
       match (jabatan):
        case 1:
            senior = senior + (0.1*senior)
            print(f"Gaji + Tunjangan: {senior}")

        case 2:
            junior = junior + (0.1*junior)
            print(f"Gaji + Tunjangan: {junior}")


