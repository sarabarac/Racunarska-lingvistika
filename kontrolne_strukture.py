# -*- coding: utf-8 -*-


x = 2
y = 3

if x < 5:
    x = x + 2 # x += 2
else:
    y = y + 1 # y += 1

print(x, y)   


a = 5
b = 4
c= 5

if a < b:
    print("Ovo ispisujem ako je a manje od b")
elif a > b:
    print("Ovo ispisujem ako je a veće od b")
else:
    print("Ovo ispisujem slučajevima, tj. ako je a jednako b")

 if (a == b) and (c > b ):
     print("If je ispunjen")
     
else :
    print( "If nije ispunjen")
    
    
    
a = 72
b = 9
c = 23

if a < b:
    if a < c:
        print("Ovo ispisujem ako je a manje od b i ako je a manje od c")
    else:
        print("Ovo ispisujem ako je a manje od b i ako a nije manje od c")

if a < b:
    if a < c:
        print("Ovo ispisujem ako je a manje od b i ako je a manje od c")
else:
    print("Ovo ispisujem ako a nije manje od b")
     
    


x = 2
y = 3

while x < 5:
    y = y * 2 # y *= 2
    x = x + 1 # x += 1

print(x, y)



for i in range(0,10):
    print("ponavljam se")
    
mlSaradnici = ["Milena", "Milan", "Jovana", "Tijana", "Isidora"]
for saradnik in mlSaradnici:
    print(saradnik)    



 for i in range(0,10,-3):
     print(i)

 for o in range(10,0,-1):
     print(o)


brojevi = 0
for x in range(0,101):
    if x < 20 and x % 2 == 0:
        brojevi = brojevi + 1 # brojevi += 1
print(brojevi)






