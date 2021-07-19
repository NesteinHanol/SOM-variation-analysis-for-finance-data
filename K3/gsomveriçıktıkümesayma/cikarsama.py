# -*- coding: cp1254 -*-
dosya = open("eurusdALL.txt")
x=dosya.readlines()
t=len(x)
h=[]
#dosya.seek(0)#imleci basa goturuyor dosyayi yeniden okuyabilmek icin
for i in range(0,t):
    #print(dosya.read())
    h.append(x[i].split())

h.reverse() #listeyi tarihsel olarak geçmişten bu güne sırala
##################################################3
dosya=open("sonucK3.txt")
x=dosya.readlines()
t=len(x)
k=[]
for i in range(0,t):    
    k.append(x[i].split(" "))

for i in range(0,t): #sondaki /n işaretini yok etmek ve sistemi satir haline getirmek için 
    x=k[i][len(k[0])-1].split()
    k[i][len(k[0])-1]=x[0]

toplam=0
##print ("-------- 511-10000.txt ---------")
for i in range(0,400):
    ortalamatoplamfiyat=0
    artis=0
    for s in range(0,t):
        
        if (int(k[s][len(k[0])-1])==i):
            toplam=toplam+1
            
            tarih=""
            tarihsecmedizi=[]
            for yy in range(0,len(k[s][2])):#tarih kısmını alıyor
                tarihsecmedizi.append(k[s][2][yy])
    #["'", '0', '3', '.', '0', '2', '.', '2', '0', '0', '0', "'", ']']
            for r in range(1,11):
                tarih=tarih+str(tarihsecmedizi[r])
                
            for u in range(0,len(h)):
                if (h[u][0] == tarih):
                    artis=artis+float(h[u+1][len(h[u])-1])
                    artis=artis+float(h[u+2][len(h[u])-1])
                    artis=artis+float(h[u+3][len(h[u])-1])
                    
##                if((h[u][0] == tarih) and (i==235) ):
##                    artis=artis+float(h[u+1][len(h[u])-1])
##                    print (artis)
##                    artis=artis+float(h[u+2][len(h[u])-1])
##                    print (artis)
                    
                    


    if toplam==0:
        print (i," kumenin eleman sayisi == ",toplam)
    else:
        sonucortalama = artis/(toplam*3)
        if (sonucortalama<0.0001 and sonucortalama >0):
            print (i," kumenin eleman sayisi == NOTUR")
        else:
            print (i," kumenin eleman sayisi == ",toplam,"-",sonucortalama)
    toplam=0

##tarih=""
##tarihsecmedizi=[]
##for s in range(0,len(k[0][2])):#tarih kısmını alıyor
##    tarihsecmedizi.append(k[0][2][s])
##    #["'", '0', '3', '.', '0', '2', '.', '2', '0', '0', '0', "'", ']']
##for r in range(1,11):
##    tarih=tarih+str(tarihsecmedizi[r])



   
