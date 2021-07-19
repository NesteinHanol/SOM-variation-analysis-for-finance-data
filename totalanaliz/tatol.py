# -*- coding: cp1254 -*-
tarihsorgu=raw_input("Hangi tarih = ")
toplam=0
dosya = open("eurusdALL.txt")
x=dosya.readlines()
t=len(x)
dosyaeurusd=[]
#dosya.seek(0)#imleci basa goturuyor dosyayi yeniden okuyabilmek icin
for i in range(0,t):
    #print(dosya.read())
    dosyaeurusd.append(x[i].split())

dosyaeurusd.reverse() #listeyi tarihsel olarak geçmişten bu güne sırala

dosya=open("sonuc2D.txt")
x=dosya.readlines()
t=len(x)
k=[]
for i in range(0,t):    
    k.append(x[i].split(" "))

for i in range(0,t): #sondaki /n işaretini yok etmek ve sistemi satir haline getirmek için 
    x=k[i][len(k[0])-1].split()
    k[i][len(k[0])-1]=x[0]


dosya = open("totalveri2D.txt")
x=dosya.readlines()
t=len(x)
totalveri=[]
#dosya.seek(0)#imleci basa goturuyor dosyayi yeniden okuyabilmek icin
for i in range(0,t):
    #print(dosya.read())
    totalveri.append(x[i].split(","))

for i in range(0,t): #sondaki /n işaretini yok etmek ve sistemi satir haline getirmek için 
    x=totalveri[i][len(totalveri[0])-1].split()
    totalveri[i][len(totalveri[0])-1]=x[0]

#tarih kısmını almak
tarihsecmedizi=[]
tarih=""
for i in range(0,len(k)):
    
    for yy in range(0,len(k[i][2])):#tarih kısmını alıyor
        tarihsecmedizi.append(k[i][2][yy])
    #["'", '0', '3', '.', '0', '2', '.', '2', '0', '0', '0', "'", ']']
    for r in range(1,11):
        tarih=tarih+str(tarihsecmedizi[r])

    if(tarihsorgu == tarih):
        kume=k[i][len(k[i])-1]
    tarihsecmedizi=[]
    tarih=""

print "2D --- ", "kume = ",kume,",eleman sayisi = ",totalveri[int(kume)][1],",ortalama =",totalveri[int(kume)][2]
toplam=toplam+float(totalveri[int(kume)][2])

##################################-----------------------------------------------------------------------------------------

dosya=open("sonuc3D.txt")
x=dosya.readlines()
t=len(x)
k=[]
for i in range(0,t):    
    k.append(x[i].split(" "))

for i in range(0,t): #sondaki /n işaretini yok etmek ve sistemi satir haline getirmek için 
    x=k[i][len(k[0])-1].split()
    k[i][len(k[0])-1]=x[0]


dosya = open("totalveri3D.txt")
x=dosya.readlines()
t=len(x)
totalveri=[]
#dosya.seek(0)#imleci basa goturuyor dosyayi yeniden okuyabilmek icin
for i in range(0,t):
    #print(dosya.read())
    totalveri.append(x[i].split(","))

for i in range(0,t): #sondaki /n işaretini yok etmek ve sistemi satir haline getirmek için 
    x=totalveri[i][len(totalveri[0])-1].split()
    totalveri[i][len(totalveri[0])-1]=x[0]

#tarih kısmını almak
tarihsecmedizi=[]
tarih=""
for i in range(0,len(k)):
    
    for yy in range(0,len(k[i][3])):#tarih kısmını alıyor
        tarihsecmedizi.append(k[i][3][yy])
    #["'", '0', '3', '.', '0', '2', '.', '2', '0', '0', '0', "'", ']']
    for r in range(1,11):
        tarih=tarih+str(tarihsecmedizi[r])

    if(tarihsorgu == tarih):
        kume=k[i][len(k[i])-1]
    tarihsecmedizi=[]
    tarih=""
print "3D --- ", "kume = ",kume,",eleman sayisi = ",totalveri[int(kume)][1],",ortalama =",totalveri[int(kume)][2]
toplam=toplam+float(totalveri[int(kume)][2])

##################################-----------------------------------------------------------------------------------------

dosya=open("sonuc4D.txt")
x=dosya.readlines()
t=len(x)
k=[]
for i in range(0,t):    
    k.append(x[i].split(" "))

for i in range(0,t): #sondaki /n işaretini yok etmek ve sistemi satir haline getirmek için 
    x=k[i][len(k[0])-1].split()
    k[i][len(k[0])-1]=x[0]


dosya = open("totalveri4D.txt")
x=dosya.readlines()
t=len(x)
totalveri=[]
#dosya.seek(0)#imleci basa goturuyor dosyayi yeniden okuyabilmek icin
for i in range(0,t):
    #print(dosya.read())
    totalveri.append(x[i].split(","))

for i in range(0,t): #sondaki /n işaretini yok etmek ve sistemi satir haline getirmek için 
    x=totalveri[i][len(totalveri[0])-1].split()
    totalveri[i][len(totalveri[0])-1]=x[0]

#tarih kısmını almak
tarihsecmedizi=[]
tarih=""
for i in range(0,len(k)):
    
    for yy in range(0,len(k[i][4])):#tarih kısmını alıyor
        tarihsecmedizi.append(k[i][4][yy])
    #["'", '0', '3', '.', '0', '2', '.', '2', '0', '0', '0', "'", ']']
    for r in range(1,11):
        tarih=tarih+str(tarihsecmedizi[r])

    if(tarihsorgu == tarih):
        kume=k[i][len(k[i])-1]
    tarihsecmedizi=[]
    tarih=""
print "4D --- ", "kume = ",kume,",eleman sayisi = ",totalveri[int(kume)][1],",ortalama =",totalveri[int(kume)][2]
toplam=toplam+float(totalveri[int(kume)][2])

##################################-----------------------------------------------------------------------------------------

dosya=open("sonuc5D.txt")
x=dosya.readlines()
t=len(x)
k=[]
for i in range(0,t):    
    k.append(x[i].split(" "))

for i in range(0,t): #sondaki /n işaretini yok etmek ve sistemi satir haline getirmek için 
    x=k[i][len(k[0])-1].split()
    k[i][len(k[0])-1]=x[0]


dosya = open("totalveri5D.txt")
x=dosya.readlines()
t=len(x)
totalveri=[]
#dosya.seek(0)#imleci basa goturuyor dosyayi yeniden okuyabilmek icin
for i in range(0,t):
    #print(dosya.read())
    totalveri.append(x[i].split(","))

for i in range(0,t): #sondaki /n işaretini yok etmek ve sistemi satir haline getirmek için 
    x=totalveri[i][len(totalveri[0])-1].split()
    totalveri[i][len(totalveri[0])-1]=x[0]

#tarih kısmını almak
tarihsecmedizi=[]
tarih=""
for i in range(0,len(k)):
    
    for yy in range(0,len(k[i][5])):#tarih kısmını alıyor
        tarihsecmedizi.append(k[i][5][yy])
    #["'", '0', '3', '.', '0', '2', '.', '2', '0', '0', '0', "'", ']']
    for r in range(1,11):
        tarih=tarih+str(tarihsecmedizi[r])

    if(tarihsorgu == tarih):
        kume=k[i][len(k[i])-1]
    tarihsecmedizi=[]
    tarih=""
print "5D --- ", "kume = ",kume,",eleman sayisi = ",totalveri[int(kume)][1],",ortalama =",totalveri[int(kume)][2]
toplam=toplam+float(totalveri[int(kume)][2])

##################################-----------------------------------------------------------------------------------------

dosya=open("sonuc6D.txt")
x=dosya.readlines()
t=len(x)
k=[]
for i in range(0,t):    
    k.append(x[i].split(" "))

for i in range(0,t): #sondaki /n işaretini yok etmek ve sistemi satir haline getirmek için 
    x=k[i][len(k[0])-1].split()
    k[i][len(k[0])-1]=x[0]


dosya = open("totalveri6D.txt")
x=dosya.readlines()
t=len(x)
totalveri=[]
#dosya.seek(0)#imleci basa goturuyor dosyayi yeniden okuyabilmek icin
for i in range(0,t):
    #print(dosya.read())
    totalveri.append(x[i].split(","))

for i in range(0,t): #sondaki /n işaretini yok etmek ve sistemi satir haline getirmek için 
    x=totalveri[i][len(totalveri[0])-1].split()
    totalveri[i][len(totalveri[0])-1]=x[0]

#tarih kısmını almak
tarihsecmedizi=[]
tarih=""
for i in range(0,len(k)):
    
    for yy in range(0,len(k[i][6])):#tarih kısmını alıyor
        tarihsecmedizi.append(k[i][6][yy])
    #["'", '0', '3', '.', '0', '2', '.', '2', '0', '0', '0', "'", ']']
    for r in range(1,11):
        tarih=tarih+str(tarihsecmedizi[r])

    if(tarihsorgu == tarih):
        kume=k[i][len(k[i])-1]
    tarihsecmedizi=[]
    tarih=""
print "6D --- ", "kume = ",kume,",eleman sayisi = ",totalveri[int(kume)][1],",ortalama =",totalveri[int(kume)][2]
toplam=toplam+float(totalveri[int(kume)][2])

##################################-----------------------------------------------------------------------------------------

dosya=open("sonucK1.txt")
x=dosya.readlines()
t=len(x)
k=[]
for i in range(0,t):    
    k.append(x[i].split(" "))

for i in range(0,t): #sondaki /n işaretini yok etmek ve sistemi satir haline getirmek için 
    x=k[i][len(k[0])-1].split()
    k[i][len(k[0])-1]=x[0]


dosya = open("totalveriK1.txt")
x=dosya.readlines()
t=len(x)
totalveri=[]
#dosya.seek(0)#imleci basa goturuyor dosyayi yeniden okuyabilmek icin
for i in range(0,t):
    #print(dosya.read())
    totalveri.append(x[i].split(","))

for i in range(0,t): #sondaki /n işaretini yok etmek ve sistemi satir haline getirmek için 
    x=totalveri[i][len(totalveri[0])-1].split()
    totalveri[i][len(totalveri[0])-1]=x[0]

#tarih kısmını almak
tarihsecmedizi=[]
tarih=""
for i in range(0,len(k)):
    
    for yy in range(0,len(k[i][2])):#tarih kısmını alıyor
        tarihsecmedizi.append(k[i][2][yy])
    #["'", '0', '3', '.', '0', '2', '.', '2', '0', '0', '0', "'", ']']
    for r in range(1,11):
        tarih=tarih+str(tarihsecmedizi[r])

    if(tarihsorgu == tarih):
        kume=k[i][len(k[i])-1]
    tarihsecmedizi=[]
    tarih=""
print "K1 --- ", "kume = ",kume,",eleman sayisi = ",totalveri[int(kume)][1],",ortalama =",totalveri[int(kume)][2]
toplam=toplam+float(totalveri[int(kume)][2])

##################################-----------------------------------------------------------------------------------------

dosya=open("sonucK2.txt")
x=dosya.readlines()
t=len(x)
k=[]
for i in range(0,t):    
    k.append(x[i].split(" "))

for i in range(0,t): #sondaki /n işaretini yok etmek ve sistemi satir haline getirmek için 
    x=k[i][len(k[0])-1].split()
    k[i][len(k[0])-1]=x[0]


dosya = open("totalveriK2.txt")
x=dosya.readlines()
t=len(x)
totalveri=[]
#dosya.seek(0)#imleci basa goturuyor dosyayi yeniden okuyabilmek icin
for i in range(0,t):
    #print(dosya.read())
    totalveri.append(x[i].split(","))

for i in range(0,t): #sondaki /n işaretini yok etmek ve sistemi satir haline getirmek için 
    x=totalveri[i][len(totalveri[0])-1].split()
    totalveri[i][len(totalveri[0])-1]=x[0]

#tarih kısmını almak
tarihsecmedizi=[]
tarih=""
for i in range(0,len(k)):
    
    for yy in range(0,len(k[i][3])):#tarih kısmını alıyor
        tarihsecmedizi.append(k[i][3][yy])
    #["'", '0', '3', '.', '0', '2', '.', '2', '0', '0', '0', "'", ']']
    for r in range(1,11):
        tarih=tarih+str(tarihsecmedizi[r])

    if(tarihsorgu == tarih):
        kume=k[i][len(k[i])-1]
    tarihsecmedizi=[]
    tarih=""
print "K2 --- ", "kume = ",kume,",eleman sayisi = ",totalveri[int(kume)][1],",ortalama =",totalveri[int(kume)][2]
toplam=toplam+float(totalveri[int(kume)][2])

##################################-----------------------------------------------------------------------------------------

dosya=open("sonucK3.txt")
x=dosya.readlines()
t=len(x)
k=[]
for i in range(0,t):    
    k.append(x[i].split(" "))

for i in range(0,t): #sondaki /n işaretini yok etmek ve sistemi satir haline getirmek için 
    x=k[i][len(k[0])-1].split()
    k[i][len(k[0])-1]=x[0]


dosya = open("totalveriK3.txt")
x=dosya.readlines()
t=len(x)
totalveri=[]
#dosya.seek(0)#imleci basa goturuyor dosyayi yeniden okuyabilmek icin
for i in range(0,t):
    #print(dosya.read())
    totalveri.append(x[i].split(","))

for i in range(0,t): #sondaki /n işaretini yok etmek ve sistemi satir haline getirmek için 
    x=totalveri[i][len(totalveri[0])-1].split()
    totalveri[i][len(totalveri[0])-1]=x[0]

#tarih kısmını almak
tarihsecmedizi=[]
tarih=""
for i in range(0,len(k)):
    
    for yy in range(0,len(k[i][2])):#tarih kısmını alıyor
        tarihsecmedizi.append(k[i][2][yy])
    #["'", '0', '3', '.', '0', '2', '.', '2', '0', '0', '0', "'", ']']
    for r in range(1,11):
        tarih=tarih+str(tarihsecmedizi[r])

    if(tarihsorgu == tarih):
        kume=k[i][len(k[i])-1]
    tarihsecmedizi=[]
    tarih=""
print "K3 --- ", "kume = ",kume,",eleman sayisi = ",totalveri[int(kume)][1],",ortalama =",totalveri[int(kume)][2]
toplam=toplam+float(totalveri[int(kume)][2])

##################################-----------------------------------------------------------------------------------------

dosya=open("sonucK4.txt")
x=dosya.readlines()
t=len(x)
k=[]
for i in range(0,t):    
    k.append(x[i].split(" "))

for i in range(0,t): #sondaki /n işaretini yok etmek ve sistemi satir haline getirmek için 
    x=k[i][len(k[0])-1].split()
    k[i][len(k[0])-1]=x[0]


dosya = open("totalveriK4.txt")
x=dosya.readlines()
t=len(x)
totalveri=[]
#dosya.seek(0)#imleci basa goturuyor dosyayi yeniden okuyabilmek icin
for i in range(0,t):
    #print(dosya.read())
    totalveri.append(x[i].split(","))

for i in range(0,t): #sondaki /n işaretini yok etmek ve sistemi satir haline getirmek için 
    x=totalveri[i][len(totalveri[0])-1].split()
    totalveri[i][len(totalveri[0])-1]=x[0]

#tarih kısmını almak
tarihsecmedizi=[]
tarih=""
for i in range(0,len(k)):
    
    for yy in range(0,len(k[i][2])):#tarih kısmını alıyor
        tarihsecmedizi.append(k[i][2][yy])
    #["'", '0', '3', '.', '0', '2', '.', '2', '0', '0', '0', "'", ']']
    for r in range(1,11):
        tarih=tarih+str(tarihsecmedizi[r])

    if(tarihsorgu == tarih):
        kume=k[i][len(k[i])-1]
    tarihsecmedizi=[]
    tarih=""
print "K4 --- ", "kume = ",kume,",eleman sayisi = ",totalveri[int(kume)][1],",ortalama =",totalveri[int(kume)][2]
toplam=toplam+float(totalveri[int(kume)][2])

##################################-----------------------------------------------------------------------------------------

dosya=open("sonucK5.txt")
x=dosya.readlines()
t=len(x)
k=[]
for i in range(0,t):    
    k.append(x[i].split(" "))

for i in range(0,t): #sondaki /n işaretini yok etmek ve sistemi satir haline getirmek için 
    x=k[i][len(k[0])-1].split()
    k[i][len(k[0])-1]=x[0]


dosya = open("totalveriK5.txt")
x=dosya.readlines()
t=len(x)
totalveri=[]
#dosya.seek(0)#imleci basa goturuyor dosyayi yeniden okuyabilmek icin
for i in range(0,t):
    #print(dosya.read())
    totalveri.append(x[i].split(","))

for i in range(0,t): #sondaki /n işaretini yok etmek ve sistemi satir haline getirmek için 
    x=totalveri[i][len(totalveri[0])-1].split()
    totalveri[i][len(totalveri[0])-1]=x[0]

#tarih kısmını almak
tarihsecmedizi=[]
tarih=""
for i in range(0,len(k)):
    
    for yy in range(0,len(k[i][3])):#tarih kısmını alıyor
        tarihsecmedizi.append(k[i][3][yy])
    #["'", '0', '3', '.', '0', '2', '.', '2', '0', '0', '0', "'", ']']
    for r in range(1,11):
        tarih=tarih+str(tarihsecmedizi[r])

    if(tarihsorgu == tarih):
        kume=k[i][len(k[i])-1]
    tarihsecmedizi=[]
    tarih=""
print "K5 --- ", "kume = ",kume,",eleman sayisi = ",totalveri[int(kume)][1],",ortalama =",totalveri[int(kume)][2]
toplam=toplam+float(totalveri[int(kume)][2])

##################################-----------------------------------------------------------------------------------------

dosya=open("sonucK6.txt")
x=dosya.readlines()
t=len(x)
k=[]
for i in range(0,t):    
    k.append(x[i].split(" "))

for i in range(0,t): #sondaki /n işaretini yok etmek ve sistemi satir haline getirmek için 
    x=k[i][len(k[0])-1].split()
    k[i][len(k[0])-1]=x[0]


dosya = open("totalveriK6.txt")
x=dosya.readlines()
t=len(x)
totalveri=[]
#dosya.seek(0)#imleci basa goturuyor dosyayi yeniden okuyabilmek icin
for i in range(0,t):
    #print(dosya.read())
    totalveri.append(x[i].split(","))

for i in range(0,t): #sondaki /n işaretini yok etmek ve sistemi satir haline getirmek için 
    x=totalveri[i][len(totalveri[0])-1].split()
    totalveri[i][len(totalveri[0])-1]=x[0]

#tarih kısmını almak
tarihsecmedizi=[]
tarih=""
for i in range(0,len(k)):
    
    for yy in range(0,len(k[i][4])):#tarih kısmını alıyor
        tarihsecmedizi.append(k[i][4][yy])
    #["'", '0', '3', '.', '0', '2', '.', '2', '0', '0', '0', "'", ']']
    for r in range(1,11):
        tarih=tarih+str(tarihsecmedizi[r])

    if(tarihsorgu == tarih):
        kume=k[i][len(k[i])-1]
    tarihsecmedizi=[]
    tarih=""
print "K6 --- ", "kume = ",kume,",eleman sayisi = ",totalveri[int(kume)][1],",ortalama =",totalveri[int(kume)][2]
toplam=toplam+float(totalveri[int(kume)][2])

##################################-----------------------------------------------------------------------------------------

dosya=open("sonucK7.txt")
x=dosya.readlines()
t=len(x)
k=[]
for i in range(0,t):    
    k.append(x[i].split(" "))

for i in range(0,t): #sondaki /n işaretini yok etmek ve sistemi satir haline getirmek için 
    x=k[i][len(k[0])-1].split()
    k[i][len(k[0])-1]=x[0]


dosya = open("totalveriK7.txt")
x=dosya.readlines()
t=len(x)
totalveri=[]
#dosya.seek(0)#imleci basa goturuyor dosyayi yeniden okuyabilmek icin
for i in range(0,t):
    #print(dosya.read())
    totalveri.append(x[i].split(","))

for i in range(0,t): #sondaki /n işaretini yok etmek ve sistemi satir haline getirmek için 
    x=totalveri[i][len(totalveri[0])-1].split()
    totalveri[i][len(totalveri[0])-1]=x[0]

#tarih kısmını almak
tarihsecmedizi=[]
tarih=""
for i in range(0,len(k)):
    
    for yy in range(0,len(k[i][3])):#tarih kısmını alıyor
        tarihsecmedizi.append(k[i][3][yy])
    #["'", '0', '3', '.', '0', '2', '.', '2', '0', '0', '0', "'", ']']
    for r in range(1,11):
        tarih=tarih+str(tarihsecmedizi[r])

    if(tarihsorgu == tarih):
        kume=k[i][len(k[i])-1]
    tarihsecmedizi=[]
    tarih=""
print "K7 --- ", "kume = ",kume,",eleman sayisi = ",totalveri[int(kume)][1],",ortalama =",totalveri[int(kume)][2]
toplam=toplam+float(totalveri[int(kume)][2])

##################################-----------------------------------------------------------------------------------------
print "Toplam Ortalama == ",toplam
