
#Naam:merry ashji
#Klas:
#Studentnummer:


def mean(lst):
    """ Retourneert het gemiddelde (float) van de lijst lst. """
    som=sum(lst)
    lengte=len(lst)
    gemiddelde=som/lengte
    return gemiddelde



def rnge(lst):
    """ Retourneert het bereik (int) van de lijst lst. """
    bereik= max(lst)-min(lst)
    return bereik



def median(lst):
    """ Retourneert de mediaan (float) van de lijst lst. """
    lst=sorted(lst)
    if (len(lst)%2)!=0:
        x=((len(lst))//2)
        median=float(lst[x])
    else:
        x=((len(lst))//2)
        median=(lst[x]+lst[x-1])/2
    return median

def q1(lst):
    lst.sort()
    lst1 = []
    for i in range ((len(lst)//2)):
        lst1.append(1)
        lst1[i] = lst[i]
    m=median (lst1)
    return m

def q3(lst):
    lst.sort()
    lst1 = []
    for i in range ((len(lst)//2)):
        lst1.append(1)
        lst1[i] = lst[len(lst) - i - 1]
    m=median (lst1)
    return m


def var(lst):
    """ Retourneert de variantie (float) van de lijst lst. """
    gemiddelde=mean(lst)
    variantie=[]
    for i in lst:
        x= (i-gemiddelde)**2
        variantie.append(x)
    som=sum(variantie)
    z=som/(len(lst))
    return z

def std(lst):
    """ Retourneert de standaardafwijking (float) van de lijst lst. """
    standaardafwijking= var(lst)**(1/2)
    return standaardafwijking


def freq(lst):
    """Retourneert een dictionary met als keys de waardes die voorkomen in lst en
    als value het aantal voorkomens van die waarde."""

    freqs = dict()
    for ietm in lst:
        if ietm in freqs:
            freqs[ietm]+=1
        else:
            freqs[ietm]=1

    return freqs




def modes(lst):
    mode=[]
    for i in range(len(lst)):
        mode.append(lst.count(lst[i]))
    m= max(mode)
    ml = [x for x in lst if lst.count(x)==m ] #to find most frequent values
    modi = []
    for x in ml: #to remove duplicates of mode
        if x not in modi:
         modi.append(x)
    return sorted (modi)




def my_assert_arg(function, arg, expected_output):
    assert function(arg) == expected_output, \
        f"Fout: {function.__name__}({arg}) geeft {function(arg)} in plaats van {expected_output}"


def test_mean():
        testcases = [
            ([4, 2, 5, 8, 6], 5.0),
            ([1, 3, 2, 4, 6, 2, 4, 2], 3.0)
        ]

        for case in testcases:
            my_assert_arg(mean, case[0], case[1])


def test_rnge():
    testcases = [
        ([4, 2, 5, 8, 6], 6),
        ([1, 3, 2, 4, 6, 2, 4, 2], 5)
    ]

    for case in testcases:
        my_assert_arg(rnge, case[0], case[1])


def test_median():
    testcases = [
        ([4, 2, 5, 8, 6], 5.0),
        ([1, 3, 4, 6, 4, 2], 3.5),
        ([1, 3, 4, 6, 2, 4, 2], 3.0),
        ([1, 3, 2, 4, 6, 2, 4, 2], 2.5)
    ]

    for case in testcases:
        my_assert_arg(median, case[0], case[1])


def test_modes():
    testcases = [
        ([4, 2, 5, 8, 6], [2, 4, 5, 6, 8]),
        ([1, 3, 4, 6, 4, 2], [4]),
        ([1, 3, 4, 6, 2, 4, 2], [2, 4]),
        ([1, 3, 2, 4, 6, 2, 4, 2], [2])
    ]

    for case in testcases:
        my_assert_arg(modes, case[0], case[1])


def test_var():
    testcases = [
        ([4, 2, 5, 8, 6], 4.0),
        ([1, 3, 2, 4, 6, 2, 4, 2], 2.25)
    ]

    for case in testcases:
        my_assert_arg(var, case[0], case[1])


def test_std():
    testcases = [
        ([4, 2, 5, 8, 6], 2.0),
        ([1, 3, 2, 4, 6, 2, 4, 2], 1.5)
    ]

    for case in testcases:
        my_assert_arg(std, case[0], case[1])


def test_q1():
    testcases = [
        ([4, 2, 5, 8, 6], 3.0),
        ([1, 3, 4, 6, 4, 2], 2.0),
        ([1, 3, 5, 6, 1, 4, 2], 1.0),
        ([1, 3, 3, 5, 6, 2, 4, 1], 1.5)
    ]

    for case in testcases:
        my_assert_arg(q1, case[0], case[1])


def test_q3():
    testcases = [
        ([4, 2, 5, 8, 6], 7.0),
        ([1, 3, 4, 6, 4, 2], 4.0),
        ([1, 3, 5, 6, 2, 4, 1], 5.0),
        ([1, 3, 3, 5, 6, 2, 4, 1], 4.5)
    ]

    for case in testcases:
        my_assert_arg(q3, case[0], case[1])


def test_freq():
    testcases = [
        ([4, 2, 5, 8, 6], {2: 1, 4: 1, 5: 1, 6: 1, 8: 1}),
        ([1, 3, 4, 6, 4, 2], {1: 1, 2: 1, 3: 1, 4: 2, 6: 1}),
        ([1, 3, 5, 6, 2, 4, 1], {1: 2, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}),
        ([1, 3, 3, 5, 6, 2, 4, 1], {1: 2, 2: 1, 3: 2, 4: 1, 5: 1, 6: 1})
    ]

    for case in testcases:
        my_assert_arg(freq, case[0], case[1])


if __name__ == '__main__':
    try:
        print("\x1b[0;32m")

        test_mean()
        print("Je functie mean(lst) werkt goed!")

        test_rnge()
        print("Je functie rnge(lst) werkt goed!")

        test_median()
        print("Je functie median(lst) werkt goed!")

        test_q1()
        print("Je functie q1(lst) werkt goed!")

        test_q3()
        print("Je functie q3(lst) werkt goed!")

        test_var()
        print("Je functie var(lst) werkt goed!")

        test_std()
        print("Je functie std(lst) werkt goed!")

        test_freq()
        print("Je functie freq(lst) werkt goed!")

        test_modes()
        print("Je functie modes() werkt goed!")

        print("\nGefeliciteerd, alles lijkt te werken! Lever je werk nu in op Canvas...\n")


        def hist(freqs):
            v_min = min(freqs.keys())
            v_max = max(freqs.keys())

            histo = str()
            for i in range(v_min, v_max + 1):
                histo += "{:5d} ".format(i)
                if i in freqs.keys():
                    histo += "█" * freqs[i]
                histo += '\n'

            return histo


        print("\x1b[0;30m")
        s = input("Geef een reeks van gehele getallen (gescheiden door een spatie): ")
        userlst = [int(c) for c in s.split()]

        print("\nHet gemiddelde is {:.2f}".format(mean(userlst)))
        print("De modi zijn {}".format(modes(userlst)))
        print("De mediaan is {:.2f}".format(median(userlst)))
        print("Q1 is {:.2f}".format(q1(userlst)))
        print("Q3 is {:.2f}".format(q3(userlst)))

        print("Het bereik is {}".format(rnge(userlst)))
        print("De variantie is {:.2f}".format(var(userlst)))
        print("De standaardafwijking is {:.2f}".format(std(userlst)))

        print("\nHistogram (gekanteld):\n\n" + hist(freq(userlst)))

    except AssertionError as ae:
        print("\x1b[0;31m")
        print(ae)