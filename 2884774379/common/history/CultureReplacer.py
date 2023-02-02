import os

# AFRICA
COUNTRY_PATH = "D:\\SteamLibrary\\steamapps\\workshop\\content\\529340\\2884774379\\common\\history\\input_country_definitions"
OUTPUT_COUNTRY_PATH = "D:\\SteamLibrary\\steamapps\\workshop\\content\\529340\\2884774379\\common\\country_definitions"
POPS_PATH = "D:\\SteamLibrary\\steamapps\\common\\Victoria 3\\game\\common\\history\\pops"
OUTPUT_POPS_PATH = "D:\\SteamLibrary\\steamapps\\workshop\\content\\529340\\2884774379\\common\\history\\pops"
CULTURES_TO_CONVERT_AFRICA = ['akan', 'senufo','dyula','kru','fulbe','wolof','bambara',
'kissi','mossi','hausa','songhai','yoruba','equatorial_bantu',' edo','ibo','tiv','fon',
'ibibio','kanuri','ewe','unyamwezi','chewa','yao','makua','lacustrine_bantu',
'sukuma','luo','ruanda','rundi','maasai','kikuyu','nilotic','afar','somali','mande',
'lunda','sena','chewa','nguni','baganda','dinka','nuba','azande','lomwe','fur','baguirmi',
'sara','fang','tswana','khoisan','nguni','fluvian_bantu','bakongo','kavango_bantu',
'ovimbundu','herero','tonga','nuer','luba','shona','sotho','xhosa','zulu']
CULTURES_TO_CONVERT_AMERICA = ['quechua','amazonian','guajiro','muisca','aimara','guarani',
'patagonian','miskito','cariban','tarascan','inuit','athabaskan','metis',
'caribeno','cajun','iroquoian','salish','paiute','nez_perce','siouan','apache',
'dakota','caddoan','cherokee','algonquian','muskogean','navajo','hawaiian','cree',
'oodham','comanche','apache','pueblo','hokan','zapotec','nahua','mixtec','mayan']
CULTURES_TO_CONVERT_INDONESIA = ['dayak','bornean','moro','hakka','javan','sumatran',
'batak','melanesian','moluccan','balinese','moro','filipino','polynesian','micronesian','melanesian']
CULTURES_TO_CONVERT_N_AFRICA = ['tuareg','maures','haratin','teda']
CULTURES_TO_CONVERT_AMERICA_AFRICA = ['afro_antillean','afro_caribbean','afro_caribeno']

if __name__ == '__main__':
    for fo in os.listdir(COUNTRY_PATH):
        newCountryFile = open(OUTPUT_COUNTRY_PATH + '/' + fo, 'w')
        countryFile = open(COUNTRY_PATH + '/' + fo)
        countryFile = countryFile.read()
        for x in CULTURES_TO_CONVERT_AFRICA:
            countryFile = countryFile.replace(x, 'africana')
        for y in CULTURES_TO_CONVERT_N_AFRICA:
            countryFile = countryFile.replace(y, 'berber')
        for z in CULTURES_TO_CONVERT_AMERICA:
            countryFile = countryFile.replace(z, 'nativa')
        for w in CULTURES_TO_CONVERT_INDONESIA:
            countryFile = countryFile.replace(w, 'malay')
        for d in CULTURES_TO_CONVERT_AMERICA_AFRICA:
            countryFile = countryFile.replace(d, 'afro_american')
        for a in ['maori']:
            countryFile = countryFile.replace(a, 'aborigine')
        for b in [' beja']:
            countryFile = countryFile.replace(b, 'sudanese')
        for c in ['amhara','tigray','sidama']:
            countryFile = countryFile.replace(c, 'oromo')
        for e in ['mongo\n', ' malagasy']:
            countryFile = countryFile.replace(e, 'africana\n')
        newCountryFile.write(countryFile)
    for f in os.listdir(POPS_PATH):
        newPopFile = open(OUTPUT_POPS_PATH + '/' + f, 'w')
        popFile = open(POPS_PATH + '/' + f)
        popFile = popFile.read()
        for x in CULTURES_TO_CONVERT_AFRICA:
            popFile = popFile.replace(x, 'africana')
        for y in CULTURES_TO_CONVERT_N_AFRICA:
            popFile = popFile.replace(y, 'berber')
        for z in CULTURES_TO_CONVERT_AMERICA:
            popFile = popFile.replace(z, 'nativa')
        for w in CULTURES_TO_CONVERT_INDONESIA:
            popFile = popFile.replace(w, 'malay')
        for d in CULTURES_TO_CONVERT_AMERICA_AFRICA:
            popFile = popFile.replace(d, 'afro_american')
        for a in ['maori']:
            popFile = popFile.replace(a, 'aborigine')
        for b in [' beja']:
            popFile = popFile.replace(b, 'sudanese')
        for c in ['amhara','tigray','sidama']:
            popFile = popFile.replace(c, 'oromo')
        for e in ['mongo\n', 'malagasy']:
            popFile = popFile.replace(e, 'africana\n')
        newPopFile.write(popFile)
