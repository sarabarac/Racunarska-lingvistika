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
#strip=ukloni mi  simbole sa kraja reči ako ih pronađeš
#remove je element koji želimo ukloniti

#da bi se izbegli razmaci, for x in lista_stihova:
    #
#for petlja se može zameniti i jednim reodm: neponovljene=set(konačna)

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


dečak=[]
for i in devojka_iz_petnice:
    if i=="Devojke":
        i="Dečaci"
    if i=="Devojka":
        i="Dečak"
    if i=="joj":
        i="mu"
    if i=="mrtvi":
        i="mrtva"
    if i=="Mrtvi":
        i="Mrtva"
    if i=="njenim":
        i="njegovim"
    if i=="koju":
        i="kojeg"
    if i=="ona":
        i="on"
    
    if i.endswith("io")==True:
        i=i.replace("io","ila")
    if i.endswith("eo")==True:
        i=i.replace("eo","ela")
    if (i.endswith("ac")==True) and (i!=("pisac")):
        i=i.replace("ac","ka")
    if i.endswith("an")==True:
        i=i.replace("an","na")
    else:
        if (i.endswith("na")==True):
            i=i.replace("na","an")
    if i.endswith("en"):
        i=i.replace("en","ena")
    dečak.append(i)
    
rečnik2=' '

    
    
    
    
    
    
    