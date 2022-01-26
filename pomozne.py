UROCANJE_STARO_V_NOVO = {}
UROCANJE_NOVO = {}

EFEKT_STARO_V_NOVO = {}
EFEKT_NOVO = {}

DOSEG_STARO_V_NOVO = {}
DOSEG_NOVO = {}

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
