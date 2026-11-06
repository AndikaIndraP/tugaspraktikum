# Andika Indra Praja
# 2611229
# 1A

nilai = int(input("Masukkan nilai n: "))

def fibonacci(nilai):
    if nilai <= 1:
        return nilai
    else:
        return fibonacci(nilai-1) + fibonacci(nilai-2)

for i in range(nilai):
    print(f"Nilai Fibonacci[{i}] = {fibonacci(i)}")
    print("Halo, saya Andika Indra Praja dengan NIM 2611229 dari kelas 1A")