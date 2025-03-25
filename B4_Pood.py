def pood():
    ostud=[]
    hinnad=[]
    ostetud=[]
    while True:
        ost=input("Sisesta ostud (lõpetamiseks 'lõpp'): ")
        if ost=="lõpp":
            break
        hind=float(input("Sisesta hind: "))
        ostud.append(ost)
        hinnad.append(hind)
    while True:
        print("1. Kustuta ostud ja lisa ostetud")
        print("2. Näita ostud tähestikulises järjekorras")
        print("3. Leia kalleim ja odavaim")
        print("4. Leia ostu hind")
        print("5. Lõpeta")
        valik=input("Vali number: ")
        if valik=="1":
            kustutatav=input("Mis ostud kustutada? ")
            if kustutatav in ostud:
                koht=ostud.index(kustutatav)
                ostetud.append(ostud[koht])
                ostud.pop(koht)
                hinnad.pop(koht)
                print("Tšekk:")
                for i in range(ostetud):
                    print(ostetud[i])
                print("Kustutatud ja lisatud!")
            else:
                print("Ei leitud!")
        elif valik=="2":
            uus_nimekiri=sorted(ostud)
            for i in range(uus_nimekiri):
                koht=ostud.index(uus_nimekiri[i])
                print(uus_nimekiri[i],":",hinnad[koht],"€")
        elif valik=="3":
            if ostud:
                kallis=max(hinnad)
                odav=min(hinnad)
                kallis_koht=hinnad.index(kallis)
                odav_koht=hinnad.index(odav)
                print("Kalleim:",ostud[kallis_koht],"(",kallis,"€)")
                print("Odavaim:",ostud[odav_koht],"(",odav,"€)")
            else:
                print("Ostude nimekiri tühi!")
        elif valik=="4":
            otsitav=input("Mis ostu hind? ")
            if otsitav in ostud:
                koht=ostud.index(otsitav)
                print("Hind:",hinnad[koht],"€")
            else:
                print("Ei leitud!")
        elif valik=="5":
            print("Lõpp!")
            break
        else:
            print("Vale valik!")
pood()
