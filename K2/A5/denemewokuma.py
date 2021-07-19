import WagirlikOkuma
import math
W=WagirlikOkuma.Liste()
girdi = ['28', '36', '130']

habidat2=[]
mindizibul=[]

toplam=0

for l in range(0,400):
    for y in range(0,len(girdi)):
        toplam=toplam+(float(girdi[y])-float(W[y][l]))**2
    mindizibul.append(math.sqrt(toplam))
    #print ("mindizibul[",l,"]","==",math.sqrt(toplam))
    toplam=0

enk=999999999999999999
mind=list(mindizibul)
for p in range(0,len(mindizibul)):
    if mindizibul[p] < enk:
        enk=mindizibul[p]
        indes=p

mindizibul=[]
toplam=0

    


habidat2.append(indes)
