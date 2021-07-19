# -*- coding: cp1254 -*-
##import urllib2
##import re
##htmlfile=urllib2.urlopen("https://www.investing.com/commodities/copper")
##htmltext=htmlfile.read()
##
##regex='<span class="arial_26 inlineblock pid-8831-last" id="last_last" dir="ltr">(.+?)</span>'
##pattern = re.compile(regex)
##price = re.findall(pattern,htmltext)


import urllib2
import re

url = "https://www.investing.com/commodities/copper"
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

req = urllib2.Request(url, headers=headers)

response = urllib2.urlopen(req)

your_json = response.read()
response.close()

regex='<span class="arial_26 inlineblock pid-8831-last" id="last_last" dir="ltr">(.+?)</span>'
pattern = re.compile(regex)
price = re.findall(pattern,your_json)

import time
#time.sleep(3600) 1 saat demek
#s=x[0]+x[2]+x[3]+x[4]+"."+x[6]+x[7] alt�n i�in gelen deger duzenle
#hepsi icin amerikan sunucusundan cek


##import smtplib                           #smtplib modulunu projemize ekledik
### Hesap bilgilerimiz
##kullan�c�="gmailadresimiz@gmail.com"
##kullan�c�_sifresi = 'gmailsifremiz'
##al�c� = 'g�nderilen@mail.com'            # al�c�n�n mail adresi
##konu = 'Selam'
##msj = 'Naber!'
### bilgileri bir metinde derledik
##email_text = """
##From: {}
##To: {}
##Subject: {}
##{}
##""" .format(kullan�c�,al�c�, konu, msj)
##try:
##server = smtplib.SMTP('smtp.gmail.com:587')   #servere ba�lanmak i�in gerekli host ve portu belirttik
##server.starttls() #serveri TLS(b�t�n ba�lant� �ifreli olucak bilgiler korunucak) ba�lant�s� ile ba�latt�k
##server.login(kullan�c�, kullan�c�_sifresi)   # Gmail SMTP server'�na giri� yapt�k
##server.sendmail(kullan�c�, al�c�, email_text) # Mail'imizi g�nderdik 
##server.close()     # SMTP serverimizi kapatt�k
##print ('email g�nderildi')
##except:
##print("bir hata olu�tu")
