print("ini adalah kalkulator sederhana")

while True:
    a = int (input ("Masukan angka pertama: "))
    b = int (input ("Masukan angka kedua: "))

    print("pilih operasi")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    c = (input ("masukan pilihan (1/2/3/4) : "))

    if c == '1':
        print (a, "+" , b, "=", a+b)
    elif c == '2':
        print (a, "-" , b, "=", a-b)
    elif c == '3':
        print (a, "*" , b, "=", a*b)
    elif c == '4':
        print (a, "/" , b, "=", a/b)
    else :
        print("masukan salah")

    d = (input ("hitung lagi ? (Ketik N untuk berhenti): "))
    if d == 'N':
        break
    else :
        True
    

   