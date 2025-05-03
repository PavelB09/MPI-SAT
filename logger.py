import csv

csv_file = "rezultate.csv"
def init_csv():
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Algoritm","Strategie","Satisfiabil","Timp (s)","Memorie (MB)"])
        
def log_rezultat(algoritm, strategie="", satisfiabil="", timp=0.0, mem=0.0):
    with open(csv_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([algoritm,strategie,satisfiabil,f"{timp:.6f}",f"{mem:.6f}"])
