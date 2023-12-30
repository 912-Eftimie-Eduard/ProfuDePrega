#Să se genereze toate submulțimile mulțimii A = {1,2, ... , n}, unde numărul natural nenul n ≤ 10 se citește de la tastatură (fără backtracking)

#okay, e destul de stupida solutia asta, dar merge , nu inteleg de ce v-a pus fara backtracking, practic, general submultimi de cate 1 element, dupa 2, 3, ... 10 (spune ca n<=10), si le afisez

n = int(input("n = "))
for i in range(1, n + 1):
    print(i, end = " | ")
print()
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        print(i, j, end = " | ")
print()
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        for k in range(j + 1, n + 1):
            print(i, j, k, end = " | ")
print()
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        for k in range(j + 1, n + 1):
            for l in range(k + 1, n + 1):
                print(i, j, k, l, end = " | ")
print()
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        for k in range(j + 1, n + 1):
            for l in range(k + 1, n + 1):
                for m in range(l + 1, n + 1):
                    print(i, j, k, l, m, end = " | ")
print()
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        for k in range(j + 1, n + 1):
            for l in range(k + 1, n + 1):
                for m in range(l + 1, n + 1):
                    for o in range(m + 1, n + 1):
                        print(i, j, k, l, m, o, end = " | ")
print()
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        for k in range(j + 1, n + 1):
            for l in range(k + 1, n + 1):
                for m in range(l + 1, n + 1):
                    for o in range(m + 1, n + 1):
                        for p in range(o + 1, n + 1):
                            print(i, j, k, l, m, o, p, end = " | ")
print()
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        for k in range(j + 1, n + 1):
            for l in range(k + 1, n + 1):
                for m in range(l + 1, n + 1):
                    for o in range(m + 1, n + 1):
                        for p in range(o + 1, n + 1):
                            for q in range(p + 1, n + 1):
                                print(i, j, k, l, m, o, p, q, end = " | ")
print()
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        for k in range(j + 1, n + 1):
            for l in range(k + 1, n + 1):
                for m in range(l + 1, n + 1):
                    for o in range(m + 1, n + 1):
                        for p in range(o + 1, n + 1):
                            for q in range(p + 1, n + 1):
                                for r in range(q + 1, n + 1):
                                    print(i, j, k, l, m, o, p, q, r, end = " | ")
print()
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        for k in range(j + 1, n + 1):
            for l in range(k + 1, n + 1):
                for m in range(l + 1, n + 1):
                    for o in range(m + 1, n + 1):
                        for p in range(o + 1, n + 1):
                            for q in range(p + 1, n + 1):
                                for r in range(q + 1, n + 1):
                                    for s in range(r + 1, n + 1):
                                        print(i, j, k, l, m, o, p, q, r, s, end = " | ")
print()

"""
def generate_subsets(n):
    for i in range(2**n):
        subset = [j + 1 for j in range(n) if (i >> j) & 1]
        yield subset

# Citim n de la tastatură
n = int(input("Introduceti n (n <= 10): "))

# Verificăm condiția n <= 10
if n > 10:
    print("Valoarea lui n trebuie să fie mai mică sau egală cu 10.")
else:
    print("Submulțimile mulțimii A = {1, 2, ...,", n, "} sunt:")
    for subset in generate_subsets(n):
        print(subset)

mai am si solutia asta, dar e mai complicata si nu stiu daca va lasa cu subsets ))
Acest program folosește o funcție generator (generate_subsets) care produce toate submulțimile mulțimii A prin parcurgerea tuturor numerelor de la 0 la 
2^n−1 și construirea submulțimilor corespunzătoare folosind reprezentarea binară a acestor numere.
"""

mai am astea de la b si c