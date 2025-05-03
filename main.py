from utile import clear, citire, shortcut
from rezolutie import rezolutie
from DP import DP
from DPLL import DPLL
from logger import init_csv, log_rezultat
import tracemalloc, time

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
                # --- Rezolutie ---
                print("\nMetode de rezolutie:")
                print("1. clasica")
                print("2. scurta")
                sub = input("Alege (1/2): ")
                strategie = "clasica" if sub == "1" else "scurta" if sub == "2" else None
                if strategie is None:
                    print("Optiune invalida pentru rezolutie.")
                    continue

                tracemalloc.start()
                inceput = time.perf_counter()
                rezultat = rezolutie(K, strategie)
                sfarsit = time.perf_counter()
                mem_before, mem_varf = tracemalloc.get_traced_memory()
                tracemalloc.stop()

                timp = sfarsit - inceput
                mem_mb = mem_varf / 10**6
                sat = "Satisfiabil" if rezultat else "Nesatisfiabil"

                print(f"\nRezolutie ({strategie}): {sat}")
                print(f"Timp: {timp:.6f}s, Memorie: {mem_mb:.6f}MB")

                log_rezultat(
                    algoritm="Rezolutie",
                    strategie=strategie,
                    satisfiabil=sat,
                    timp=timp,
                    mem=mem_mb
                )

            case "2":
                # --- DP ---
                tracemalloc.start()
                inceput = time.perf_counter()
                rezultat = DP(K)
                sfarsit = time.perf_counter()
                mem_before, mem_varf = tracemalloc.get_traced_memory()
                tracemalloc.stop()

                timp = sfarsit - inceput
                mem_mb = mem_varf / 10**6
                sat = "Satisfiabil" if rezultat else "Nesatisfiabil"

                print(f"\nDP: {sat}")
                print(f"Timp: {timp:.6f}s, Memorie: {mem_mb:.6f}MB")

                log_rezultat(
                    algoritm="DP",
                    strategie="",
                    satisfiabil=sat,
                    timp=timp,
                    mem=mem_mb
                )

            case "3":
                # --- DPLL ---
                print("\nStrategii DPLL:")
                print("1. clasica")
                print("2. aleator")
                print("3. frecventa")
                print("4. minima")
                sub = input("Alege (1/2/3/4): ")
                strategie = {"1":"clasica","2":"aleator","3":"frecventa","4":"minima"}.get(sub)
                if strategie is None:
                    print("Optiune invalida pentru DPLL.")
                    continue

                tracemalloc.start()
                inceput = time.perf_counter()
                rezultat = DPLL(K, strategie=strategie)
                sfarsit = time.perf_counter()
                mem_before, mem_varf = tracemalloc.get_traced_memory()
                tracemalloc.stop()

                timp = sfarsit - inceput
                mem_mb = mem_varf / 10**6
                sat = "Satisfiabil" if rezultat else "Nesatisfiabil"

                print(f"\nDPLL ({strategie}): {sat}")
                print(f"Timp: {timp:.6f}s, Memorie: {mem_mb:.6f}MB")

                log_rezultat(
                    algoritm="DPLL",
                    strategie=strategie,
                    satisfiabil=sat,
                    timp=timp,
                    mem=mem_mb
                )

            case "0":
                break

            case _:
                print("Optiune invalida. Introdu 0-3.")

        if optiune != "0":
            input("\nApasa Enter pentru a continua...")
            clear()


def main():
    init_csv()
    clear()
    print("Introduceti clauzele (fiecare clauza pe o linie, terminati cu o linie goala):")
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

            case "5":
                shortcut(K)
            case "0":
                break

            case _:
                print("Optiune invalida. Introdu 0-4.")

        if optiune != "0":
            input("\nApasa Enter pentru a continua...")
            clear()

    clear()
if __name__ == "__main__":
    main()
