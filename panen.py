# Program Penghitung Total Hasil Panen

def hitung_total_hasil(panen):
    return sum(panen)


# Data hasil panen dalam kilogram
data_panen = [100, 150, 200, 175]

total = hitung_total_hasil(data_panen)

print("Data hasil panen:", data_panen)
print("Total hasil panen:", total, "kg")