# -*- coding: cp1254 -*-
# AMAC = [HUCRE1,HUCRE2,TARİH] olarak dosyaya yazdırmak
#3,3 kısmı yapılacak yani k4
dosya=open("sonuc1D.txt")
x=dosya.readlines()
t=len(x)
k=[]
for i in range(0,t):    
    k.append(x[i].split(" "))

for i in range(0,t): #sondaki /n işaretini yok etmek ve sistemi satir haline getirmek için 
    x=k[i][len(k[0])-1].split()
    k[i][len(k[0])-1]=x[0]

habidat=[]
habidat2=[]
for i in range(0,len(k)-5):
    habidat.append([])
    habidat2.append([])


import WagirlikOkuma
import WagirlikIsleme
W4=WagirlikOkuma.Liste("W4D.txt")
cc=[]
dd=[]
for i in range(0,len(k)-5):
    tarih=""
    tarihsecmedizi=[]
    for s in range(0,len(k[i+5][9])):#tarih kısmını alıyor
        tarihsecmedizi.append(k[i+5][9][s])
        #["'", '0', '3', '.', '0', '2', '.', '2', '0', '0', '0', "'", ']']
    for r in range(1,11):
        tarih=tarih+str(tarihsecmedizi[r])

##    for p in range(0,len(k2)):
##        if (tarih==k2[p][0]):
##            habidat[i].append(float(k2[p][1]))
##            habidat[i].append(tarih)
##            habidat[i].append(k[i][len(k[i])-1])
##            break 
    
    habidat[i].append(k[i][len(k[0])-1])
    habidat[i].append(k[i+1][len(k[0])-1])
    habidat[i].append(k[i+2][len(k[0])-1])
    habidat[i].append(k[i+3][len(k[0])-1])
    habidat[i].append(k[i+4][len(k[0])-1])
    habidat[i].append(k[i+5][len(k[0])-1])

    #ara deger olarak bolunuyor buradan sonra W agirlik okumasına gonderiliyor
    cc.append(habidat[i][0])
    cc.append(habidat[i][1])
    cc.append(habidat[i][2])
    cc.append(habidat[i][3])
    habidat2[i].append(WagirlikIsleme.WagirlikIsle(cc,W4))
    habidat2[i].append(k[i+4][len(k[0])-1])
    habidat2[i].append(k[i+5][len(k[0])-1])
    
    habidat[i].append(tarih)
    habidat2[i].append(tarih)
    cc=[]
    dd=[]

dosya=open("veri[K2].txt","w")
st=""
for i in range(0,len(habidat2)):
    for f in range(0,len(habidat2[i])-1):
        st=st+str(habidat2[i][f])+","
    st=st+str(habidat2[i][len(habidat2[i])-1])
    st=st+"\n"
    dosya.write(st)
    st=""
dosya.close()
