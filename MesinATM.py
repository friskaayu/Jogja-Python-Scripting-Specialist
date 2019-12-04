'''
-   Pada sebuah bank, nasabah yang membuka rekening harus menyetor minimal 100000 terlebih dahulu. 
-   Buatlah program sederhana untuk mesin ATM dengan kelas Nasabah dan Rekening. 
-   Fungsi/method yang harus ada adalah fungsi ambil uang, setor, dan transfer. 
-   Kemudian buatlah nasabah bernama Aldo dan Aldi. 
    Simulasikan kejadian Aldo melakukan pengambilan uang sebanyak 150000. Aldi mentransfer 
    uang sejumlah 50000 ke rekening Aldo. 
-   Lalu cetak data kedua nasabah! (catatan: ketika terjadi suatu kegiatan di ATM (setor, tarik, transfer) 
    akan ada output berupa keterangan kejadian. 
    Contoh “Transfer sebesar xxxxx ke rekening xxxxx”. 
    Format keterangan yang dicetak bebas.

'''
import sys

Nasabah1 = {"nama":"Aldo",
            "password":"12345",
            "rekening":"01020304",
            'saldo':4500000}
Nasabah2 = {"nama":"Aldi",
            "password":"54321",
            "rekening":"09080706",
            "saldo":7800000}
username = Nasabah1["nama"] or Nasabah2["nama"]
password = Nasabah1["password"] or Nasabah2["password"]
class nasabah():
    def __init__(self, nama, psw):
        self.nama = nama
        self.psw = password
       
    def login(self, nama = username, psw= password):
        self.nama = username
        self.psw = password
       
class rekening(nasabah):
    def __init__(self, nama, psw):
        self.nama = nama
        self.psw = password

    def tarik(self):
        nominal = int(input("Jumlah Tarik Tunai : "))
        saldo1 = Nasabah1["saldo"]
        saldo2 = Nasabah2["saldo"]
        if saldo1 < nominal and saldo2 < nominal:
            print("Transaksi Gagal!")
        else:
            print(" {}, Transaksi Anda Berhasil ".format(self.nama))
            print("Anda Melakukan Tarik Tunai Senilai {} ".format(nominal))
        return nominal

    def setor(self):
        nominal = int(input("Jumlah Setor Tunai : "))
        saldo1 = Nasabah1["saldo"]
        saldo2 = Nasabah2["saldo"]
        print(" {}, Transaksi Anda Berhasil ".format(self.nama))
        print("Anda Melakukan Setor Tunai Senilai {} ".format(nominal))
        return nominal

    def transfer(self):
        norek = input(" Masukan Nomer Rekening Tujuan : ")
        if norek == Nasabah1['rekening'] or norek == Nasabah2['rekening']:
            nominal = int(input("Masukan Jumlah Transfer : "))
            if Nasabah1["saldo"] < nominal and Nasabah2["saldo"] <  - nominal:
                print("Saldo Anda Tidak Mencukupi")
            else:
                print(" {}, Transaksi Anda Berhasil ".format(self.nama))
                print("Anda Melakukan Transfer Senilai {} ".format(nominal))
                print("Nomer Rekening Tujuan : {}".format(norek))
                return nominal, norek
            return norek
        else:
            print("Data Tidak Ditemukan")
            return norek

    def menu(self):
        print("---------- SIlahkan Pilih Transaksi Anda  ----------")
        print(" Ketik 1 untuk Tarik Tunai")
        print(" Ketik 2 untuk Setor Tunai")
        print(" Ketik 3 untuk Transfer ")
        menu = int(input("Masukan Pilihan (1/2/3) : "))
        return menu



print("---------- SIMULASI MESIN ATM ----------")
print(" Selamat datang di BankAnda ")
print(" Ketik 1 untuk  membuka Rekening Baru")
print(" Ketik 2 untuk Login")
while True:
    a = (input("Masukan pilihan anda (1/2): "))
# buka rekening baru
    if a =='1':
        while True:
            nama = (input ("Masukan nama user: "))
            password = int (input ("Masukan password (hanya angka): "))
            saldo = int (input ("Masukan setoran awal (hanya angka): "))
            if saldo >= 100000 :
                print ("Terimakasih {} ,Anda telah terdaftar sebagai nasabah baru.".format(nama))
                print ("{} telah ditambahkan dalam saldo anda".format(saldo))
                b = (input("Kembali ke menu awal ? (Y/N): "))
                if b =='Y':
                    break
                if b =='N':
                   sys.exit()
            else:    
                print ("Setoran Awal kurang dari 100000 , mohon ulangi pengisian data ")
# Login   
    elif a =='2': 
        while True:
            username = input("nama user anda : ")
            password = input("Password : ")
            c = rekening(username,password)
            c.login()
            if username == Nasabah1['nama'] and password == Nasabah1['password']:
                d = c.menu()
                if d == 1:
                    nom = c.tarik()
                    if Nasabah1["saldo"] < nom:
                        print("Saldo Anda Tidak Mencukupi")
                        sys.exit()
                    else:
                        total = Nasabah1['saldo'] - nom
                        print("Sisa Saldo Anda : {}".format(total))
                        sys.exit()
                elif d == 2:
                    nom = c.setor()
                    total = Nasabah1["saldo"] + nom
                    print("Saldo Anda Saat ini : {} ".format(total))
                    sys.exit()

                elif d == 3:
                    trans = c.transfer()
                    if trans[1] == Nasabah1['rekening']:
                        if Nasabah1['saldo'] < trans[0] and Nasabah2['saldo']  < trans[0]:
                            print()
                            sys.exit()
                        else:
                            print("Sisa Saldo Anda : ",Nasabah1['Saldo']-trans[0])
                            sys.exit()
                    else:
                        print()
                        sys.exit()
                       

            elif username == Nasabah2['nama'] and password == Nasabah2['password']:
                e = c.menu()
                if e == 1:
                    nom = c.tarik()
                    if Nasabah2["saldo"] < nom:
                        print("Saldo Anda Tidak Mencukupi")
                        sys.exit()
                    else:
                        total = Nasabah2['saldo'] - nom
                        print("Sisa Saldo Anda : {}".format(total))
                        sys.exit()

                elif e == 2:
                    nom = c.setor()
                    total = Nasabah2["saldo"] + nom
                    print("Saldo Anda Saat ini : {} ".format(total))
                    sys.exit()

                elif e == 3:
                    trans = c.transfer()
                    if trans[1] == Nasabah2['rekening'] :
                        if Nasabah1['saldo'] < trans[0] and Nasabah2['saldo']  < trans[0]:
                            print()
                            sys.exit()
                        else:
                            print("Sisa Saldo Anda : ",Nasabah2['Saldo']-trans[0])
                            sys.exit()
                    else:
                        print()
                        sys.exit()
                        
    else:
        print ("Masukan salah, mohon ulangi")



