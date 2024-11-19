#Naam: Merry Ashji
#Klas: V1Q
#Studentnummer:1764739

def floor(real):
    """ Retourneert het grootste gehele getal (int), dat kleiner dan of gelijk is aan real (float). """
    if (real>=0 ):
        return (int(real))
    elif (real==int(real)):
        return int(real)
    else:
        return (int(real))-1

def ceil(real):
    """ Retourneert het kleinste gehele getal (int), groter dan of gelijk aan real (float). """
    if (real<0 ):
        return (int(real))
    elif (real==int(real)):
        return int(real)
    else:
        return (int(real))+1

def div(n):
    """ Retourneert een (natuurlijk) gesorteerde verzameling (list) van delers van n (int)."""
    divisors =[]
    for i in range(1,n+1):
        if n%i == 0:
           divisors.append(i)
    return sorted(divisors)


def is_prime(n):
    """ Return True als n (int) een priemgetal is, anders False. """
    divisors =[]
    if n<=1:
        return False
    for i in range(1,n+1):
        if n%i == 0:
           divisors.append(i)
           x= len(divisors)
    if x<=2:
        return True
    else:
        return False


def primes(num):
    """ Return alle priemgetallen kleiner dan num (int). """
    list=[]
    for i in range (1, num):
        if is_prime(i) == True:
            list.append(i)

    return list



def prime_factors(n):
    """ Return een (natuurlijk) gesorteerde verzameling (list) van priemfactoren van n (int)
    Return [n] als n een priemgetal is, of wanneer n == 1."""
    i = 2
    factors = []
    while i * i <= n:
        if (n % i)!=0:
            i += 1
        else:
            n =n//i
            factors.append(i)
    if n >= 1:
        factors.append(n)
    return factors



def gcd(a, b):
    """ Return de grootste grootste gemene deler , ggd (ofwel greatest common divisor, gcd) (int) van
    natuurlijke getallen a en b (beide int)."""
    while b!=0:
        (a,b) = (b, a % b)
    return (a)


def lcm(a, b):

   x=gcd(a,b)
   y=(a*b)//x
   return (y)



def add_frac(n1, d1, n2, d2):

   if d1==d2:
       n3=n1+n2
       return (n3,d1)
   else:
       d3=lcm(d1,d2)
       x=d3//d1
       y=d3//d2
       n3= ((n1*x)+(n2*y))
       return ((n3),(d3))


def my_assert_args(function, args, expected_output):
   argstr = str(args).replace(',)', ')')

   assert function(*args) == expected_output, \
\
       f"Fout: {function.__name__}{argstr} geeft {function(*args)} in plaats van {expected_output}"


def test_floor():
   testcases = [((1.0,), 1),

                ((1.05,), 1),

                ((1.95,), 1),

                ((-1.0,), -1),

                ((-1.05,), -2),

                ((-1.95,), -2)]

   for case in testcases:
       my_assert_args(floor, case[0], case[1])


def test_ceil():
   testcases = [((1.0,), 1),

                ((1.05,), 2),

                ((1.95,), 2),

                ((-1.0,), -1),

                ((-1.05,), -1),

                ((-1.95,), -1)]

   for case in testcases:
       my_assert_args(ceil, case[0], case[1])


def test_div():
   testcases = [

       ((1,), [1]),

       ((2,), [1, 2]),

       ((3,), [1, 3]),

       ((4,), [1, 2, 4]),

       ((8,), [1, 2, 4, 8]),

       ((12,), [1, 2, 3, 4, 6, 12]),

       ((19,), [1, 19]),

       ((25,), [1, 5, 25]),

       ((929,), [1, 929]),

       ((936,), [1, 2, 3, 4, 6, 8, 9, 12, 13, 18, 24, 26, 36, 39, 52, 72, 78, 104, 117, 156, 234, 312, 468, 936])

   ]

   for case in testcases:
       my_assert_args(div, case[0], sorted(case[1]))


def test_is_prime():
   testcases = [

       ((1,), False),

       ((2,), True),

       ((3,), True),

       ((4,), False),

       ((5,), True),

       ((6,), False),

       ((29,), True)

   ]

   for case in testcases:
       my_assert_args(is_prime, case[0], case[1])


def test_primefactors():
   testcases = [

       ((1,), [1]),

       ((2,), [2]),

       ((3,), [3]),

       ((4,), [2, 2]),

       ((8,), [2, 2, 2]),

       ((12,), [2, 2, 3]),

       ((2352,), [2, 2, 2, 2, 3, 7, 7]),

       ((9075,), [3, 5, 5, 11, 11])

   ]

   for case in testcases:
       my_assert_args(prime_factors, case[0], sorted(case[1]))


def test_primes():
   testcases = [

       ((1,), []),

       ((2,), []),

       ((3,), [2]),

       ((4,), [2, 3]),

       ((5,), [2, 3]),

       ((6,), [2, 3, 5]),

       ((30,), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

   ]

   for case in testcases:
       my_assert_args(primes, case[0], sorted(case[1]))


def test_gcd():
   testcases = [

       ((60, 70), 10)

   ]

   for case in testcases:
       my_assert_args(gcd, case[0], case[1])


def test_lcm():
   testcases = [

       ((15, 27), 135)

   ]

   for case in testcases:
       my_assert_args(lcm, case[0], case[1])


def test_add_frac():
   testcases = [

       ((1, 2, 1, 4), (3, 4)),

       ((3, 4, 1, 6), (11, 12)),

       ((1, 6, 3, 4), (11, 12))

   ]

   for case in testcases:
       my_assert_args(add_frac, case[0], case[1])


if __name__ == '__main__':

   try:

       print("\x1b[0;32m")

       test_floor()

       print("Je functie floor() werkt goed!")

       test_ceil()

       print("Je functie ceil() werkt goed!")

       test_div()

       print("Je functie div(n) werkt goed!")

       test_is_prime()

       print("Je functie is_prime(n) werkt goed!")

       test_primefactors()

       print("Je functie primefactors(n) werkt goed!")

       test_primes()

       print("Je functie primes() werkt goed!")

       test_gcd()

       print("Je functie gcd(a, b) werkt goed!")

       test_lcm()

       print("Je functie lcm(a, b) werkt goed!")

       test_add_frac()

       print("Je functie add_frac(n1, d1, n2, d2) werkt goed!")

       print("Gefeliciteerd, alles lijkt te werken! Lever je werk nu in op Canvas...")



   except AssertionError as ae:

       print("\x1b[0;31m")

       print(ae)