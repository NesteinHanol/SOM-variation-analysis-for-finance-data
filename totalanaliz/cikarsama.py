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
dosya=open("sonuc2D.txt")
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
yazilacakdizi=[]
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
        #print (i," kumenin eleman sayisi == ",toplam)
        yazilacakdizi.append([i,toplam,"BOS"])
    else:
        sonucortalama = artis/(toplam*3)
        #sonucortalama = artis/toplam
        if (sonucortalama<0.0001 and sonucortalama >0):
            #print (i," kumenin eleman sayisi == ",toplam,"-","NOTUR")
            yazilacakdizi.append([i,toplam,"NOTUR"])
        else:
            #print (i," kumenin eleman sayisi == ",toplam,"-",sonucortalama)
            yazilacakdizi.append([i,toplam,sonucortalama])
    toplam=0

dosya=open("totalveri2D.txt","w")
st=""
for i in range(0,len(yazilacakdizi)):
    for k in range(0,len(yazilacakdizi[i])-1):
        st=st+str(yazilacakdizi[i][k])+","
    st=st+str(yazilacakdizi[i][len(yazilacakdizi[i])-1])
    st=st+"\n"
    dosya.write(st)
    st=""
dosya.close()

##tarih=""
##tarihsecmedizi=[]
##for s in range(0,len(k[0][2])):#tarih kısmını alıyor
##    tarihsecmedizi.append(k[0][2][s])
##    #["'", '0', '3', '.', '0', '2', '.', '2', '0', '0', '0', "'", ']']
##for r in range(1,11):
##    tarih=tarih+str(tarihsecmedizi[r])
###################################################################3
dosya=open("sonuc3D.txt")
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
yazilacakdizi=[]
for i in range(0,400):
    ortalamatoplamfiyat=0
    artis=0
    for s in range(0,t):
        
        if (int(k[s][len(k[0])-1])==i):
            toplam=toplam+1
            
            tarih=""
            tarihsecmedizi=[]
            for yy in range(0,len(k[s][3])):#tarih kısmını alıyor
                tarihsecmedizi.append(k[s][3][yy])
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
        #print (i," kumenin eleman sayisi == ",toplam)
        yazilacakdizi.append([i,toplam,"BOS"])
    else:
        sonucortalama = artis/(toplam*3)
        #sonucortalama = artis/toplam
        if (sonucortalama<0.0001 and sonucortalama >0):
            #print (i," kumenin eleman sayisi == ",toplam,"-","NOTUR")
            yazilacakdizi.append([i,toplam,"NOTUR"])
        else:
            #print (i," kumenin eleman sayisi == ",toplam,"-",sonucortalama)
            yazilacakdizi.append([i,toplam,sonucortalama])
    toplam=0

dosya=open("totalveri3D.txt","w")
st=""
for i in range(0,len(yazilacakdizi)):
    for k in range(0,len(yazilacakdizi[i])-1):
        st=st+str(yazilacakdizi[i][k])+","
    st=st+str(yazilacakdizi[i][len(yazilacakdizi[i])-1])
    st=st+"\n"
    dosya.write(st)
    st=""
dosya.close()
##################################################################
###################################################################3
dosya=open("sonuc4D.txt")
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
yazilacakdizi=[]
for i in range(0,400):
    ortalamatoplamfiyat=0
    artis=0
    for s in range(0,t):
        
        if (int(k[s][len(k[0])-1])==i):
            toplam=toplam+1
            
            tarih=""
            tarihsecmedizi=[]
            for yy in range(0,len(k[s][4])):#tarih kısmını alıyor
                tarihsecmedizi.append(k[s][4][yy])
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
        #print (i," kumenin eleman sayisi == ",toplam)
        yazilacakdizi.append([i,toplam,"BOS"])
    else:
        sonucortalama = artis/(toplam*3)
        #sonucortalama = artis/toplam
        if (sonucortalama<0.0001 and sonucortalama >0):
            #print (i," kumenin eleman sayisi == ",toplam,"-","NOTUR")
            yazilacakdizi.append([i,toplam,"NOTUR"])
        else:
            #print (i," kumenin eleman sayisi == ",toplam,"-",sonucortalama)
            yazilacakdizi.append([i,toplam,sonucortalama])
    toplam=0

dosya=open("totalveri4D.txt","w")
st=""
for i in range(0,len(yazilacakdizi)):
    for k in range(0,len(yazilacakdizi[i])-1):
        st=st+str(yazilacakdizi[i][k])+","
    st=st+str(yazilacakdizi[i][len(yazilacakdizi[i])-1])
    st=st+"\n"
    dosya.write(st)
    st=""
dosya.close()
##################################################################   
###################################################################3
dosya=open("sonuc5D.txt")
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
yazilacakdizi=[]
for i in range(0,400):
    ortalamatoplamfiyat=0
    artis=0
    for s in range(0,t):
        
        if (int(k[s][len(k[0])-1])==i):
            toplam=toplam+1
            
            tarih=""
            tarihsecmedizi=[]
            for yy in range(0,len(k[s][5])):#tarih kısmını alıyor
                tarihsecmedizi.append(k[s][5][yy])
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
        #print (i," kumenin eleman sayisi == ",toplam)
        yazilacakdizi.append([i,toplam,"BOS"])
    else:
        sonucortalama = artis/(toplam*3)
        #sonucortalama = artis/toplam
        if (sonucortalama<0.0001 and sonucortalama >0):
            #print (i," kumenin eleman sayisi == ",toplam,"-","NOTUR")
            yazilacakdizi.append([i,toplam,"NOTUR"])
        else:
            #print (i," kumenin eleman sayisi == ",toplam,"-",sonucortalama)
            yazilacakdizi.append([i,toplam,sonucortalama])
    toplam=0

dosya=open("totalveri5D.txt","w")
st=""
for i in range(0,len(yazilacakdizi)):
    for k in range(0,len(yazilacakdizi[i])-1):
        st=st+str(yazilacakdizi[i][k])+","
    st=st+str(yazilacakdizi[i][len(yazilacakdizi[i])-1])
    st=st+"\n"
    dosya.write(st)
    st=""
dosya.close()
##################################################################
###################################################################3
dosya=open("sonuc6D.txt")
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
yazilacakdizi=[]
for i in range(0,400):
    ortalamatoplamfiyat=0
    artis=0
    for s in range(0,t):
        
        if (int(k[s][len(k[0])-1])==i):
            toplam=toplam+1
            
            tarih=""
            tarihsecmedizi=[]
            for yy in range(0,len(k[s][6])):#tarih kısmını alıyor
                tarihsecmedizi.append(k[s][6][yy])
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
        #print (i," kumenin eleman sayisi == ",toplam)
        yazilacakdizi.append([i,toplam,"BOS"])
    else:
        sonucortalama = artis/(toplam*3)
        #sonucortalama = artis/toplam
        if (sonucortalama<0.0001 and sonucortalama >0):
            #print (i," kumenin eleman sayisi == ",toplam,"-","NOTUR")
            yazilacakdizi.append([i,toplam,"NOTUR"])
        else:
            #print (i," kumenin eleman sayisi == ",toplam,"-",sonucortalama)
            yazilacakdizi.append([i,toplam,sonucortalama])
    toplam=0

dosya=open("totalveri6D.txt","w")
st=""
for i in range(0,len(yazilacakdizi)):
    for k in range(0,len(yazilacakdizi[i])-1):
        st=st+str(yazilacakdizi[i][k])+","
    st=st+str(yazilacakdizi[i][len(yazilacakdizi[i])-1])
    st=st+"\n"
    dosya.write(st)
    st=""
dosya.close()
##################################################################
###################################################################3
dosya=open("sonucK1.txt")
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
yazilacakdizi=[]
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
        #print (i," kumenin eleman sayisi == ",toplam)
        yazilacakdizi.append([i,toplam,"BOS"])
    else:
        sonucortalama = artis/(toplam*3)
        #sonucortalama = artis/toplam
        if (sonucortalama<0.0001 and sonucortalama >0):
            #print (i," kumenin eleman sayisi == ",toplam,"-","NOTUR")
            yazilacakdizi.append([i,toplam,"NOTUR"])
        else:
            #print (i," kumenin eleman sayisi == ",toplam,"-",sonucortalama)
            yazilacakdizi.append([i,toplam,sonucortalama])
    toplam=0

dosya=open("totalveriK1.txt","w")
st=""
for i in range(0,len(yazilacakdizi)):
    for k in range(0,len(yazilacakdizi[i])-1):
        st=st+str(yazilacakdizi[i][k])+","
    st=st+str(yazilacakdizi[i][len(yazilacakdizi[i])-1])
    st=st+"\n"
    dosya.write(st)
    st=""
dosya.close()
##################################################################
###################################################################3
dosya=open("sonucK2.txt")
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
yazilacakdizi=[]
for i in range(0,400):
    ortalamatoplamfiyat=0
    artis=0
    for s in range(0,t):
        
        if (int(k[s][len(k[0])-1])==i):
            toplam=toplam+1
            
            tarih=""
            tarihsecmedizi=[]
            for yy in range(0,len(k[s][3])):#tarih kısmını alıyor
                tarihsecmedizi.append(k[s][3][yy])
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
        #print (i," kumenin eleman sayisi == ",toplam)
        yazilacakdizi.append([i,toplam,"BOS"])
    else:
        sonucortalama = artis/(toplam*3)
        #sonucortalama = artis/toplam
        if (sonucortalama<0.0001 and sonucortalama >0):
            #print (i," kumenin eleman sayisi == ",toplam,"-","NOTUR")
            yazilacakdizi.append([i,toplam,"NOTUR"])
        else:
            #print (i," kumenin eleman sayisi == ",toplam,"-",sonucortalama)
            yazilacakdizi.append([i,toplam,sonucortalama])
    toplam=0

dosya=open("totalveriK2.txt","w")
st=""
for i in range(0,len(yazilacakdizi)):
    for k in range(0,len(yazilacakdizi[i])-1):
        st=st+str(yazilacakdizi[i][k])+","
    st=st+str(yazilacakdizi[i][len(yazilacakdizi[i])-1])
    st=st+"\n"
    dosya.write(st)
    st=""
dosya.close()
##################################################################
###################################################################3
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
yazilacakdizi=[]
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
        #print (i," kumenin eleman sayisi == ",toplam)
        yazilacakdizi.append([i,toplam,"BOS"])
    else:
        sonucortalama = artis/(toplam*3)
        #sonucortalama = artis/toplam
        if (sonucortalama<0.0001 and sonucortalama >0):
            #print (i," kumenin eleman sayisi == ",toplam,"-","NOTUR")
            yazilacakdizi.append([i,toplam,"NOTUR"])
        else:
            #print (i," kumenin eleman sayisi == ",toplam,"-",sonucortalama)
            yazilacakdizi.append([i,toplam,sonucortalama])
    toplam=0

dosya=open("totalveriK3.txt","w")
st=""
for i in range(0,len(yazilacakdizi)):
    for k in range(0,len(yazilacakdizi[i])-1):
        st=st+str(yazilacakdizi[i][k])+","
    st=st+str(yazilacakdizi[i][len(yazilacakdizi[i])-1])
    st=st+"\n"
    dosya.write(st)
    st=""
dosya.close()
##################################################################
###################################################################3
dosya=open("sonucK4.txt")
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
yazilacakdizi=[]
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
        #print (i," kumenin eleman sayisi == ",toplam)
        yazilacakdizi.append([i,toplam,"BOS"])
    else:
        sonucortalama = artis/(toplam*3)
        #sonucortalama = artis/toplam
        if (sonucortalama<0.0001 and sonucortalama >0):
            #print (i," kumenin eleman sayisi == ",toplam,"-","NOTUR")
            yazilacakdizi.append([i,toplam,"NOTUR"])
        else:
            #print (i," kumenin eleman sayisi == ",toplam,"-",sonucortalama)
            yazilacakdizi.append([i,toplam,sonucortalama])
    toplam=0

dosya=open("totalveriK4.txt","w")
st=""
for i in range(0,len(yazilacakdizi)):
    for k in range(0,len(yazilacakdizi[i])-1):
        st=st+str(yazilacakdizi[i][k])+","
    st=st+str(yazilacakdizi[i][len(yazilacakdizi[i])-1])
    st=st+"\n"
    dosya.write(st)
    st=""
dosya.close()
##################################################################
###################################################################3
dosya=open("sonucK5.txt")
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
yazilacakdizi=[]
for i in range(0,400):
    ortalamatoplamfiyat=0
    artis=0
    for s in range(0,t):
        
        if (int(k[s][len(k[0])-1])==i):
            toplam=toplam+1
            
            tarih=""
            tarihsecmedizi=[]
            for yy in range(0,len(k[s][3])):#tarih kısmını alıyor
                tarihsecmedizi.append(k[s][3][yy])
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
        #print (i," kumenin eleman sayisi == ",toplam)
        yazilacakdizi.append([i,toplam,"BOS"])
    else:
        sonucortalama = artis/(toplam*3)
        #sonucortalama = artis/toplam
        if (sonucortalama<0.0001 and sonucortalama >0):
            #print (i," kumenin eleman sayisi == ",toplam,"-","NOTUR")
            yazilacakdizi.append([i,toplam,"NOTUR"])
        else:
            #print (i," kumenin eleman sayisi == ",toplam,"-",sonucortalama)
            yazilacakdizi.append([i,toplam,sonucortalama])
    toplam=0

dosya=open("totalveriK5.txt","w")
st=""
for i in range(0,len(yazilacakdizi)):
    for k in range(0,len(yazilacakdizi[i])-1):
        st=st+str(yazilacakdizi[i][k])+","
    st=st+str(yazilacakdizi[i][len(yazilacakdizi[i])-1])
    st=st+"\n"
    dosya.write(st)
    st=""
dosya.close()
##################################################################
###################################################################3
dosya=open("sonucK6.txt")
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
yazilacakdizi=[]
for i in range(0,400):
    ortalamatoplamfiyat=0
    artis=0
    for s in range(0,t):
        
        if (int(k[s][len(k[0])-1])==i):
            toplam=toplam+1
            
            tarih=""
            tarihsecmedizi=[]
            for yy in range(0,len(k[s][4])):#tarih kısmını alıyor
                tarihsecmedizi.append(k[s][4][yy])
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
        #print (i," kumenin eleman sayisi == ",toplam)
        yazilacakdizi.append([i,toplam,"BOS"])
    else:
        sonucortalama = artis/(toplam*3)
        #sonucortalama = artis/toplam
        if (sonucortalama<0.0001 and sonucortalama >0):
            #print (i," kumenin eleman sayisi == ",toplam,"-","NOTUR")
            yazilacakdizi.append([i,toplam,"NOTUR"])
        else:
            #print (i," kumenin eleman sayisi == ",toplam,"-",sonucortalama)
            yazilacakdizi.append([i,toplam,sonucortalama])
    toplam=0

dosya=open("totalveriK6.txt","w")
st=""
for i in range(0,len(yazilacakdizi)):
    for k in range(0,len(yazilacakdizi[i])-1):
        st=st+str(yazilacakdizi[i][k])+","
    st=st+str(yazilacakdizi[i][len(yazilacakdizi[i])-1])
    st=st+"\n"
    dosya.write(st)
    st=""
dosya.close()
##################################################################
###################################################################3
dosya=open("sonucK7.txt")
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
yazilacakdizi=[]
for i in range(0,400):
    ortalamatoplamfiyat=0
    artis=0
    for s in range(0,t):
        
        if (int(k[s][len(k[0])-1])==i):
            toplam=toplam+1
            
            tarih=""
            tarihsecmedizi=[]
            for yy in range(0,len(k[s][3])):#tarih kısmını alıyor
                tarihsecmedizi.append(k[s][3][yy])
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
        #print (i," kumenin eleman sayisi == ",toplam)
        yazilacakdizi.append([i,toplam,"BOS"])
    else:
        sonucortalama = artis/(toplam*3)
        #sonucortalama = artis/toplam
        if (sonucortalama<0.0001 and sonucortalama >0):
            #print (i," kumenin eleman sayisi == ",toplam,"-","NOTUR")
            yazilacakdizi.append([i,toplam,"NOTUR"])
        else:
            #print (i," kumenin eleman sayisi == ",toplam,"-",sonucortalama)
            yazilacakdizi.append([i,toplam,sonucortalama])
    toplam=0

dosya=open("totalveriK7.txt","w")
st=""
for i in range(0,len(yazilacakdizi)):
    for k in range(0,len(yazilacakdizi[i])-1):
        st=st+str(yazilacakdizi[i][k])+","
    st=st+str(yazilacakdizi[i][len(yazilacakdizi[i])-1])
    st=st+"\n"
    dosya.write(st)
    st=""
dosya.close()
##################################################################
