# -*- coding: cp1254 -*-
def Liste():
    dosya=open("veri[K3].txt")
    x=dosya.readlines()
    t=len(x)
    k=[]
    for i in range(0,t):    
        k.append(x[i].split(","))

    for i in range(0,t): #sondaki /n i�aretini yok etmek ve sistemi satir haline getirmek i�in 
        x=k[i][len(k[0])-1].split()
        k[i][len(k[0])-1]=x[0]
        
    return k
