# slovarji
"""
slovar = {"ključ" : "vrednost", 
          "ključ2" : "vrednost2"}
print(slovar)
# dostop
print(slovar["ključ"])

# raznoliki slovar
razno = {"stevilo" : 6, 
         "ime" : "Tomas",
          "seznam": [1,2,3,4],
           "slovar": {"firma":"Porchse", "moč": "129kw" }}


print(razno["stevilo"] + 10)
print(razno["slovar"]) #{"firma":"Porchse", "moč": "129kw" }
print(razno["slovar"]["firma"])
"""
#open meteo API

import requests

base_url = "https://api.open-meteo.com/v1/forecast?latitude=46.2248&longitude=14.1721&daily=rain_sum&timezone=Europe%2FBerlin&forecast_days=1"

call = requests.get(base_url).json()
print(call["daily"]["rain_sum"])

#Vaja1 Izpiši trenutno temperaturo.
base_url = "https://api.open-meteo.com/v1/forecast?latitude=46.2248&longitude=14.1721&current=temperature_2m&timezone=Europe%2FBerlin&forecast_days=1"

call = requests.get(base_url).json()
print(call["current"]["temperature_2m"])

#Vaja2 Izpiši temperature za naslednjih 7 dni.
base_url2 = "https://api.open-meteo.com/v1/forecast?latitude=46.2248&longitude=14.1721&daily=temperature_2m_max&timezone=Europe%2FBerlin"
call2 = requests.get(base_url2).json()
print(call2["daily"]["temperature_2m_max"])

#Vaja3 Ugotovi, kateri dan bo najtoplejši oz. najhladnejši, in izpiši datum ter temperaturo.
base_url3 = "https://api.open-meteo.com/v1/forecast?latitude=46.2248&longitude=14.1721&daily=temperature_2m_max,temperature_2m_min&timezone=Europe%2FBerlin" 
call3 = requests.get(base_url3).json()
sez = call(["daily"]["temperature_2m_max"])
sez2 = call(["daily"]["temperature_2m_min"])
najtopljše = 0
najhladnješe = 0
print(sez)
print(sez2)


#Vaja4 Ugotovi, kateri dan ima največjo razliko med dnevno in nočno temperaturo.