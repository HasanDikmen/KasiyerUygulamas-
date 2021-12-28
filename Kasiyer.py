#Bu projede sözlük,liste,while döngüsü,break ifadesi,if-else-elif koşul blokları,çeşitli operatörler,print ve input fonksiyonu farklı türde değişkenler kullanılmıştır.
#Hocam burada hayali bir ürün listesi oluşturup market uygulamamı o listeyi baz alarak çalıştıracağım (8.satır).
#Döngüden etkilenmemesi için döngünün dışına ürün sepetimi liste şeklinde oluşturdum (9.satır).
#Temel seviye yazmak yerine biraz daha kullanıcı dostu olması için kodlarımda string ifadelere sıklıkla yer vererek kullanıcıyı bilgilendirdim.
#Barkod kısmını uygulamanın gerçeğe yakın olması için ekledim tabiki bizim barkod girdimiz olmadığı için işlemleri ürün kodları üzerinden yürüteceğiz.
#Kullanan kasiyer ürün kodu bilgileri ekranı ile ürünlerin kodlarını görebilir ürün kodu giriş ekranı ile kodunu girdiği ürünleri sepete ekleyebilir.
#Sepet sorgulama işlemleri menüsü ile sepete eklediği ürünleri görebilir sepeti boşaltabilir.
ürünler={"3214":"Süt","2314":"Ekmek","6341":"Elma","7413":"Et","3061":"Peynir","1732":"Yumurta","1690":"Su","6433":"Kuruyemiş","2603":"Sigara","1010":"Alkol"}
sepet=[]
print("**********************************")
print("HD KASA SİSTEMİ ARAYÜZÜNE HOŞGELDİNİZ")
print("**********************************")
while True:
    print("\nİşlemler:\n1-Barkod okutma işlemleri\n2-Ürün kodu girişi\n3-Sepet Sorgulama işlemleri\n4-Ürün kodu bilgileri\n5-Çıkış")
    işlem = int(input("\n-Lütfen Yapmak İstediğiniz işleme ait rakamı giriniz:"))
    if (işlem==1):#Buranın işi bitti
        while True:
            print("+Barkod işlemleri seçildi\nBurası henüz kullanıma açık değildir...")
            aramen4=input("Ana menüye dönmek için x tuşuna basınız:")
            if(aramen4=="x"):
                break
    elif(işlem==2):#Buranın işi bitti ama geliştirilebilir
        print("+Ürün Kodu işlemleri seçildi")
        while True:
            Barkod=input("Ürünün barkod numaranısı tuşlayınız:")
            sepet.append(ürünler[Barkod])
            aramen2 = input("Çıkmak için x devam etmek için y tuşuna basınız")
            if (aramen2=="x"):
                break
    elif(işlem==3):
        print("+Sepet Sorgulama işlemleri seçildi")
        while True:
            aramen3 = int(input("*Sepetinizdeki ürünleri görmek için 1'e basınız\n*Sepetinizi boşaltmak için 2'ye basınız\n*Ana menüye dönmek için 3'e basınız\n:"))
            if (aramen3==1):
                print("Sepetinizdeki ürünler:")
                print(sepet)
            elif(aramen3==2):
                sepet.clear()
            elif(aramen3==3):
                break
    elif(işlem==4):#Buranın işi bitti
        print("+Ürün kodu bilgileri seçildi")
        while True:
            print("Ürünler-Kodları\n(Süt-3214)\n(Ekmek-2314)\n(Elma-6341)\n(Et-7413)\n(Peynir-3061)\n(Yumurta-1732)\n(Su-1690)\n(Kuruyemiş-6433)\n(Sigara-2603)\n(Alkol-1010)")
            aramen1 = input("Ana menüye dönmek için x tuşuna basınız:")
            if (aramen1=="x"):
                break
    elif(işlem==5):#Buranın işi bitti
        break
print("Çıkış yapılıyor...")
