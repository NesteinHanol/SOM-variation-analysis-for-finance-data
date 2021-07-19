# -*- coding: cp1254 -*-
# AMAC = [HUCRE1,HUCRE2,TARİH] olarak dosyaya yazdırmak
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
for i in range(0,len(k)-1):
    habidat.append([])

for i in range(0,len(k)-1):
    tarih=""
    tarihsecmedizi=[]
    for s in range(0,len(k[i+1][9])):#tarih kısmını alıyor
        tarihsecmedizi.append(k[i+1][9][s])
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
    habidat[i].append(tarih)

dosya=open("veri2D.txt","w")
st=""
for i in range(0,len(habidat)):
    for k in range(0,len(habidat[i])-1):
        st=st+str(habidat[i][k])+","
    st=st+str(habidat[i][len(habidat[i])-1])
    st=st+"\n"
    dosya.write(st)
    st=""
dosya.close()
