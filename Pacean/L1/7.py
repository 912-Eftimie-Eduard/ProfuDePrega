#7. Se citesc întregii x, y, n, p. Să se copieze în x, începând din poziția p, ultimii n biți din y și să se afișeze noua valoare a lui x.
"""
    Rezolvare explicata:
    -- Citim x, un numar in baza 2
    ex de nr in baza 2: 1 = 1, 10 = 2, 11 = 3, 100 = 4, 101 = 5, 110 = 6, 111 = 7 ...
    --> sa spunem ca avem y = 101110101, x = 101011010, n = 4, p = 3
    y = 101110101, numaram bitii de la dreapta la stanga, incepand de la 0
    pozitii biti: 8|7|6|5|4|3|2|1|0
              y = 1|0|1|1|1|0|1|0|1
    noi ne dorim ca copiem de pe pozitia 3, ultimii 4 biti din y, adica 0111 , de pe pozitiile 6 5 4 3
    1.pentru asta vom crea un mask, un nr care acelasi numar de biti ca si y, are valoarea 1 pe pozitiile de care avem nevoie: 6 5 4 3 si 0 pe restul pozitiilor
    pozitii biti: 8|7|6|5|4|3|2|1|0
           mask = 0|0|1|1|1|1|0|0|0

    2.acum, vom face y &(and) mask, vom aplica operatia de and pe bitii lui y si pe bitii din mask
    AND:
    daca pe o pozitie din mask avem 1, atunci 1 & valoarea din y de pe acea pozitie = valoarea din y de pe acea pozitie
    daca pe o pozitie din mask avem 0, atunci 0 & valoarea din y de pe acea pozitie = 0

    pozitii biti:   8|7|6|5|4|3|2|1|0

                y = 1|0|1|1|1|0|1|0|1
             mask = 0|0|1|1|1|1|0|0|0
        ================================    
         y & mask = 0|0|1|1|1|0|0|0|0
        
        pe pozitia 0, 1 & 0 = 0, pe pozitia 1, 0 & 0 = 0, pe pozitia 2, 1 & 1 = 1, pe pozitia 3, 1 & 1 = 1, pe pozitia 4, 1 & 1 = 1, pe pozitia 5, 0 & 1 = 0, pe pozitia 6, 1 & 0 = 0, pe pozitia 7, 0 & 0 = 0, pe pozitia 8, 1 & 0 = 0 
     
    3. acum ca am obtinut y & mask, vom face x |(or) (y & mask), vom aplica operatia de or pe bitii lui x si pe bitii din y & mask
    OR:
    daca pe o pozitie din y & mask avem 1, atunci 1 | valoarea din x de pe acea pozitie = 1
    daca pe o pozitie din y & mask avem 0, atunci 0 | valoarea din x de pe acea pozitie = valoarea din x de pe acea pozitie
     
    pozitii biti:   8|7|6|5|4|3|2|1|0

                x = 1|0|1|0|1|1|0|1|0
         y & mask = 0|0|1|1|1|0|0|0|0
        ================================
   x | (y & mask) = 1|0|1|1|1|1|0|1|0

        pe pozitia 0, 1 | 0 = 1, pe pozitia 1, 0 | 0 = 0, pe pozitia 2, 1 | 1 = 1, pe pozitia 3, 0 | 1 = 1, pe pozitia 4, 1 | 1 = 1, pe pozitia 5, 1 | 0 = 1, pe pozitia 6, 0 | 0 = 0, pe pozitia 7, 1 | 0 = 1, pe pozitia 8, 0 | 0 = 0

        deci, am avut asa:
        x = 101011010
        y = 101110101
        n = 4
        p = 3
        1.am creat o masca cu valoarea 1 pe bitii de care avem nevoie si 0 pe restul pozitiilor
        mask = 000111100
        2.am aplicat operatia AND pe y si mask cat sa obtinem bitii de care avem nevoie din y
        y & mask = 000111000
        3.am aplicat operatia OR pe x si (y & mask) cat sa obtinem x cu bitii de care aveam nevoie din y
        x | (y & mask) = 101111010
"""
x = int(input("x = ")) # x = 101011010
y = int(input("y = ")) # y = 101110101
n = int(input("n = ")) # n = 4
p = int(input("p = ")) # p = 3
mask = (1 << n) - 1 # cream o masca cu valoarea 1 pe bitii de care avem nevoie si 0 pe restul pozitiilor , << inseamna shiftare la stanga, adica 1 << n inseamna 1 * 2^n, n fiind numarul de biti pe care vrem sa ii avem 1
print("x = ", bin(x)) 
print("y = ", bin(y))
print("mask = ", bin(mask))
print("y & mask = ", bin(y & mask))
print("x | (y & mask) = ", bin(x | (y & mask)))
x = x | (y & mask)
print("x = ", bin(x))
"""
    Exemplu:
    x = 101011010 = 346
    y = 101110101 = 373
    n = 4
    p = 3
    mask = 000111100
    y & mask = 000111000
    x | (y & mask) = 101111010
    x = 101111010
"""
# am folosit bin() pentru a afisa numerele in baza 2, iar tu le dai ca input in baza 10
# daca vrei sa le dai ca input in baza 2 , scrie asta:
'''
x = int(input("x = "), 2)
y = int(input("y = "), 2)
'''