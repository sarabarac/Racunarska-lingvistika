# -*- coding: utf-8 -*-
lavica = 0
tigrica = 0
sve_reci = set()



korpus = "Juče sam bio u zoo vrtu. Video sam tri lava i bila je tu jedna lavica. Lavica nije imala grivu, jer to imaju samo muški lavovi. Bila je u zoo vrtu i jedna tigrica. Ona je imala jako lepo krzno. Bilo mi je žao što tigrica i lavica ne mogu da se druže, jer mislim da bi se baš lepo slagale pošto su obe mačke."

tokeniziraniKorpus = korpus.split(" ")
print(tokeniziraniKorpus)

for reč in tokeniziraniKorpus:
    # prebacivanje reči u mala slova
    reč = reč.lower()
    # uklanjanje interpunkcijskih znakova
    reč = reč.strip(",.") #strip je komanda za uklananje interpunkcije sa desne strane
    
    sve_reci.add(reč)
    

    if reč == "lavica":
        lavica += 1 # lavica = lavica + 1
    elif reč == "tigrica":
        tigrica += 1 # tigrica = tigrica + 1
        


print("Broj javljanja reči lavica:", lavica) 
print("Broj javljanja reči tigrica:", tigrica)

print(len(sve_reci))





