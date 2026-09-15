# Program Penghitung Total Hasil Panen

def hitung_total_hasil(panen):
    return sum(panen)


def hitung_diskon(total, persentase_diskon):
    diskon = total * persentase_diskon / 100
    return total - diskon


# Data hasil panen dalam kilogram
data_panen = [100, 150, 200, 175]

total = hitung_total_hasil(data_panen)
total_setelah_diskon = hitung_diskon(total, 10)

print("Data hasil panen:", data_panen)
print("Total hasil panen:", total, "kg")
print("Total setelah diskon 10%:", total_setelah_diskon, "kg")