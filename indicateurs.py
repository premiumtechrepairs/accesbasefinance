def marge_net(resultat_net, chiffre_affaires):
    r = (resultat_net / chiffre_affaires) * 100
    return r

print(marge_net(50, 1000))

def liquidite(actifs_c, passifs_c):
    li = actifs_c / passifs_c
    return li

def endettement(dettestotal, capitauxpropre):
    li = dettestotal / capitauxpropre
    return li

def rendement(coursfin, coursdebut):
    li = ((coursfin - coursdebut) / coursdebut) * 100
    return li

def moyennemobile(listenombres, fenetre):
    li = []
    for e in range(len(listenombres)):
        debut = max(0, e - fenetre + 1)
        l = liste[debut : e + 1]
        li.append(sum(l)/len(l))
    return li

