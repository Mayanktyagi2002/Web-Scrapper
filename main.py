from operator import length_hint
from tkinter import scrolledtext
from turtle import title
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from random import randint
from time import sleep

source=requests.get('https://getlatka.com');
source.raise_for_status()
header=[]
pages=np.arange(1,50,25)

soup=BeautifulSoup(source.text,'html.parser')
table1=soup.find('table',class_='data-table_table__2P6Tl')

header=[]
for i in table1.find_all('th'):
    title=i.text
    header.append(title)

mydata=pd.DataFrame(columns=header)
#print(mydata)

for page in pages:
    source2=requests.get("https://getlatka.com/?page="+str(page))
    soup2=BeautifulSoup(source2.text,'html.parser')
    table2=soup2.find('tbody')
    sleep(randint(2,8))
    for j in table2.find_all('tr')[0:]:
        row_data=j.find_all('td')
        row=[i.text for i in row_data]
        length=len(mydata)
        mydata.loc[length]=row

#TOCSV=mydata.to_csv('C:\data\company_details.csv')
TOJson=mydata.to_json('C:\data\company_details.json')