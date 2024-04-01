import time


bakiye = 0

# Personel Account
def Musteri():
    Tc = "2"
    password = "2"
    if Tc == input("TC'nizi Girin :") and password == input("Sifrenizi Girin :"):
        print("Hos Geldiniz...")
    else:
        print("Bilgiler Yanlis..! Tekrar deneyin")
        quit()

# Show Amount
def bakiyeGoster():
    global bakiye
    print("Bakiyeniz :",bakiye)
    time.sleep(3.0)

# Add Money
def ParaYatir():
    global bakiye
    paraYatir = int(input("Ne kadar Yatirmak istiyorsunuz? :"))
    if paraYatir < 0:
        print("Negatif islem yapamazsiniz.")
        ParaYatir()
    elif paraYatir == 0:
        print("Hatali islem..!")
        ParaYatir()
    else:
        bakiye += paraYatir
        print("Hesabiniza",paraYatir,"TL Yatirildi.. Guncel bakiyeniz :",bakiye)
        time.sleep(3.0)

# withdraw Money
def ParaCek():
    global bakiye
    paraCek = int(input("Ne kadar cekmek istiyorsunuz? :"))
    if paraCek < 0:
        print("Negatif islem yapamazsiniz.")
        ParaCek()
    elif bakiye - paraCek < 0:
        print("Yeterli paraniz yok..!")
        ParaCek()
    elif paraCek == 0:
        print("Hatali islem..!")
        ParaCek()
    else:
        bakiye -= paraCek
        print("Hesabinizdan",paraCek,"TL Cektiniz.. Guncel bakiyeniz :",bakiye)
        time.sleep(3.0)
# Quit
def Cikis():
    quit()

# Mother Program
Musteri()


while True:
    print("""*********************
  ***ANASAYFA***
1. Bakiye Sorgulama
2. Para Yatir
3. Para Cek
4. Cikis
*********************""")
    Secenek = int(input("Ne yapmak istiyorsunuz? :"))
    if Secenek == 1:
        bakiyeGoster()
    elif Secenek == 2:
        ParaYatir()
    if Secenek == 3:
        ParaCek()
    if Secenek == 4:
        Cikis()

