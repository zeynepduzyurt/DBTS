# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 10:25:22 2018

@author: Zeynep
"""
import requests

from bs4 import BeautifulSoup

'''
#Ay yapim dizileri, dizideki oyuncular ve kanallari..
url = "http://www.wikizeroo.net/index.php?q=aHR0cHM6Ly90ci53aWtpcGVkaWEub3JnL3dpa2kvQXlfWWFwxLFt"

response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")


for i in  soup.find_all("table", {"class": "wikitable sortable"}):
    i=i.text
    i = i.strip()
    print(i)
'''



#yila gore diziler, yapim yillari, turleri

a = float(input("Yili giriniz:"))

def deneme(url):
    response = requests.get(url)
    html_icerigi = response.content

    soup = BeautifulSoup(html_icerigi, "html.parser")

    baslik = soup.find_all("a", {"class": "no_underline"})
    yil = soup.find_all("div", {"class": "oflow_a"})
    tur = soup.find_all("span", {"itemprop": "genre"})


    for baslik, yil, tur in zip(baslik, yil, tur):
        baslik = baslik.text
        yil = yil.text
        tur = tur.text

        baslik = baslik.strip()  # bastaki sondaki bosluklari siler.
        baslik = baslik.replace("\n", "")  # \n yerine bosluk koyar.

        yil = yil.strip()
        yil = yil.replace("\n", "")

        tur = tur.strip()
        tur = tur.replace("\n", "")

        print("Dizi ismi: {} Dizi Baslangic Yili : {} Dizinin Türü :{} ".format(baslik, yil, tur))





if(a == 2010):
    deneme("http://www.beyazperde.com/diziler/en/iyi/ulke-5026/onyil-2010/yila-2010/")
if(a == 2011):
    deneme("http://www.beyazperde.com/diziler/en/iyi/ulke-5026/onyil-2010/yila-2011/")
if(a == 2012):
    deneme("http://www.beyazperde.com/diziler/en/iyi/ulke-5026/onyil-2010/yila-2012/")
if(a == 2014):
    deneme("http://www.beyazperde.com/diziler/en/iyi/ulke-5026/onyil-2010/yila-2014/")
if(a == 2015):
    deneme("http://www.beyazperde.com/diziler/en/iyi/ulke-5026/onyil-2010/yila-2015/")
if(a == 2016):
    deneme("http://www.beyazperde.com/diziler/en/iyi/ulke-5026/onyil-2010/yila-2016/")
if(a == 2017):
    deneme("http://www.beyazperde.com/diziler/en/iyi/ulke-5026/onyil-2010/yila-2017/")
if (a == 2018):
    deneme("http://www.beyazperde.com/diziler/en/iyi/ulke-5026/onyil-2010/yila-2018")















