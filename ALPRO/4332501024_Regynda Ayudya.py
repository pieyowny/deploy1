import string

def enkripsi(teks, kunci):
    a = string.ascii_lowercase 
    R = string.ascii_uppercase
    hasil = ""
    for kalimat in teks:
        if kalimat in a:
            hasil += a[(a.index(kalimat) + kunci) % 26]
        elif kalimat in R:
            hasil += R[(R.index(kalimat) + kunci) % 26]
        else:
            hasil += kalimat
    return hasil

def dekripsi(teks, kunci):
    return enkripsi(teks, -kunci)


teks = input("Masukkan teks: ")
kunci = int(input("Masukkan kunci: "))


hasil_enkripsi = enkripsi(teks, kunci)
hasil_dekripsi = dekripsi(hasil_enkripsi, kunci)

print("\nHasil Enkripsi :", hasil_enkripsi)
print("Hasil Dekripsi :", hasil_dekripsi)