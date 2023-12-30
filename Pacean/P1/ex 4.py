"""
Scrieti intr-o singura linie de cod (si fara a folosi structuri repetitive) pentru a afisa o singura data, in ordine lexicografica, vocalele folosite intr-un text citit din fisierul text.txt.
Input:
Fisierul text.txt contine:
    "Ana are mere."
Output:
    A a e
"""
print(' '.join(sorted(set(filter(str.isalpha, open('text.txt').read())) & set('aeiouAEIOU'))))
# open() - deschide fisierul
# read() - citeste tot continutul fisierului
# str.isalpha() - verifica daca un caracter este litera

# filter(str.isalpha, open('text.txt').read()) - filtreaza doar literele din fisier
# print( set(filter(str.isalpha, open('text.txt').read()) )) - afiseaza doar literele din fisier
# setul literelor din fisier & setul literelor vocale - afiseaza doar vocalele care apar in fisier
# sort - sorteaza vocalele in ordine lexicografica
# join - afiseaza vocalele separate prin spatiu , daca lasam fara join, afisa vocalele asa ['A', 'a', 'e'], afisa set-ul



