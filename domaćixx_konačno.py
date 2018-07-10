with open("zad.xml", "r", encoding="utf-8") as fajl:
    recnik=dict()
    for red in fajl:
        if not(red.startswith("<")):
            try:
                rec,mala_rec,lema,pos=red.split("\t")
                if pos.startswith("N"):
                    #print(rec,mala_rec,lema,pos)
                    if lema in recnik.keys():
                        recnik[lema]=recnik[lema]+1
                    else:
                        recnik[lema]=1
     
            
            except:
                print(red)
   
        
with open("recnik.txt", "w", encoding="utf-8") as izlaz:
    
    for l,f in recnik.items():
        izlaz.write(l + "\t\t" + str(f) + "\n")
        
