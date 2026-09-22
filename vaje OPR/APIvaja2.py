
import requests

base_url = "https://opentdb.com/api.php?amount=10&category=12&type=multiple"

call = requests.get(base_url).json()
rez = call["results"]

for r in rez:
    vprašanje = r["question"]
    pravilen = (r["correct_answer"])
    nepravilen = (r["incorrect_answers"])
    odgovori = [pravilen] + nepravilen

    print(vprašanje)
    print(odgovori)
    odgovor = input("Oddaj svoj odgovor: ")

    if odgovor == pravilen: 
        print("Odgovor je pravilen.")

    else:
        print(f"Odgovor je nepravilen. Pravilni odgovor je {pravilen}")

    print("-------------------------------------------")