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
                sat = rezolutie(K, strategie)
                sfarsit = time.perf_counter()
                _, mem_varf = tracemalloc.get_traced_memory()
                tracemalloc.stop()

                timp = sfarsit - inceput
                mem_mb = mem_varf / 10**6
                sat = "Satisfiabil" if sat else "Nesatisfiabil"

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
                sat = DP(K)
                sfarsit = time.perf_counter()
                _, mem_varf = tracemalloc.get_traced_memory()
                tracemalloc.stop()

                timp = sfarsit - inceput
                mem_mb = mem_varf / 10**6
                sat = "Satisfiabil" if sat else "Nesatisfiabil"

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
                sat = DPLL(K, strategie=strategie)
                sfarsit = time.perf_counter()
                _, mem_varf = tracemalloc.get_traced_memory()
                tracemalloc.stop()

                timp = sfarsit - inceput
                mem_mb = mem_varf / 10**6
                sat = "Satisfiabil" if sat else "Nesatisfiabil"

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
                    strategie = "clasica"
                elif sub == "2":
                    strategie = "scurta"
                else:
                    print("Optiune invalida pentru rezolutie.")
                    continue

                sat = rezolutie(K, strategie)
                print(f"\nRezolutie ({strategie}):", "Satisfiabil" if sat else "Nesatisfiabil")

            case "2":
                sat = DP(K)
                print("\nDP:", "Satisfiabil" if sat else "Nesatisfiabil")

            case "3":
                print("\nStrategii DPLL:")
                print("1. clasica")
                print("2. aleator")
                print("3. frecventa")
                print("4. minima (MOMS)")
                sub = input("Alege (1/2/3/4): ")
                strategie = {"1":"clasica","2":"aleator","3":"frecventa","4":"minima"}.get(sub)

                if strategie is None:
                    print("Optiune invalida pentru DPLL.")
                    continue

                sat = DPLL(K, strategie=strategie)
                print(f"\nDPLL ({strategie}):", "Satisfiabil" if sat else "Nesatisfiabil")

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
