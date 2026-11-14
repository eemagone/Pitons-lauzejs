import itertools
import time

KOPAS = {
    "1": "abcdefghijklmnopqrstuvwxyz",
    "2": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "3": "abcdefghijklmnopqrstuvwxyz0123456789",
    "4": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
    "5": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:,.<>/?",
}

MAX_P_GARUMS = 10

print("KODEJS 2.2v\n")

parole = input("Ievadi paroli: ")

print("\nIzvelies simbolu kopu:")
print("1 - mazie burti")
print("2 - mazie + lielie burti")
print("3 - mazie + cipari")
print("4 - burti + cipari")
print("5 - viss...")
izvele = input("Izvele: ")

if izvele not in KOPAS:
    print("Nepareiza izvele.")
    raise SystemExit

simboli = KOPAS[izvele]

meginajumi = 0
atrada = False
atrasta_parole = ""
start = time.time()

for garums in range(1, MAX_P_GARUMS + 1):
    for minejums in itertools.product(simboli, repeat=garums):
        meginajumi += 1
        mybparole = "".join(minejums)
        if mybparole == parole:
            atrada = True
            atrasta_parole = mybparole
            break
    if atrada:
        break

laiks = time.time() - start

print("\n\nKodeja rezultati:\n")
if atrada:
    print(f"Atrasta parole: {atrasta_parole}")
    print(f"Meginajumi: {meginajumi}")
else:
    print(f"Parole netika atrasta lidz garumam {MAX_P_GARUMS}")
    print(f"Meginajumi: {meginajumi}")
print(f"Laiks: {laiks:.2f} sekundes")
