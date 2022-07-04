print(""" 

HESAP MAKİNESİ 

TOPLAMA İŞLEMİ İÇİN 1'e basın.
ÇIKARMA İŞLEMİ İÇİN 2'e basın.
ÇARPMA İŞLEMİ İÇİN  3'e basın. 
BÖLME İŞLEMİ İÇİN 4'e basın.


""")
işlem=str(input("işlem seçiniz:"))

if işlem=="1":
    sayi1=int(input("sayi1 giriniz:"))
    sayi2=int(input("sayi2 giriniz:"))
    print("sonuç:", sayi1 + sayi2 )
elif işlem=="2":
    sayi1=int(input("sayi1 giriniz:"))
    sayi2=int(input("sayi1 giriniz:"))
    print("sonuç:", sayi1-sayi2) 
elif işlem=="3":
    sayi1=int(input("sayi1 giriniz:"))
    sayi2=int(input("sayi2 giriniz:"))
    print("sonuç:", sayi1*sayi2)
elif işlem=="4":
    sayi1=int(input("sayi1 giriniz:"))
    sayi2=int(input("sayi2 giriniz:"))
    print("sonuç:", sayi1/sayi2)
else:
    print(" Geçersiz işlem girdiniz...")
