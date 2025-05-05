import copy
from utile import comp
from DP import Reg1, gaseste_clauza_unit, gaseste_lit_pur, Reg2

def strategie_alege_literal(K, strategie="clasica"):
    if strategie == "aleator":
        from random import choice
        return choice(list(next(iter(K))))

    elif strategie == "frecventa":
        frecvente = {}
        for C in K:
            for L in C:
                frecvente[L] = frecvente.get(L, 0) + 1
        return max(frecvente, key=frecvente.get)

    elif strategie == "minima": # MOMS (Maximum Occurrences in clauses of Minimum Size)
        lung_min = min(len(C) for C in K)
        contor = {}

        for C in K:
            if len(C) == lung_min:
                for L in C:
                    contor[L] = contor.get(L, 0) + 1
        return max(contor, key=contor.get)

    else:
        return next(iter(next(iter(K))))
    
def DPLL(K, strategie="clasica"):
    k_prim = copy.deepcopy(K)
    while True:
        if not k_prim:
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
        if k_prim == []:
            return True
        
        # Regula 3
        if k_prim is not None:
            L = strategie_alege_literal(k_prim, strategie)
            print("Aplic regula 3 (ramificare) pentru literalul", L)
            k_nou = Reg1(copy.deepcopy(k_prim), L)
            print("Multimea de clauze dupa aplicarea regulii:", k_nou)
            if DPLL(k_nou, strategie):
                return True
            comp_l = comp(L)
            print("Aplic regula 3 (ramificare) pentru literalul", comp_l)
            k_nou = Reg1(copy.deepcopy(k_prim), comp_l)
            print("Multimea de clauze dupa aplicarea regulii:", k_nou)
            return DPLL(k_nou, strategie)

