import re
import orodja

HTML_UROKOV = 'uroki.html'


sola_sl = {'vsebina': 'sola'}
urocanje_sl = {'vsebina': 'urocanje'}
doseg_sl = {'vsebina': 'doseg'}
efekt_sl = {'vsebina': 'efekt'}

SLOVARJI = [sola_sl, urocanje_sl, doseg_sl, efekt_sl]

def ocisti_niz(string):
    '''V nizu zbriše znaka '"' in ',' saj tedva ne nosita velike pomenske vloge. 
    Poleg tega zbriše tudi 's' na koncu, ker je ta v dobljenih podatkih nedosledno uporabljen.'''
    ociscen = string.lower()
    while '"' in ociscen:
        ociscen = ociscen.replace('"', '')
    while ',' in ociscen:
        ociscen = ociscen.replace(',', '')
    if ociscen[-1] == 's':
        return ociscen[:-1]
    else:
        return ociscen

skupek_urokov_po_stopnji = re.compile(
    r'<div id="wiki-tab-0-(?P<stopnja>\d)".*?><div class="list-pages-box">(?P<vsebina>.*?)'
    r'<\/div>\s*<\/div>',
    flags=re.DOTALL
)

vzorec_bloka = re.compile(
    r'<tr>\s*<td><a href.*?<\/tr>',
    flags=re.DOTALL
)

vzorec_uroka = re.compile(
    r'<a href="/spell:(?P<urok_href>.*?)">(?P<urok>.*?)</a></td>\s*'
    r'<td><em>(?P<sola>.+?)</em></td>\s*'
    r'<td>(?P<urocanje>.+?)</td>\s*'
    r'<td>(?P<doseg>.+?)</td>\s*'
    r'<td>(?P<efekt>.+?)</td>\s*'
    r'<td>(?P<potrebscine>.+?)</td>'
)

def vrni_uroke_po_stopnji():
    izvorna_datoteka = 'uroki.html'
    vsebina_datoteke = orodja.vsebina_datoteke(izvorna_datoteka)
    uroki = []
    for ujemanje in skupek_urokov_po_stopnji.findall(vsebina_datoteke):
        uroki.extend(vrni_uroke(ujemanje[0], ujemanje[1]))
    return uroki

def vrni_uroke(stopnja, vsi_na_kupu):
    uroki = []
    for blok in vzorec_bloka.findall(vsi_na_kupu):
        uroki.append(prebavi_urok(blok, stopnja))
    return uroki

def prebavi_urok(blok, stopnja):
    urok = vzorec_uroka.search(blok).groupdict()
    urok['ritual'] = len(urok['urocanje'].split(' <em><sup>')) >= 2 and 'R' in urok['urocanje'].split()[-1]
    # določimo kodo šole čaranje
    sola_t = (urok['sola'].split()[0], sola_sl)
    urocanje_t = (urok['urocanje'].split(' <em><sup>')[0], urocanje_sl)
    doseg_t = (urok['doseg'], doseg_sl)
    efekt_t = (urok['efekt'], efekt_sl)
    for nekaj, slovar in [sola_t, urocanje_t, doseg_t, efekt_t]:
        nekaj = ocisti_niz(nekaj)
        if nekaj not in slovar.keys():
            slovar[nekaj] = len(slovar)
        urok[slovar['vsebina']] = slovar[nekaj]
    potrebscine = urok.pop('potrebscine')
    urok['verbal'] = 'V' in potrebscine
    urok['somatic'] = 'S' in potrebscine
    urok['material'] = 'M' in potrebscine
    urok['stopnja'] = int(stopnja)
    return urok
    
   
prebavljeni_uroki = []
prebavljeni_uroki.extend(vrni_uroke_po_stopnji())
print(f'Prebavil sem {len(prebavljeni_uroki)} urokov!')

orodja.zapisi_json(prebavljeni_uroki, 'podatki/uroki.json')
for slovar in SLOVARJI:
    naslov = f"podatki/{ slovar.get('vsebina') }.json"
    orodja.zapisi_json(slovar, naslov)

orodja.zapisi_csv(prebavljeni_uroki, ['urok_href', 'urok', 'sola', 'urocanje', 'doseg', 'efekt', 'ritual', 'verbal', 'somatic', 'material', 'stopnja'], 'podatki/uroki.csv')
for slovar in SLOVARJI:
    naslov = f"podatki/{ slovar.get('vsebina') }.csv"
    a = list(slovar.keys())
    a.remove('vsebina')
    slvcsv = []
    for el in a:
        sl = {}
        sl['ime'] = el
        sl['id'] = slovar[el]
        slvcsv.append(sl)
    orodja.zapisi_csv(slvcsv, ['ime', 'id'], naslov)