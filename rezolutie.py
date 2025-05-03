import copy
from utile import comp

def rezolvent(c1, c2):
    for literal in c1:
        complement = comp(literal)
        if complement in c2:
            R = []
            for x in c1:
                if x != literal:
                    R.append(x)
            for y in c2:
                if y != complement:
                    R.append(y)
            if R:
                R = set(R)
            else:
                R = set()
            return R
    return None

def gaseste_rez(K):
    for i in range(0, len(K) - 1):
        for j in range(i + 1, len(K)):
            R = rezolvent(K[i], K[j])
            if R is not None and R not in K:
                return R
    return None

def gaseste_rez_pereche_scurta(k_prim):
    optiuni = []
    for i in range(len(k_prim)-1):
        for j in range(i+1, len(k_prim)):
            r = rezolvent(k_prim[i], k_prim[j])
            if r is not None and r not in k_prim:
                optiuni.append((len(k_prim[i]) + len(k_prim[j]), r))
    return min(optiuni)[1] if optiuni else None

def rezolutie(K, metoda="clasica"):
    k_prim = copy.deepcopy(K)
    pas = 1
    while True:

        if metoda == "clasica":
            R = gaseste_rez(k_prim)
        else:
            R = gaseste_rez_pereche_scurta(k_prim)

        print(f"Pasul {pas}")
        pas += 1
        print("Rezolvent gasit:", R)

        if R is None:
            return True
        if R == set():
            return False
        k_prim.append(R)