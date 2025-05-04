import os
import time
import tracemalloc
from logger import log_rezultat

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def comp(L):
    if L.startswith("-"):
        return L[1:]
    return "-" + L

def citire():
    K = []
    while True:
        C = input()
        if C == "":
            break
        K.append(set(C.split()))
    return K

def shortcut(K):
    from rezolutie import rezolutie
    from DP import DP
    from DPLL import DPLL
    
    # --- Rezolutie ---
    for strategie in ("clasica", "scurta"):
        print(f"\n>> Rezolutie ({strategie})")
        tracemalloc.start()
        inceput = time.perf_counter()
        sat = rezolutie(K, strategie)
        timp = time.perf_counter() - inceput
        _, mem_varf = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        sat = "Satisfiabil" if sat else "Nesatisfiabil"
        mb = mem_varf / 10**6
        print(f"Timp: {timp:.6f}s, Memorie: {mb:.6f}MB -> {sat}")
        log_rezultat("Rezolutie", strategie, sat, timp, mb)

    # --- DP ---
    print("\n>> DP")
    tracemalloc.start()
    inceput = time.perf_counter()
    sat = DP(K) 
    timp = time.perf_counter() - inceput
    _, mem_varf = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    sat = "Satisfiabil" if sat else "Nesatisfiabil"
    mb = mem_varf / 10**6
    print(f"Timp: {timp:.6f}s, Memorie: {mb:.6f}MB -> {sat}")
    log_rezultat("DP", "", sat, timp, mb)

    # --- DPLL ---
    for strategie in ("clasica", "aleator", "frecventa", "minima"):
        print(f"\n>> DPLL ({strategie})")
        tracemalloc.start()
        inceput = time.perf_counter()
        sat = DPLL(K, strategie=strategie)
        timp = time.perf_counter() - inceput
        _, mem_varf = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        sat = "Satisfiabil" if sat else "Nesatisfiabil"
        mb = mem_varf / 10**6
        print(f"Timp: {timp:.6f}s, Memorie: {mb:.6f}MB -> {sat}")
        log_rezultat("DPLL", strategie, sat, timp, mb)

