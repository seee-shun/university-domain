# coding=utf-8
import requests
import re
from bs4 import BeautifulSoup

html_doc = requests.get("https://so-zou.jp/software/tech/network/domain/ac-jp.htm").text
soup = BeautifulSoup(html_doc, 'html.parser') # BeautifulSoupの初期化
# print(soup.prettify())

university_domain = []
name = soup.find_all('td',text=re.compile('大学'))
area = ''
domain = '.ac.jp'

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
    
    jp_pattern = re.compile(r'奈良先進科学技術大学大学院|北海学園大学|弘前医療福祉大学|尚絅学院大学|仙台大学|東北文教大学|日本ウェルネススポーツ大学|白鴎大学|聖学院大学|日本薬科大学|聖徳大学|神奈川工科大学|横浜薬科大学|高千穂大学|玉川大学|玉川大学|東洋学園大学|日本教育大学院大学|早稲田大学|身延山大学|清泉女学院大学|岐阜女子大学|名古屋学院大学|びわこ成蹊スポーツ大学|京都医療科学大学|立命館大学|大阪成蹊大学|大阪総合保育大学|奈良学園大学|吉備国際大学|広島経済大学|宇部フロンティア大学|沖縄科学技術大学院大学')
    lg_jp_pattern = re.compile(r'千葉県立保健医療大学')
    net_pattern = re.compile(r'富士大学|愛知産業大学')
    com_pattern = re.compile(r'聖カタリナ大学')
    ac_pattern = re.compile(r'ビジネス・ブレークスルー大学')

    if bool(jp_pattern.search(n)):
        domain = '.jp'
    elif bool(lg_jp_pattern.search(n)):
        domain = '.lg.jp'
    elif bool(net_pattern.search(n))
        domain = '.net'
    elif bool(com_pattern.search(n)):
        domain = '.com'
    elif bool(ac_pattern.search(n)):
        domain = '.ac'

    university_domain.append({'name': n.string,'address':'@' + address[i].string + domain,'area':area,'school_color':''})
    

# print(university_domain) 
# TODO2 このページのaタグをすべて抜き出してください。(HTMLの内容)

# for tag in real_page_tags:
#     print(tag.string)

# elems = soup('#g-contents > table:nth-of-type(6) > tbody > tr:nth-of-type(2) > td:nth-of-type(1)')
# print(elems)
# TODO3 このページのaタグをすべて抜き出してください。(HTMLの内容)

# for tag in real_page_tags:
#     print(tag.get("href")) 
#g-contents > table:nth-child(6) > tbody > tr:nth-child(2) > td:nth-child(1)