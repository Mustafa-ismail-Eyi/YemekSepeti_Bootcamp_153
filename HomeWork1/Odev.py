# %%
"""
Bir metnin uzunluğunu hesaplamak için bir Python programı yazınız. ipucu Len fonksiyonu
"""

user_input = input("Bir cümle yazın")
print(f"yazdığınız kelime de şu kadar karakter var: {len(user_input)}")

# %%

"""Kullanıcı tarafından girilen bir metnin ilk iki ve son iki karakterini ekrana yazdıran Python programını yazınız."""
user_input = input("Bir cümle yazın")
print(user_input[:2],user_input[-2:])
# %%
"""Kullanıcıdan değişecek metin ve eski harf ve yeni harf bilgisini alarak 
girilen metin üzerinden değişikliği yapıp sonucu ekrana yazdıran Python programını yazınız."""

user_input = input("bir cümle yazın")
source = input("değiştirmek istediğiniz karakteri giriniz")
dest = input("yeni karakteri giriniz")

print(user_input.replace(source,dest))
# %%
"""Kullanıcı tarafından girilen bir kelimenin palindrom 
olup olmadığını karşılaştırma operatöründen faydalanarak print() fonksiyonu ile ekrana yazdırınız. """

palindrom = input("palindrom bir cümle giriniz")
if palindrom[::] == palindrom[::-1]:
    print("Palindrom")
else:
    print("palindrom değil") 

# %%
"""Girilen bir metnin son 2 karakterini 4 defa çoğaltarak 
ekrana yazan Python programını yazınız. `*` aritmetik operatöründen faydalanabilirsiniz. """

user_input = input("metin girin")
print(user_input[-2:]*4)
# %%
"""5 elemanlı bir liste oluşturunuz. Bu liste içerisindeki 2. elemanı 100 ile değiştiren python kodu yazınız."""
import random
liste = [random.choice(range(100)) for i in range(5)]
liste[1] = 100
print(liste)

# %%
liste1 = [1,2,3]
liste2 = [4,5,6]
liste3 = liste1 + liste2
liste1.extend(liste2)
print(liste1)
# %%
"""Oluşturduğunuz 3 elemanlı bir liste içerisine ilk sıraya "Elma" kelimesini ekleyiniz. """
liste2 = [4,5,6]
liste2.insert(0,'Elma')
print(liste2)
# %%
"""
yukarıdaki listeden ilk 3 sayısını silip ekrana yazdırınız. 
"""
liste = [1,2,3,4,5,6,7,1,3,3,3,2,2,1,23]
liste.remove(3)
print(liste)
# %%

"""
liste1 = ["1",1,2,"3"]
Yukarıdaki listenin bir kopyasını alarak 250 sayısını listenin sonuna ekleyiniz,her iki listeyi ekrana yazdırınız.
Beklenen Çıktı:
["1",1,2,"3"] => Liste1 Çıktısı
["1",1,2,"3",250] => Liste2 Çıktısı
"""
liste1 = ["1",1,2,"3"]
liste1.append(250)
print(liste1)
# %%
"""

Aşağıdaki üç farklı sözlüğü tek sözlükte birleştiren python kodunu yazınız
dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50,6:60}
Beklenen Çıktı : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""
dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50,6:60}

dict1.update(dict2)
dict1.update(dict3)
print(dict1)
# %%
"""sozluk ={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
Sözlükteki en son elemanı silerek ekrana işlem sonucunu yazdırınız
Beklenen Çıktı :(6,60)"""
sozluk ={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(sozluk.popitem())
# %%
"""dict1={1:10, 2:20}
Yukarıdaki sözlüğe bir eleman ekleyiniz. 
Beklenen Çıktı :{1:10, 2:20, 3:30}
"""
dict1={1:10, 2:20}
dict1.update([(3,30)])
dict1.update({4:40})
print(dict1)
# %%
liste=[1,2,3,4,5]
dict1 = {i:i*10 for i in liste}
print(dict1)
# %%

"""sozluk={1:10,2:20,3:30,4:40,5:50}
Sözlük içerisine 6 sayısını anahtar olarak değeri 60 olacak şekilde setdefault fonksiyonunu kullanarak ekleyiniz
"""

sozluk.setdefault(6,60)
print(sozluk)
# %%
"""
Seven Segment Display 
https://en.wikipedia.org/wiki/Seven-segment_display"""


# %%
"""
Bir listeyi bir sözlükte sıralamak için bir Python programı yazın <br>
Örnek Veri: num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
"""
num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
for key, values in num.items():
    num[key] = sorted(values)
print(num)
# %%

"""sozluk = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']} 

ilgili sözlükten anahtar kısımlarında bulunan boşlukları temizleyen python kodu yazınız. 
"""
sozluk = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']} 
sozluk = { k.replace(' ', ''): v for k, v in sozluk.items() }
print(sozluk)
# %%
"""liste=[1,2,3,4,5,6] listesindeki 1. elemanı del komutu ile siliniz?
"""
del liste[0]
print(liste)

#%%
"""
liste1=[1,2,3]
liste2=[4,5,6,7,8]
iki listeyi liste3 ile birleştiriniz?
"""
liste1=[1,2,3]
liste2=[4,5,6,7,8]
liste3 = liste1 + liste2
print(liste3)
# %%
"""
liste=["elma" , "armut", "çilek"] listesine append komutu ile sona 3 elemanını ekleyiniz?
"""
liste=["elma" , "armut", "çilek"]
liste.append(3)
print(liste)
# %%

"""Girilen on sayı içerisinden en büyük üç sayıyı bulmak için bir Python fonksiyonu yazınız"""

liste=[1,2,3,4,5,6]

print(sorted(liste,reverse=True)[:3])
# %%
"""Bir metin içerisindeki büyük ve küçük harflerin listesini yazdıran python programını yazınız."""

metin = input("metin giriniz")
kucuk=[]
buyuk=[]
for x in metin:
    if 65 <= ord(x) < 90:
        buyuk.append(x)
    else:
        kucuk.append(x)

print(f"buyuk harfler: {buyuk}")
print(f"kucuk harfler: {kucuk}") 
#%%
"""kullanıcıdan alınan 10 sayının çift ve tek sayıların sayısını ekrana yazdıran programı yazınız. """

for i in range(10):
    user_input = int(input("Sayi giriniz"))
    if (user_input % 2) == 0:
        print("Sayi cift")
    else:
        print("Sayi tek")
# %%
"""
Seven Segment Display 
https://en.wikipedia.org/wiki/Seven-segment_display

* * * * *
*       *
*       *
* * * * *
*       *
*       *
* * * * *

8 sayısı girildiğinde yukarıdaki çıktıyı veren python programını 0 dan 9 a kadar olan sayılar için yazalım
## hex,bin,zfill, tek satırda if

"""

