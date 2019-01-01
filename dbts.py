

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 11:55:40 2018

@author: Zeynep
"""

import numpy as np
import pandas as pd 



#2.veri onisleme

dizi = pd.read_csv('tumveriler.csv')
print(dizi) 

#deneme = dizi.corr()


#Giris Degerleri icin sutunlar ayrildi,degiskenler olusturuldu
ortsure = pd.DataFrame(dizi.iloc[:,2:3].values, columns=['Ort Sure'])
diziadi = pd.DataFrame(dizi.iloc[:,0:1].values, columns=['Dizi Adi'])
yapimci = pd.DataFrame(dizi.iloc[:,5:6].values)
senarist = pd.DataFrame(dizi.iloc[:,6:7].values)
yapimsirketi = pd.DataFrame(dizi.iloc[:,4:5].values)
yayinkanali = pd.DataFrame(dizi.iloc[:,3:4].values)
oyuncupuanlari = pd.DataFrame(dizi.iloc[:,8:11].values)
diziadi = dizi['Dizi Adi']
turler = pd.DataFrame(dizi.iloc[:,-6:-5].values)
baslangicyili = dizi['Baslangic Yili']
bitisyili = dizi['Bitis Yili']
ihracdurumu = dizi['ihrac durumu']

#cikis degerleri
sezonbolumsayisi = pd.DataFrame(dizi.iloc[:,-4:-2].values,columns=['Sezon Sayisi','Bolum Sayisi'])
basari = pd.DataFrame(dizi.iloc[:,-1:].values, columns=['Basari'])
ihracdurumu = pd.DataFrame(dizi.iloc[:,-2:-1].values, columns=['İhraç durumu'])



#sayisal degere donusturulur.
from sklearn.preprocessing import LabelEncoder

yayinkanali = yayinkanali.apply(LabelEncoder().fit_transform)
yapimsirketi = yapimsirketi.apply(LabelEncoder().fit_transform)
senarist = senarist.apply(LabelEncoder().fit_transform)
yapimci = yapimci.apply(LabelEncoder().fit_transform)
turler = turler.apply(LabelEncoder().fit_transform)


ihracdurumu = ihracdurumu.apply(LabelEncoder().fit_transform)
print(ihracdurumu) 

dizi['Senarist'].value_counts()
dizi['Yapim sirketi'].value_counts()
dizi['Yayinci Kuruluslar'].value_counts()


'''tür,yayın kanalı, yapim sirketi kategorik oldugundan onehotencoder ile veriler duzenlendi.'''
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(categorical_features='all')

senarist = ohe.fit_transform(senarist).toarray()
yapimsirketi = ohe.fit_transform(yapimsirketi).toarray()
turler=ohe.fit_transform(turler).toarray()

yayinkanali = ohe.fit_transform(yayinkanali).toarray()
yapimci = ohe.fit_transform(yapimci).toarray()


#concat fonksiyonu kullanabılmek ıcın dataframe turune cevirdim.
yapimci = pd.DataFrame(data = yapimci, index = range(182))
senarist = pd.DataFrame(data = senarist, index = range(182))
yapimsirketi = pd.DataFrame(data = yapimsirketi, index = range(182))
print(yapimsirketi)

yayinkanali = pd.DataFrame(data = yayinkanali, index = range(182), columns = ['ATV','Fox Tv','Kanal D','Star Tv','Show Tv','TRT1','TV 8'])
print(yayinkanali)
turler =pd.DataFrame(data = turler, index = range(182), columns = ['Aksiyon','Ask','Dram','Fantastik','Genclik','Komedi','Polisiye','Romantik','Romantik komedi','Tarih'])
print(turler)
dizi['Turler'].value_counts() #turler kolonundaki farklı degerlerın sayılarını gosterır.


#verileri onislemeden sonra birlestirme islemi. 
xveri=pd.concat([diziadi,baslangicyili,ortsure,senarist,yapimsirketi,yapimci,turler,yayinkanali,bitisyili,sezonbolumsayisi,basari,ihracdurumu],axis=1)


a = int(input("Dizi adina göre tahmin yapmak için 1, yıla göre tahmin yapmak için 0 yazınız."))
if(int(a) == 0):
 
    yil = int(input("Tahmin etmek istediginiz yılı giriniz."))
    testveri=xveri[xveri['Baslangic Yili'] == yil]
    egitimveri=xveri[xveri['Baslangic Yili'] < yil] 
    xegitim = pd.DataFrame(egitimveri.iloc[:,1:-5].values)
    yegitim = pd.DataFrame(egitimveri.iloc[:,-5:].values, columns=['Bitis Yili','Sezon Sayisi','Bolum Sayisi','Basari Durumu','Ihrac Durumu'])
    xtest = pd.DataFrame(testveri.iloc[:,1:-5].values)
    ytest = pd.DataFrame(testveri.iloc[:,-5:].values, columns=['Bitis Yili','Sezon Sayisi','Bolum Sayisi','Basari Durumu','Ihrac Durumu'])
    
if(int(a) == 1):
     
     adi = (input("Tahmin etmek istediginiz dizi adi giriniz."))
     testdiziadiveri=xveri[xveri['Dizi Adi'] == adi]
     tarih= int(testdiziadiveri[['Baslangic Yili']].values)
     egitimveri=xveri[xveri['Baslangic Yili'] < tarih]
     xegitim = pd.DataFrame(egitimveri.iloc[:,1:-5].values)
     yegitim = pd.DataFrame(egitimveri.iloc[:,-5:].values, columns=['Bitis Yili','Sezon Sayisi','Bolum Sayisi','Basari Durumu','Ihrac Durumu'])
     xtest = pd.DataFrame(testdiziadiveri.iloc[:,1:-5].values)
     ytest = pd.DataFrame(testdiziadiveri.iloc[:,-5:].values, columns=['Bitis Yili','Sezon Sayisi','Bolum Sayisi','Basari Durumu','Ihrac Durumu'])
     xtestdiziadi= pd.DataFrame(testdiziadiveri.iloc[:,0:1])
     
from sklearn.neighbors import KNeighborsClassifier
neighbors = KNeighborsClassifier(n_neighbors=5)
neighbors.fit(xegitim, yegitim) 
neighborspred= neighbors.predict(xtest)
print(neighborspred)  
     


from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier(criterion = 'gini')
dtc.fit(xegitim,yegitim)
dtcpred = dtc.predict(xtest) 





