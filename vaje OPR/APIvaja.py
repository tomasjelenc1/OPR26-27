import requests

#API osnovna vaja
imena = ["Svit", "Gaj", "Urban", "Žan"]



for i, imena in enumerate(imena):
    base_url = f"https://api.agify.io?name={imena}"
    call = requests.get(base_url).json()
    print(f"call['name']")
    print(f"call['age']")

















# for each
"""
for i in imena:
    print(i)

# enumerate
print(list(enumerate(imena)))

for i in enumerate(imena):
    print(i, imena)
"""