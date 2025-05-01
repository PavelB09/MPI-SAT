import os
import copy
import time
import tracemalloc

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def comp(L):
    if L.startswith("-"):
        return L[1:]
    else:
        return "-" + L

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

def DP(K):
    k_prim = copy.deepcopy(K)
    while True:
        if k_prim is None:
            return True
        if any(len(C) == 0 for C in k_prim):
            return False
        prop_unitate = gaseste_clauza_unit(k_prim)
        if prop_unitate is not None:
            L = prop_unitate.pop()
            print("Aplic regula 1 (propagarea unitatii) pentru literalul", L)
            k_prim = Reg1(k_prim, L)
            print("Multimea de clauze dupa aplicarea regulii:", k_prim)
            continue
        lit_pur = gaseste_lit_pur(k_prim)
        if lit_pur is not None:
            print("Aplic regula 2 (literar pur) pentru literalul", lit_pur)
            k_prim = Reg2(k_prim, lit_pur)
            print("Multimea de clauze dupa aplicarea regulii:", k_prim)
            continue
        R = rezolutie(k_prim)
        if R is True:
            return True
        else:
            return False

def gaseste_clauza_unit(K):
    for C in K:
        if len(C) == 1:
            return C
    return None

def Reg1(K, L):
    k_nou = []
    complement = comp(L)
    for C in K:
        if L in C:
            continue
        if complement in C:
            c_noua = C.copy()
            c_noua.remove(complement)
            k_nou.append(c_noua)
        else:
            k_nou.append(C)
    for C in k_nou:
        if len(C) == 0:
            k_nou.remove(C)
    return k_nou

def gaseste_lit_pur(K):
    literari = set()
    for C in K:
        for L in C:
            literari.add(L)
    for L in literari:
        if comp(L) not in literari:
            return L
    return None

def Reg2(K, L):
    return [C for C in K if L not in C]

def DPLL(K, strategie="clasica"):
    k_prim = copy.deepcopy(K)
    while True:
        if k_prim is None:
            return True
        if any(len(C) == 0 for C in k_prim):
            return False
        
        # Regula 1
        prop_unitate = gaseste_clauza_unit(k_prim)
        if prop_unitate is not None:
            L = prop_unitate.pop()
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
            print("Multimea de clauze dupa aplicarea regulii:", k_prim)
            if DPLL(k_nou):
                return True
            comp_l = comp(L)
            print("Aplic regula 3 (ramificare) pentru literalul", comp_l)
            k_nou = Reg1(copy.deepcopy(k_prim), comp_l)
            print("Multimea de clauze dupa aplicarea regulii:", k_prim)
            return DPLL(k_nou)

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


def citire():
    K = []
    while True:
        C = input()
        if C == "":
            break
        K.append(set(C.split()))
    return K

def masurare_performanta(K):
    optiune = ""
    while optiune != "0":
        print("Optiuni:")
        print("1. Rezolutie")
        print("2. DP")
        print("3. DPLL")
        print("0. Iesire")
        optiune = input("Alege metoda: ")

        match optiune:
            case "1":
                print("\nMetode de rezolutie:")
                print("1. clasica")
                print("2. scurta")
                sub = input("Alege (1/2): ")
                if sub == "1":
                    metoda = "clasica"
                elif sub == "2":
                    metoda = "scurta"
                else:
                    print("Optiune invalida pentru rezolutie.")
                    continue

                print(f"Se executa Rezolutie ({metoda}) cu masurarea performantei...")
                tracemalloc.start()
                inceput = time.perf_counter()
                rezultat = rezolutie(K, metoda)
                sfarsit = time.perf_counter()
                mem_curenta, mem_varf = tracemalloc.get_traced_memory()
                tracemalloc.stop()

                print(f"\nRezolutie ({metoda}):", "Satisfiabil" if rezultat else "Nesatisfiabil")
                print(f"Timp de executie: {sfarsit - inceput:.6f} secunde")
                print(f"Memorie utilizata (varf): {mem_varf / 10**6:.6f} MB")

            case "2":
                print("Se executa algoritmul DP cu masurarea performantei...")
                tracemalloc.start()
                inceput = time.perf_counter()
                rezultat = DP(K)
                sfarsit = time.perf_counter()
                mem_curenta, mem_varf = tracemalloc.get_traced_memory()
                tracemalloc.stop()
                print("\nDP:", "Satisfiabil" if rezultat else "Nesatisfiabil")
                print(f"Timp de executie: {sfarsit - inceput:.6f} secunde")
                print(f"Memorie utilizata (varf): {mem_varf / 10**6:.6f} MB")

            case "3":
                print("\nStrategii DPLL:")
                print("1. clasica")
                print("2. aleator")
                print("3. frecventa")
                print("4. minima (MOMS)")
                sub = input("Alege (1/2/3/4): ")
                if sub == "1":
                    strat = "clasica"
                elif sub == "2":
                    strat = "aleator"
                elif sub == "3":
                    strat = "frecventa"
                elif sub == "4":
                    strat = "minima"
                else:
                    print("Optiune invalida pentru DPLL.")
                    continue

                print(f"Se executa DPLL ({strat}) cu masurarea performantei...")
                tracemalloc.start()
                inceput = time.perf_counter()
                rezultat = DPLL(K, strategie=strat)
                sfarsit = time.perf_counter()
                mem_curenta, mem_varf = tracemalloc.get_traced_memory()
                tracemalloc.stop()

                print(f"\nDPLL ({strat}):", "Satisfiabil" if rezultat else "Nesatisfiabil")
                print(f"Timp de executie: {sfarsit - inceput:.6f} secunde")
                print(f"Memorie utilizata (varf): {mem_varf / 10**6:.6f} MB")

            case "0":
                break

            case _:
                print("Optiune invalida. Introdu 0-3.")

        if optiune != "0":
            input("\nApasa Enter pentru a continua...")
            clear()


def main():
    clear()
    print("Introduceti clauzele, apoi apasati ENTER:")
    K = citire()
    clear()
    optiune = ""
    while optiune != "0":
        print("Optiuni:")
        print("1. Rezolutie")
        print("2. DP")
        print("3. DPLL")
        print("4. Masurare performanta")
        print("0. Iesire")
        optiune = input("Alege metoda: ")

        match optiune:
            case "1":
                print("\nMetode de rezolutie:")
                print("1. clasica")
                print("2. scurta")
                sub = input("Alege (1/2): ")
                if sub == "1":
                    metoda = "clasica"
                elif sub == "2":
                    metoda = "scurta"
                else:
                    print("Optiune invalida pentru rezolutie.")
                    continue

                rezultat = rezolutie(K, metoda)
                print(f"\nRezolutie ({metoda}):", "Satisfiabil" if rezultat else "Nesatisfiabil")

            case "2":
                rezultat = DP(K)
                print("\nDP:", "Satisfiabil" if rezultat else "Nesatisfiabil")

            case "3":
                print("\nStrategii DPLL:")
                print("1. clasica")
                print("2. aleator")
                print("3. frecventa")
                print("4. minima (MOMS)")
                sub = input("Alege (1/2/3/4): ")
                if sub == "1":
                    strat = "clasica"
                elif sub == "2":
                    strat = "aleator"
                elif sub == "3":
                    strat = "frecventa"
                elif sub == "4":
                    strat = "minima"
                else:
                    print("Optiune invalida pentru DPLL.")
                    continue

                rezultat = DPLL(K, strategie=strat)
                print(f"\nDPLL ({strat}):", "Satisfiabil" if rezultat else "Nesatisfiabil")

            case "4":
                clear()
                masurare_performanta(K)

            case "0":
                break

            case _:
                print("Optiune invalida. Introdu 0-4.")

        if optiune != "0":
            input("\nApasa Enter pentru a continua...")
            clear()

    clear()
main()