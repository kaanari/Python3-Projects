import sys
import base64
import json

def fonksiyon(c):
    a=89
    x=89
    z=89*2
    b=10
    print("A'nın şuanki değeri : ",x)

    if(c != z):
        sys.exit("89 Yazmak Yok!")

    a=x
    c = int(c/2)
    sonuc = b * c

    if(sonuc==(a)*b):
        a=a*2
        print("Tebrikler. İlk Dersi Tamamladınız.")

def encode_secret():
    a = base64.b64encode(bytes(u'Tahmin ediyorum ki yukarıdaki satırlardan böyle çizimler çıkacağını tahmin edemezdiniz.\nBu örneği Python\'dan ziyade Notebook ile neler yapabileceğinizinde güzel örneklerinden bir tanesi.\nBu metni yukarıdaki kod satırlarında görüyormusunuz? (Bence şifrelenmiş bir metin bulabilirsiniz)', "utf-8"))
    return a

def decode_secret(a):
    b = base64.b64decode(a).decode("utf-8", "ignore")
    return b

def print_ex1(x1,y1,string1,float1):
    print("X değişkeninin değeri = ",x1,"   Tipi = ",str(type(x1)).split("'")[1])
    print("Y değişkeninin değeri = ",y1,"   Tipi = ",str(type(y1)).split("'")[1])
    print("String değişkeninin değeri = ",string1,"   Tipi = ",str(type(string1)).split("'")[1])
    print("Ondalik_sayim değişkeninin değeri = ",float1,"   Tipi = ",str(type(float1)).split("'")[1],"\n")
    
def get_value_ex04():
    return 1024

def key_ex04():
    
    sayi = get_value_ex04() # Bu satırda hata yok :)

    # Bu satırdan aşağısı düzenlenecek.

    sayi = sayi**(1/2)

    sayi = sayi*2

    sayi = sayi + ((5 + sayi)*12-2)/5

    sayi_gecici = sayi % 5

    sayi_gecici = sayi - sayi_gecici

    sonuc = sayi
    
    return sonuc

def control_password_ex05(password):
    if(password == "22425768" and type(password) == str):
        print("Congratulations. You cracked the NASA.")
    else:
        print("ERROR!")
        
def get_password_ex05():
    return "5032.425"
    
    
    
def get_crack_key_ex05():
    return "3"

def example_ex06():
    info = "Bill Gates 02 10 1955"

    info = info.split(" ")
    isim = info[0].upper()
    soyisim = info[1].upper()
    gun = info[2]
    ay = info[3]
    yil = info[4]

    yas = 2019-int(yil)
    tarih = "Doğum Tarihi: " + gun + "/" +  ay + "/"  + yil

    print(isim + " " +soyisim + " - " + tarih + " - " + "Yaş: " + str(yas))
    print("Mantıksal Sonuç: "+str((int(yil)<2002 and int(ay)<6) or (int(gun)>=15)))
    

def ucgen2_cizim(inp):
    for row in range(inp): # Input kadar satır yazdırmak için bu for'u kullandık.
        numbers = 1 # Üçgeni 1'den başlaktık.
        for a in range(row+1): # İşlem yaptığı satırda kaç sayı yazdıracağımızı bu for ile belirledik.
            print(numbers,end="") # Sayılarımızı yazdırdık.
            print(" ",end="") # Aynı satırdaki sayılar arasında boşluk bıraktık.
            numbers+=1
                
        print("") #Alt satıra geçmek için kullandık.
        
def hasta_arama(names):
    name = (input("Hasta İsmi: ").lower()).capitalize()
    checkPatient = name in names # names listesinde name değişkeninin olup olmadığını kontrol edip boolean sonuç döndürür.
    
    if checkPatient:
        index = names.index(name)
        print("Hasta hastanemizde kayıtlıdır.")
    else:
        index = -1
        print("Hasta hastanemizde kayıtlı değildir.")
    
    return checkPatient,index

def json_ex03():
    x = '{"success":true,"message":"","result":[{"MarketName":"USD-BTC","High":8303.99000000,"Low":8004.37900000,"Volume":349.36606161,"Last":8249.53500000,"BaseVolume":2867881.16868972,"TimeStamp":"2019-10-21T15:16:35.037","Bid":8245.00000000,"Ask":8246.13800000,"OpenBuyOrders":2129,"OpenSellOrders":3391,"PrevDay":8004.38300000,"Created":"2018-05-31T13:24:40.77"}]}'
    y = json.loads(x)
    return y