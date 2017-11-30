import sqlite3
baglanti=sqlite3.connect('d:/database.db')
isaretci=baglanti.cursor()
isaretci.execute('''CREATE TABLE Arabalar(Arabano INTEGER PRIMARY KEY, ArabaMarka VARCHAR(20), ArabaPlaka VARCHAR(10), ArabaRenk VARCHAR(20))''')
isaretci.execute('''CREATE TABLE Musteriler(Musno INTEGER PRIMARY KEY, AdSoyad VARCHAR(20), Tel VARCHAR(15), TC VARCHAR(11))''')
isaretci.execute('''CREATE TABLE Kiralama(Kiralamano INTEGER PRIMARY KEY, Musno INTEGER REFERENCES Musteriler(Musno), Arabano INTEGER REFERENCES Arabalar(Arabano) ,KiralamaBedeli MONEY, Tarih DATE)''')
baglanti.commit()

#//////////FONKSIYONLAR/////////////////
#/////////ARABALAR TABLOSU FONKSIYONLARI/////////////
def araba_listele():	#Arabalari listeler
	isaretci=baglanti.cursor()
	dataset = isaretci.execute('''select * from Arabalar''')  
	print(dataset.fetchall())
	baglanti.commit()
def araba_ekle():	#Arabalari ekler
	isaretci=baglanti.cursor()
	No=input("Araba Sira Numarasi Girin: ")
	Marka=input("Marka Girin: ")
	Plaka=input("Plaka Girin: ")
	Renk=input("Renk girin: ")
	isaretci.execute('''INSERT INTO Arabalar (Arabano,ArabaMarka,ArabaPlaka,ArabaRenk) VALUES (?,?,?,?)''',(No,Marka,Plaka,Renk))
	baglanti.commit()
def araba_sil():	#Arabalari siler
	isaretci=baglanti.cursor()
	No=input("Silinecek Olan Araba Sira Numarasi Girin: ")
	isaretci.execute('''DELETE FROM Arabalar WHERE Arabano = ?''',(No))
	baglanti.commit()
def araba_guncelle():	#Arabalari gunceller
	isaretci=baglanti.cursor()
	No=input("Guncellemek Istenilen Araba Nosunu Giriniz: ")
	Marka=input("Marka Girin: ")
	Plaka=input("Plaka Girin: ")
	Renk=input("Renk girin: ")
	dataset = isaretci.execute('''UPDATE Arabalar SET ArabaMarka = ?,ArabaPlaka = ?,ArabaRenk = ? WHERE Arabano=?''',(Marka,Plaka,Renk,No))
	baglanti.commit()
def araba_arama():	#Araba arar
	No=input("Araba No Giriniz: ")
	dataset = isaretci.execute('''SELECT * FROM Arabalar WHERE Arabano = ?''',(No))
	for i in dataset.fetchall():
		print("Araba No :\t",i[0])
		print("Araba Marka :\t",i[1])
		print("Araba Plaka :\t\t",i[2])
		print("Araba Renk :\t\t",i[3])
		
#/////////MUSTERILER TABLOSU FONKSIYONLARI//////////////
def musteri_listele():	#Musterileri listeler
	isaretci=baglanti.cursor()
	dataset = isaretci.execute('''select * from Musteriler''')  
	print(dataset.fetchall())
	baglanti.commit()
def musteri_ekle():	#Musterileri ekler
	isaretci=baglanti.cursor()
	No = input("Musteri Sira Numarasi Girin: ")
	Isim = input("Ad Soyad Girin: ")
	Telefon = input("Telefon Girin: ")
	Kimlik = input("Tc Kimlik girin: ")
	isaretci.execute('''INSERT INTO Musteriler (Musno,AdSoyad,Tel,TC) VALUES(?,?,?,?)''',(No,Isim,Telefon,Kimlik))
	baglanti.commit()
def musteri_sil():	#Musterileri siler
	isaretci=baglanti.cursor()
	No=input("Silinecek Olan Musteri Sira Numarasi Girin: ")
	isaretci.execute('''DELETE FROM Musteriler WHERE Musno=?''',(No))
	baglanti.commit()
def musteri_guncelle():	#Musterileri gunceller
	isaretci=baglanti.cursor()
	No=input("Guncellemek Istenilen Musteri Nosunu Giriniz: ")
	Isim=input("Ad Soyad Girin: ")
	Telefon=input("Telefon Girin: ")
	Kimlik=input("Kimlik Girin: ")
	dataset = isaretci.execute('''UPDATE Musteriler SET AdSoyad=?,Tel=?,TC=? WHERE Musno=?''',(Isim,Telefon,Kimlik,No))
	baglanti.commit()
def musteri_arama():	#Musteri arar
	No=input("Musteri No Giriniz: ")
	dataset = isaretci.execute('''SELECT * FROM Musteriler WHERE Musno = ?''',(No))
	for i in dataset.fetchall():
		print("Musteri No:\t",i[0])
		print("Musteri Ad Soyad:\t",i[1])
		print("Musteri Telefon:\t\t",i[2])
		print("Musteri Kimlik:\t\t",i[3])
		
#/////////KIRALAMA TABLOSU FONKSIYONLARI//////////////
def kiralama_listele():	#Kiralama listeler
	isaretci=baglanti.cursor()
	dataset = isaretci.execute('''select * from Kiralama''')  
	print(dataset.fetchall())
	baglanti.commit()
def kiralama_ekle():	#Kiralama ekler
	isaretci=baglanti.cursor()
	No = input("Kiralama Sira Numarasi Girin: ")
	Musid = input("Mus No Girin: ")
	Arabaid = input("Araba No Girin: ")
	Ucret = input("Ucret Girin: ")
	Tarih = input("Tarih Girin: ")
	isaretci.execute('''INSERT INTO Kiralama (Kiralamano,Musno,Arabano,KiralamaBedeli,Tarih) VALUES(?,?,?,?,?)''',(No,Musid,Arabaid,Ucret,Tarih))
	baglanti.commit()
def kiralama_sil():	#Kiralama siler
	isaretci=baglanti.cursor()
	No=input("Silinecek Olan Kiralama Sira Numarasi Girin: ")
	isaretci.execute('''DELETE FROM Kiralama WHERE Kiralamano=?''',(No))
	baglanti.commit()
def kiralama_guncelle():	#Kiralama gunceller
	isaretci=baglanti.cursor()
	No = input("Kiralama Sira Numarasi Girin: ")
	Musid = input("Mus No Girin: ")
	Arabaid = input("Araba No Girin: ")
	Ucret = input("Ucret Girin: ")
	Tarih = input("Tarih Girin: ")
	dataset = isaretci.execute('''UPDATE Kiralama SET Musno=?,Arabano=?,KiralamaBedeli=?,Tarih=? WHERE Kiralamano=?''',(Musid,Arabaid,Ucret,Tarih,No))
	baglanti.commit()
def kiralama_arama():	#Kiralama arar
	No=input("Kiralama No Giriniz: ")
	dataset = isaretci.execute('''SELECT * FROM Kiralama WHERE Kiralamano = ?''',(No))
	for i in dataset.fetchall():
		print("Kiralama No:\t",i[0])
		print("Kiralama Mus No:\t",i[1])
		print("Kiralama Araba No:\t",i[2])
		print("Kiralama Ucret:\t",i[3])
		print("Kiralama Tarih:\t",i[4])
		



secim=input("\t\t\tUni Rent A Car \n 1-Arabalar \n 2-Musteriler\n 3-Kiralama \nSecim : ")
secim=int (secim)

if(secim==1):	#////Arabalar secilmis ise
	arabasec=input("Arabalar  \n 1-Goster \n 2-Ekle \n 3-Sil \n 4-Guncelle \n 5-Ara \nSecim : ")
	arabasec=int (arabasec)
	if(arabasec==1): 
		araba_listele()
	elif(arabasec==2):
		araba_ekle()
	elif(arabasec==3): 
		araba_sil()
	elif(arabasec==4):
		araba_guncelle()
	elif(arabasec==5):
		araba_arama()
	else:
		print("Yanlis deger girdiniz.. 1,2,3,4,5 degerlerini girebilirsiniz")
elif(secim==2):	#////Musteriler secilmis ise
	musterisec=input("Musteriler  \n 1-Goster \n 2-Ekle \n 3-Sil \n 4-Guncelle \n 5-Ara \nSecim : ")
	musterisec=int (musterisec)
	if(musterisec==1):
		musteri_listele()
	elif(musterisec==2):
		musteri_ekle()
	elif(musterisec==3): 
		musteri_sil()
	elif(musterisec==4):
		musteri_guncelle()
	elif(musterisec==5):
		musteri_arama()
	else:
		print("Yanlis deger girdiniz.. 1,2,3,4,5 degerlerini girebilirsiniz")
elif(secim==3):	#////Kiralama secilmis ise
	kiralamasec=input("Kiralama  \n 1-Goster \n 2-Ekle \n 3-Sil \n 4-Guncelle \n 5-Ara \nSecim : ")
	kiralamasec=int (kiralamasec)
	if(kiralamasec==1):
		kiralama_listele()
	elif(kiralamasec==2):
		kiralama_ekle()
	elif(kiralamasec==3): 
		kiralama_sil()
	elif(kiralamasec==4):
		kiralama_guncelle()
	elif(kiralamasec==5):
		kiralama_arama()
	else:
		print("Yanlis deger girdiniz.. 1,2,3,4,5 degerlerini girebilirsiniz")
else:
	print("Yanlis deger girdiniz.. 1,2,3 degerlerini girebilirsiniz")

