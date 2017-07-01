# -*- coding: utf-8 -*-

niska = "Milena je sinoć videla Mitra, nežnog, zelenog skakavca ispred stacionara i uzviknula je: \"Ju, Mitre, uplašio si me!\". Ali Mitar se na to nije obazirao - žustro je skočio u Mileninom pravcu. Videvši to, Milena polete preko dvorišta i polete ka stacionaru brzinom svetlosti. Nažalost, svetlost je brža od automatskog mehanizma za otvaranje vrata. I tako ostade Milenin trag na ulaznim vratima IS Petnica."
niska = niska.lower()
reči = niska.split(" ")
print(reči)

reči[4] = reči[4][:-1]
reči[5]= reči[5][:-1]
reči[12] = reči[12][0:2]
reči[13] = reči[13][1:-1]
reči[14] = reči[14][0:-1] 
reči[17] = reči[17][0:2]
reči[43] = reči[43][0:7]
reči[44] = reči[44][0:8]
reči[53] = reči[53][0:5]
reči[63] = reči[63][0:7]


telefonski_imenik = {"Paja Patak": 123456, "Mini Maus": 234567, "Šilja": 345678}
vukajlija = {"sojanica": "Posna pljeskavica. Garantovano bez trihinele.", "jahanje": "Omiljena aktivnost šefova za koju je potrebno da radnik ima konjske živce.", "šef": "Čovek koji nema smisao za umor."}
vrste_reči = {"imenice": ["polaznik", "seminar", "lingvistika", "Isidora"], "glagoli": ["slušati", "crtati", "jesti"], "zamenice": ["on", "ona", "ono"]}

print(telefonski_imenik["Mini Maus"])
print(vrste_reči["imenice"])
print(vukajlija["šef"])


vukajlija["šef"] = "Miloš"
print(vukajlija)
print(vukajlija["Miloš"])


print(telefonski_imenik.keys())
print(vrste_reči.values())


print(vrste_reči["imenice"][2])

