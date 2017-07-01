# -*- coding: utf-8 -*-
x = "loš"
y= "miloš"
z = "dobar"

print(x in y)
print(z in y)


lista_brojeva = [1, 2, 2.5]
lista_niski = ["ovo", "je", "lista", "niski", "ova", "lista", "je", "kul"]
lista_svega = [True, "može", "i", "ovo", 5.0, [1, 2, "tri"]]

print(lista_brojeva[2])
print(lista_niski[0])
print(lista_svega[-1])
print(lista_svega[-1][2])

print(lista_brojeva)
lista_brojeva[2] = 3
print(lista_brojeva)


print(lista_svega)
lista_svega.append("ćušpajz") # dodaje element na kraj liste
print(lista_svega)
lista_svega.insert(2, "brokoli") # dodaje element pod indeks koji je određen (u ovom slučaju pod indeks 2)
print(lista_svega)


print(lista_niski)
skup = set(lista_niski)
print(skup)   

print(skup_niski)
skup_niski.add("razumeš")


