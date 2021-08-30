# coding=utf-8
import requests
import re
from bs4 import BeautifulSoup
import json

html_doc = requests.get("https://so-zou.jp/software/tech/network/domain/ac-jp.htm").text
soup = BeautifulSoup(html_doc, 'lxml') # BeautifulSoupの初期化 html.parserより処理が高速
# print(soup.prettify())

name = soup.find_all('td',text=re.compile(r'大学|大學'))
area = ''
university_domain = []


address = soup.find_all('strong')
for i,n in enumerate(name):
    if 0 <= i <= 7:
        area = '北海道'
    elif 8 <= i <= 14:
        area = '東北'
    elif 15 <= i <= 33:
        area = '関東甲信'
    elif 34 <= i <= 36:
        area = '北陸'
    elif 37 <= i <= 40:
        area = '関東甲信'
    elif 41 <= i <= 43:
        area = '北陸'
    elif 44 <= i <= 51:
        area = '東海'
    elif 52 <= i <= 65:
        area = '近畿'
    elif 66 <= i <= 70:
        area = '中国'
    elif 71 <= i <= 75:
        area = '四国'
    elif 76 <= i <= 86:
        area = '九州'
    elif 87 <= i <= 91:
        area = '北海道'
    elif 92 <= i <= 102:
        area = '東北'
    elif 103 <= i <= 113:
        area = '関東甲信'
    elif 114 <= i <= 116:
        area = '北陸'
    elif 117 <= i <= 119:
        area = '関東甲信'
    elif 120 <= i <= 125:
        area = '北陸'
    elif 126 <= i <= 134:
        area = '東海'
    elif 135 <= i <= 147:
        area = '近畿'
    elif 148 <= i <= 158:
        area = '中国'
    elif 159 <= i <= 162:
        area = '四国'
    elif 163 <= i <= 174:
        area = '九州'
    elif 175 <= i <= 198:
        area = '北海道'
    elif 199 <= i <= 231:
        area = '東北'
    elif 232 <= i <= 462:
        area = '関東甲信'
    elif 463 <= i <= 474:
        area = '北陸'
    elif 475 <= i <= 485:
        area = '関東甲信'
    elif 486 <= i <= 497:
        area = '北陸'
    elif 498 <= i <= 561:
        area = '東海'
    elif 562 <= i <= 685:
        area = '近畿'
    elif 686 <= i <= 721:
        area = '中国'
    elif 722 <= i <= 728:
        area = '四国'
    elif 729 <= i <= 785:
        area = '九州'

    university_domain.append({'name': n.string,'address':address[i].string,'area':area,'school_color':''})
    

# print(university_domain) 
with open('./university.json', 'w') as f:
    json.dump(university_domain, f, ensure_ascii=False, indent=4)
