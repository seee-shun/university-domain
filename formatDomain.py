import json
import re

json_file = open('./university.json','r')
json_dict = json.load(json_file)

university_domain = [];
domain = '.ac.jp'
jp_pattern = re.compile(r'奈良先端科学技術大学院大学|北海学園大学|弘前医療福祉大学|尚絅学院大学|仙台大学|東北文教大学|日本ウェルネススポーツ大学|白鴎大学|聖学院大学|日本薬科大学|聖徳大学|神奈川工科大学|横浜薬科大学|高千穂大学|玉川大学|玉川大学|東洋学園大学|日本教育大学院大学|早稲田大学|身延山大学|清泉女学院大学|岐阜女子大学|名古屋学院大学|びわこ成蹊スポーツ大学|京都医療科学大学|立命館大学|大阪成蹊大学|大阪総合保育大学|奈良学園大学|吉備国際大学|広島経済大学|宇部フロンティア大学|沖縄科学技術大学院大学')
pref_lg_jp_pattern = re.compile(r'千葉県立保健医療大学')
net_pattern = re.compile(r'富士大学|愛知産業大学')
com_pattern = re.compile(r'聖カタリナ大学')
ac_pattern = re.compile(r'ビジネス・ブレークスルー大学')
web_ac_pattern = re.compile(r'札幌医科大学')
u_ac_pattern = re.compile(r'山形県立米沢栄養大学')
puhs_ac_pattern = re.compile(r'香川県立保健医療大学')
cc_ac_pattern = re.compile(r'桐蔭横浜大学')
gakuin_ac_pattern = re.compile(r'大妻女子大学')
gwc_ac_pattern = re.compile(r'学習院女子大学')
mba_ac_pattern = re.compile(r'グロービス経営大学院大学')
daigaku_ac_pattern = re.compile(r'白梅学園大学')
office_ac_pattern = re.compile(r'東京女子大学')
atom_ac_pattern = re.compile(r'東京電機大学')
college_ac_pattern = re.compile(r'日本医科大学')
bwu_ac_pattern = re.compile(r'文化学園大学')
univ_ac_pattern = re.compile(r'ヤマザキ学園大学|藍野大学|大阪成蹊大学')
suwa_ac_pattern = re.compile(r'諏訪東京理科大学')
uv_ac_pattern = re.compile(r'成美大学')
dwc_ac_pattern = re.compile(r'同志社女子大学')
ouc_ac_pattern = re.compile(r'大阪商業大学')
yg_ac_pattern = re.compile(r'神戸女子大学')
st_ac_pattern = re.compile(r'聖トマス大学')

for val in json_dict:
    if (jp_pattern.search(val['name']) != None):
        val['address'] = '@' + val['address'] + '.jp'
        print(val)
    elif (pref_lg_jp_pattern.search(val['name']) != None):
        val['address']  = '@pref.' + val['address'] + '.lg.jp'
        print(val)
    elif (net_pattern.search(val['name']) != None):
        val['address']  = '@' + val['address'] + '.net'
        print(val)
    elif (com_pattern.search(val['name']) != None):
        val['address']  = '@' + val['address'] + '.com'
        print(val)
    elif (ac_pattern.search(val['name']) != None):
        val['address']  = '@' + val['address'] + '.ac'
        print(val)
    elif (web_ac_pattern.search(val['name']) != None):
        val['address']  = '@web.' + val['address'] + '.ac.jp'
        print(val)
    elif (u_ac_pattern.search(val['name']) != None):
        val['address']  = '@u.' + val['address'] + '.ac.jp'
        print(val)
    elif (puhs_ac_pattern.search(val['name']) != None):
        val['address']  = '@' + val['address'] + '-puhs.ac.jp'
        print(val)
    elif (cc_ac_pattern.search(val['name']) != None):
        val['address']  = '@cc.' + val['address'] + '.ac.jp'
        print(val)
    elif (gakuin_ac_pattern.search(val['name']) != None):
        val['address']  = '@gakuin.' + val['address'] + '.ac.jp'
        print(val)
    elif (gwc_ac_pattern.search(val['name']) != None):
        val['address']  = '@gwc.' + val['address'] + '.ac.jp'
        print(val)
    elif (mba_ac_pattern.search(val['name']) != None):
        val['address']  = '@mba.' + val['address'] + '.ac.jp'
        print(val)
    elif (daigaku_ac_pattern.search(val['name']) != None):
        val['address']  = '@daigaku.' + val['address'] + '.ac.jp'
        print(val)
    elif (office_ac_pattern.search(val['name']) != None):
        val['address']  = '@office.' + val['address'] + '.ac.jp'
        print(val)
    elif (atom_ac_pattern.search(val['name']) != None):
        val['address']  = '@atom.' + val['address'] + '.ac.jp'
        print(val)
    elif (college_ac_pattern.search(val['name']) != None):
        val['address']  = '@college.' + val['address'] + '.ac.jp'
        print(val)
    elif (bwu_ac_pattern.search(val['name']) != None):
        val['address']  = '@bwu.' + val['address'] + '.ac.jp'
        print(val)
    elif (univ_ac_pattern.search(val['name']) != None):
        val['address']  = '@univ.' + val['address'] + '.ac.jp'
        print(val)
    elif (suwa_ac_pattern.search(val['name']) != None):
        val['address']  = '@suwa.' + val['address'] + '.ac.jp'
        print(val)
    elif (uv_ac_pattern.search(val['name']) != None):
        val['address']  = '@uv.' + val['address'] + '.ac.jp'
        print(val)
    elif (dwc_ac_pattern.search(val['name']) != None):
        val['address']  = '@dwc.' + val['address'] + '.ac.jp'
        print(val)
    elif (ouc_ac_pattern.search(val['name']) != None):
        val['address']  = '@ouc.' + val['address'] + '.ac.jp'
        print(val)
    elif (yg_ac_pattern.search(val['name']) != None):
        val['address']  = '@yg.' + val['address'] + '.ac.jp'
        print(val)
    elif (st_ac_pattern.search(val['name']) != None):
        val['address']  = '@st.' + val['address'] + '.ac.jp'
        print(val)
    else:
        val['address']  = '@' + val['address'] + '.ac.jp'
        # print(val)
    university_domain.append({'name': val['name'],'address':val['address'],'area':val['area'],'school_color':''})


with open('./formatUniversity.json', 'w') as f:
    json.dump(university_domain, f, ensure_ascii=False, indent=4)