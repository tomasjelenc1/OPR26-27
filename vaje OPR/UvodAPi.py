# slovarji

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

#open meteo API
import requests
base_url = "https://api.open-meteo.com/v1/forecast?latitude=46.2248&longitude=14.1721&daily=rain_sum&timezone=Europe%2FBerlin&forecast_days=1"

call = requests.get(base_url).json()
print(call["daily"]["rain_sum"])
