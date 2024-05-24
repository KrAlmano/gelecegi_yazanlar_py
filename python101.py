
#String metotları  len() -> Karakter dizisinin uzunluğunu gösterir
a="Almano  ahmet"
len(a)
b=9
b*10

c=19
print(c)
#String metotları upper() - lower()  -> büyük küçük harf

gel_yaz ="gelecegi_yazanlar"

gel_yaz.upper()
gel_yaz.lower()

gel_yaz.isupper()
gel_yaz.islower()

B=gel_yaz.upper()
B.isupper()


#String metotları  replace()

gel_yaz.replace("a","e")


#String metotları  strip()
#Boşluklardan kurtulmak için kullanılır

Den="   Ahmet     "
Den.strip()
Cen = "*Almano*"
Cen.strip("*")

#Metodlara Genel Bakış
#dir() Uygulunabilecek olan tüm metotları gösterir
dir(gel_yaz)

#Substring (Alt dizi)
#0. elemanı bulmak için -> çıktı "g" olacak
gel_yaz[0]
#ilk 4 elemanı bulmak için  -> çıktı "gele" olacak
gel_yaz[2:4]

#Tip Dönüşümleri
toplam_bir=input("Please enter a value")
toplam_iki=input("Please enter a value")

type(toplam_bir)

int(toplam_bir)+int(toplam_iki)

#virgülden sonraki kısmı siler tam sayı yapar
int(1023.2)

print("Gelecegi yazanlar")
print("Gelecegi", "Yazanlar",sep='_')

a = "bu uzun bir metindir"
a[2:5]
