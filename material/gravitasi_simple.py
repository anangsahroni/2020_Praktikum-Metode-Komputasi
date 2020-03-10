# Program Penghitungan Nilai Gaya Gravitasi
# Step 1 : Memasukkan nilai parameter perhitungan

m1 = float(input("Masukkan nilai massa 1 (m1) dalam kg: "))
m2 = float(input("Masukkan nilai massa 2 (m2) dalam kg: "))
r = float(input("Masukkan nilai jarak  (r) dalam meter: "))
G = 6.674e-11

# Step 2 : Menghitung nilai gaya gravitasi (F = G x m1 x m2 / (r^2))
F = (G*m1*m2) / (r**2)

# Step 3:  Mencetak hasil perhitungan
print("Nilai gaya gravitasi adalah: ", F, "Newton")