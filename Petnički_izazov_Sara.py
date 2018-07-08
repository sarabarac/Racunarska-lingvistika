devojka_iz_petnice = "Da je ljubav nauka\ndobio bih Nobela\nA da je ljubav knjiga\nuzeo bih NIN-a\n\nDevojke iz Petnice\nredom su pametnice\nA jedna među njima\nsad moje srce ima\n\nŽelim da sam projekat\ni da sam joj u mislima\nmrtvi Vizantinac\niz srednjeg veka pisac\nželim da sam bitan\nu njenim poslovima\n\nDevojka iz Petnice\nona meni znači sve\ni kada me se seti\nja hoću da poletim\n\nDevojka iz Petnice\nu koju sam zaljubljen\nsad uči tamo negde\nDa li pamti menn\nHoću da sam tema\nU nečemu što sprema\nMrtvi Vizantinac\niz srednjeg veka pisac\nželim da sam bitan\nu njenim poslovima"
konačna=[]

slovca=devojka_iz_petnice.lower()

lista_stihova=slovca.split("\n")


for x in lista_stihova:
    stih=x.split(" ")
    for y in stih:
        konačna.append(y)
print(konačna)
print(len(konačna))

neponovljene=[]
for x in konačna:
    if x not in neponovljene:
        neponovljene.append(x)
print(len(neponovljene))

konačna.sort()

rečnik={i: konačna.count(i) for i in konačna}
print(rečnik)

for k, v in rečnik.items():
     print(k,v)


