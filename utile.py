import os
import time
import tracemalloc
from logger import init_csv, log_rezultat

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
    
    # 1) Rezolutie: clasica si scurta
    for strategie in ("clasica", "scurta"):
        print(f"\n>> Rezolutie ({strategie})")
        tracemalloc.start()
        t0 = time.perf_counter()
        sat = rezolutie(K, strategie)
        dt = time.perf_counter() - t0
        _, mem_varf = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        sat_txt = "Satisfiabil" if sat else "Nesatisfiabil"
        mb = mem_varf / 10**6
        print(f"Timp: {dt:.6f}s, Memorie: {mb:.6f}MB -> {sat_txt}")
        log_rezultat("Rezolutie", strategie, sat_txt, dt, mb)

    # 2) DP
    print("\n>> DP")
    tracemalloc.start()
    t0 = time.perf_counter()
    sat = DP(K) 
    dt = time.perf_counter() - t0
    _, mem_varf = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    sat_txt = "Satisfiabil" if sat else "Nesatisfiabil"
    mb = mem_varf / 10**6
    print(f"Timp: {dt:.6f}s, Memorie: {mb:.6f}MB -> {sat_txt}")
    log_rezultat("DP", "", sat_txt, dt, mb)

    # 3) DPLL: cele patru strategii
    for strategie in ("clasica", "aleator", "frecventa", "minima"):
        print(f"\n>> DPLL ({strategie})")
        tracemalloc.start()
        t0 = time.perf_counter()
        sat = DPLL(K, strategie=strategie)
        dt = time.perf_counter() - t0
        _, mem_varf = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        sat_txt = "Satisfiabil" if sat else "Nesatisfiabil"
        mb = mem_varf / 10**6
        print(f"Timp: {dt:.6f}s, Memorie: {mb:.6f}MB -> {sat_txt}")
        log_rezultat("DPLL", strategie, sat_txt, dt, mb)

