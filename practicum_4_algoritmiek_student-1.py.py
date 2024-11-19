#Naam: Merry Ashji
#Klas: V1Q
#Studentnummer:1764739
'''
1) Hieronder staat de pseudocode van een sorteeralgoritme:
1.	Startend vanaf het begin van een lijst, vergelijk elk element met zijn volgende buur.
2.	Als het element groter is dan zijn volgende buur, verwissel ze van plaats.
3.	Doorloop zo de lijst tot het eind.
4.	Als er verwis1selingen zijn geweest bij stap 2., ga naar stap 1.

1a. Handmatig toepassen
Gegeven is de lijst l = [ 4, 3, 1, 2 ]. Geef de waardes die de lijst aanneemt bij álle tussenstappen bij toepassing van bovenstaand sorteeralgoritme.

Stap 1: L=[ 3, 4, 1, 2 ]
Stap 2: L=[ 3, 1, 4, 2 ]
Stap 3: L=[ 1, 3, 4, 2 ]# bij stap 2 is er een verwisseling geweest dus ik moet terug naar stap 1. stap 1 (Startend vanaf het begin van een lijst)
dus 3&1 worden eerder verwisseld dan 4&2.
Stap 4: L=[ 1, 3, 2, 4]
Stap 5: L=[ 1, 2, 3, 4]

1c. Best en worst case
•	Stel je hebt een lijst met de waarden 1, 2 en 3. Bij welke volgorde van de waarden in de lijst is het sorteeralgoritme het snelste klaar (best-case scenario)? Hoeveel vergelijkingen (zoals beschreven in stap 1. van de pseudocode) zijn nodig geweest?
       -     best-case scenario  L=[1, 2, 3]
       -     2 stap nodig.

•	Bij welke volgorde van de waarden in de lijst is het sorteeralgoritme het minst snel klaar (worst-case scenario)? Hoeveel vergelijkingen zijn nodig geweest?
       -    worst-case scenario:  L=[3, 2, 1]
       -    6 stappen nodig.

•	Stel je hebt een lijst met de waarden 1 tot en met 4. Wat is nu het best-case scenario? Hoeveel vergelijkingen zijn er nodig? En wat is nu het worst-case scenario? Hoeveel vergelijkingen zijn er nodig?
       -	best-case scenario:  L = [1, 2, 3, 4 ]
       -	3 stap nodig.
       -	worst-case scenario:  L = [4, 3, 2, 1 ]
       -	12 stappen nodig.

•	Stel je hebt een lijst met de waarden 1 tot en met n (je weet nu dus niet precies hoeveel waarden er in de lijst zitten, het zijn er 'n'). Wat is nu het best-case scenario? Hoeveel vergelijkingen zijn er nodig? En wat is nu het worst-case scenario? Hoeveel vergelijkingen zijn er nodig?
       -  	best-case scenario:  (1, 2 ,..., n-1,n)
       -    (n-1) stappen nodig.
       - 	worst-case scenario: (n, n-1 ,..., 2, 1)
       -    n(n-1) stappen nodig.
'''


def my_sort(lst):
    a = 0
    while a < len(lst):
        if a!=0 and lst[a] < lst[a-1]:
            lst[a], lst[a-1] = lst[a-1], lst[a]
            a = a - 1
        else:
            a = a + 1
    return None


def linear_search_recursive(lst, target):
    lst=sorted(lst)
    if target< lst[0] or target > lst[-1]:
        return False
    elif lst[0] != target:
        return linear_search_recursive(lst[1:],target)
    return True


def binary_search_recursive(lst, target):
    if target< lst[0] or target > lst[-1]:
        return False
    mid = len(lst) // 2
    l = lst[:mid]
    r = lst[mid:]
    if target== lst[mid]:
        return True
    elif lst[mid] > target:
        return binary_search_recursive(l, target)
    elif lst[mid] < target:
        return binary_search_recursive(r, target)
    else:
        return False



import random

def test_my_sort():
    lst_test = random.sample(range(-99, 100), 6)
    lst_copy = lst_test.copy()
    my_sort(lst_test)
    assert lst_test == sorted(lst_copy), f"Fout: my_sort({lst_copy}) geeft {lst_test} in plaats van {sorted(lst_copy)}"

def test_linear_search_recursive():
    for i in range(10):
        lst_test = random.sample(range(20), 6)
        target = random.randrange(20)
        outcome = linear_search_recursive(lst_test, target)
        assert outcome == (target in lst_test), \
            f"Fout: linear_search_recursive({lst_test}, {target}) geeft {outcome} in plaats van {target in lst_test}"


def test_binary_search_recursive():
    for i in range(10):
        lst_test = sorted(random.sample(range(20), 6))
        target = random.randrange(20)
        outcome = binary_search_recursive(lst_test, target)
        assert outcome == (target in lst_test), \
            f"Fout: binary_search_recursive({lst_test}, {target}) geeft {outcome} in plaats van {target in lst_test}"


if __name__ == '__main__':
    try:
        print("\x1b[0;32m")

        test_my_sort()
        print("Je functie my_sort() werkt goed!")

        test_linear_search_recursive()
        print("Je functie linear_search_recursive() werkt goed!")

        test_binary_search_recursive()
        print("Je functie binary_search_recursive() werkt goed!")

        print("\nGefeliciteerd, alles lijkt te werken! Lever je werk nu in op Canvas...")

    except AssertionError as ae:
        print("\x1b[0;31m")
        print(ae)