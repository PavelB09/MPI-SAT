# MPI-SAT
_Acesta este repo-ul pentru proiectul meu de la cursul MPI 2025, unde am studiat și implementat câteva metode de rezolvare a problemei SAT._
## Ce găsești:
1. Rezoluție: implementarea metodei clasice și a variantei „pereche scurtă” (minimă).

2. DP: algoritmul Davis–Putnam, cu propagarea unității și literalul pur.

3. DPLL: Davis–Putnam–Loveland–Logemann, cu patru strategii de alegere a literelui (clasică, aleatoare, după frecvență, MOMS).

4. Shortcut: funcție care rulează toate metodele pe un set de clauze și salvează rezultatele automat într-un CSV (rezultate.csv). Se selectează opțiunea 5 ascunsă.

## Structura proiectului
- main.py           # punctul de intrare și meniul interactiv
- rezolutie.py      # implementare Rezoluție + strategii
- DP.py             # implementare Davis–Putnam
- DPLL.py           # implementare DPLL + strategii
- utile.py          # funcții ajutătoare (clear, citire, shortcut)
- logger.py         # scrierea rezultatelor în CSV
- README.md         # documentația proiectului

## Instrucțiuni de utilizare
❗️Pentru utilizare rulează main.py

Datele de test se găsesc în fișierul "date de test" și se rulează în felul următor:
- Copiază datele din fișierul cu extensia .txt
- Rulează main.py
- Lipește (paste) conținutul fișierului .txt și apasă tasta ENTER de 2 ori
- Se alege opțiunea de test dorită din meniu (pentru export in ”rezultate.csv” se alege optiunea măsurarea performanței)