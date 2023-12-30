#Se da un text literar in limba romana, fara diacritice, care respecta toate regulile ortografice ale limbii romane(fara spatii nepotrivite, semne de puctuatie gresite, etc). Sa se afiseze ultimele doua cuvinte din fiecare fraza(se presupune ca fiecre fraza conine cel putin 3 cuvinte). Folositi ori de cate ori posibil modulul re.

import re # modulul re - regular expressions

def ultimele_doua_cuvinte(text):
    # Identifică frazele folosind expresii regulate
    fraze = re.split(r'(?<=[.!?])\s', text) # imparte textul in fraze
    # '?<=[.!?]' - înseamnă că se va căuta un caracter din setul [.!?] înainte de care să fie un alt caracter, iar '\s' înseamnă că se va căuta un spațiu după caracterul din setul [.!?]
    ind = 0
    for fraza in fraze:
        cuvinte = re.findall(r'\b\w+\b', fraza) # gaseste cuvintele din fraza
        # '\b\w+\b' - înseamnă că se va căuta un cuvânt care începe cu un caracter din setul [a-zA-Z0-9_] și care se termină cu un caracter din setul [a-zA-Z0-9_]
        ind += 1
        if len(cuvinte) >= 3: # dacă fraza conține cel puțin 3 cuvinte
            print(str(ind) + ") " + fraza + " -> ultimele 2 cuvinte: "  + cuvinte[-2] + " " + cuvinte[-1]) # afișăm ultimele două cuvinte din frază

#poate iti era dor de bac )))
baltag = "Vra sa zica ti-i sot? Da, mi-i sot. S-acuma umbli dupa dansul? Ce sa fac? Daca nu umbla el dupa mine, umblu eu dupa dansul."
ultimele_doua_cuvinte(baltag)



