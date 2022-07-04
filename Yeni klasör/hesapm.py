print("""

HESAP MAKİNESİ

TOPLAMA İŞLEMİ  İÇİN 1 'e BASIN.
ÇIKARMA İŞLEMİ  İÇİN 2 'e BASIN.
ÇARPMA İŞLEMİ   İÇİN 3 'e BASIN.
BÖLME İŞLEMİ    İÇİN 4 'e BASIN.

""")

işlem = str(input("İşlem seçiniz: "))

if işlem == "1":
    sayi1 = int(input("sayi1 giriniz: "))
    sayi2 = int(input("sayi2 giriniz: "))
    print("Sonuç:", sayi1 + sayi2)
elif işlem == "2":
    sayi1 = int(input("sayi1 giriniz: "))
    sayi2 = int(input("sayi2 giriniz: "))
    print("Sonuç:", sayi1 - sayi2)
elif işlem == "3":
    sayi1 = int(input("sayi1 giriniz: "))
    sayi2 = int(input("sayi2 giriniz: "))
    print("Sonuç:", sayi1 * sayi2)
elif işlem == "4":
    sayi1 = int(input("sayi1 giriniz: "))
    sayi2 = int(input("sayi2 giriniz: "))
    print("Sonuç:", sayi1/sayi2)
else:
    print("geçersiz işlem girdiniz...")