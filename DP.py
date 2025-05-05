import copy
from utile import comp
from rezolutie import rezolutie

def gaseste_clauza_unit(K):
    for C in K:
        if len(C) == 1:
            return next(iter(C)) # am pus in loc de return C
    return None

def Reg1(K, L):
    k_nou = []
    complement = comp(L)
    for C in K:
        if L in C:
            continue
        c_noua = [l for l in C if l != complement]
        k_nou.append(c_noua)
    ''' if complement in C:
            c_noua = C.copy()
            c_noua.remove(complement)
            k_nou.append(c_noua)
        else:
            k_nou.append(C)
    for C in k_nou:
        if len(C) == 0:
            k_nou.remove(C)'''
    return k_nou

def Reg2(K, L):
    return [C for C in K if L not in C]

def gaseste_lit_pur(K):
    literari = set()
    for C in K:
        for L in C:
            literari.add(L)
    for L in literari:
        if comp(L) not in literari:
            return L
    return None

def DP(K):
    k_prim = copy.deepcopy(K)
    while True:
        if k_prim is None:
            return True
        if any(len(C) == 0 for C in k_prim):
            return False
        
        # Regula 1
        prop_unitate = gaseste_clauza_unit(k_prim)
        if prop_unitate is not None:
           # L = prop_unitate.pop()
            L = prop_unitate
            print("Aplic regula 1 (propagarea unitatii) pentru literalul", L)
            k_prim = Reg1(k_prim, L)
            print("Multimea de clauze dupa aplicarea regulii:", k_prim)
            continue

        # Regula 2
        lit_pur = gaseste_lit_pur(k_prim)
        if lit_pur is not None:
            print("Aplic regula 2 (literar pur) pentru literalul", lit_pur)
            k_prim = Reg2(k_prim, lit_pur)
            print("Multimea de clauze dupa aplicarea regulii:", k_prim)
            continue

        # Rezolutie
        R = rezolutie(k_prim)
        if R is True:
            return True
        else:
            return False
