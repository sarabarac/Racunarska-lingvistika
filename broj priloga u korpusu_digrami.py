# -*- coding: utf-8 -*-
brojPriloga = 0
prilozi = ["ovde", "tamo", "tu", "desno", "negde"]
korpus = "Ovde mi je baš lepo. Džunglu ne volim. Ne bih volela da sam tamo. Moje mesto je tu. Tu se osećam kao da sam kod kuće. Stavila sam svoju šoljicu kafe desno, e baš tu."

tokeniziraniKorpus = korpus.split(" ")

for reč in tokeniziraniKorpus:
    # prebacivanje reči u mala slova
    reč = reč.lower()
    # uklanjanje interpunkcijskih znaka
    reč = reč.strip(",.")
    if reč in prilozi:
        brojPriloga += 1 # brojPriloga = brojPriloga + 1
    
    if reč in "prilozi":
        brojPriloga =+ 1
print(brojPriloga)




korpus = "Ovaj korpus sam sastavljala dok je Isidora sedela u kancelariji i puštala pesme benda The National. Pitala me je da li mi se bend sviđa i rekla je da ona misli da je to super muzika za preko dana. Pošto bukvalno više nemam ideja šta da kucam ovde, nastaviću da ispisujem šta se sve nalazi oko mene. Levo od mene su dva tanjira koje je Milena oprala. Deluju čisto. S leve strane računara nalazi se tirkizni lak čije je ime u stvari Green. Nije mi baš najjasnije ko tu ne vidi boje. S desne strane računara nalazi se providni lak, ali je bočica obojena u crno, pa je Tijana zbog toga prošlog seminara mislila da je crn. Nejasni su mi proizvođači lakova. "

korpus = korpus.lower()
digrami = list()

for i in range(len(korpus)):
   digram = korpus[i:i+2]
   digrami.append(digram)

print(digrami)
print(set(digrami))

ttr = len(set(digrami))/len(digrami)
print(ttr)


