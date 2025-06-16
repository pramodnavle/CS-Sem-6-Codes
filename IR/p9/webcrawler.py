#AIM:Write a program to implement simple web crawler.

import requests
from bs4 import BeautifulSoup
def web(page,WebUrl):
    if(page>0):
        url=WebUrl
        code=requests.get(url)
        plain=code.text
        
        s=BeautifulSoup(plain,"html.parser")
        for link in s.findAll('li'):
            tet=link.getText()
            print(tet)
            print(link)
            print()
            
web(1,"https://www.moneycontrol.com/")
