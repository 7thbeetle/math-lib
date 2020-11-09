pi = 3.141592653589793
e = 2.718281828459045

def square(i):  # square of a number
    return (i ** 2)

def cube(i):  # cube of a number
    return (i ** 2)

def sqrt(i):  # square root of a number
    return (i ** 0.5)

def exp(i):  # i power of e
    return e ** i


goldenRatio = round((1 + sqrt(5)) / 2, 10)
# golden ratio ~= 1,61803
# sqrt(5) + 1
# ----------
#     2


def root(x, i = 2):  # i root of x
    return (x ** (1 / i))


def factorial(x):  # calculates factoral, duh!
    f, i = 1, 1
    while i <= x:
        f *= i
        i += 1
    if x == 0:
        f = 0
    if x < 0:
        raise ArithmeticError
    return int(f)


def isPrime(n):  # checks if a number is a Prime number or not
    l = range(2, n // 2 + 1)
    prime = True
    for i in l:
        if (n % i) == 0:
            prime = False
            break
    if n <= 1:
        prime = False
    return prime


def secondDegree(a, b, c):  # makes a list that includes x1 and x2
    sq = sqrt(square(b) - (4 * a * c))
    xFirst = ((b * -1) + sq) / 2 * a
    xSecond = ((b * -1) - sq) / 2 * a

    # ((b * -1) +- sq
    # ------------------------
    # 2 * a

    return [xFirst, xSecond]


def circleArea(r, piLen = 2):  # a circle's area (piLen is digits after point)
    newPi = round(pi, piLen)
    return newPi * (r ** 2)


def circleCircum(r, piLen = 2):  # a cirle's circumference (piLen is digits after point)
    newPi = round(pi, piLen)
    return 2 * newPi * r


def fibonacci(t):  # t fibonacci numbers in a list
    a, b, i = 1, 1, 0
    fib = [0]
    
    while i != (t // 2):
        fib.append(a)
        a += b
        fib.append(b)
        b += a
        i += 1
    
    if t % 2 == 0:
        fib.pop()
    
    return fib


def spheresVolume(r, piLen = 2):  # calculates sphere's volume
    #  4 * pi * (r ** 3)
    # -------------------
    #         3
    newPi = round(pi, piLen)
    return 4 * newPi * (r ** 3) / 3


def cylinderVolume(r, h, piLen = 2):  # calculates volume of the cylinder
    # pi * h * (r ** 2)
    newPi = round(pi, piLen)
    return newPi * h * (r ** 2)


def ellipseCircum(a, b, piLen = 2):  # calculates circumference of the ellipse, which is messy
    # 2pi * sqrt(
    #   (a**2 + b**2)
    # -----------------
    #        2
    # )
    newPi = round(pi, piLen)
    inSqrt = ((a ** 2) + (b ** 2)) / 2
    return 2 * newPi * sqrt(inSqrt)


# -----------------------------------------------

# i'm not proud of that section
import math

def log(x, base = e):  # logarithm, base is optional (base = e)
    return math.log(x, base)

def ln(x):  # ln logarithm, base is e
    return math.log(x, e)

def log10(x):  # 10 based logarithm
    return math.log10(x)

def log2(x):  # 2 based logarithm
    return math.log2(x)

# -----------------------------------------------


def perm(n, r):  # basic permutation
    #       n!
    # ---------------
    #    (n - r)!
    if n == r:
        p = 1
    else:
        p = factorial(n) / factorial(n - r)
    return int(p)


def comb(n, k):  # basic combination
    #       n!
    # ---------------
    #  k! * (n - k)!
    if n == k:
        c = 1
    else:
        c = factorial(n) / (factorial(k) * factorial(n - k))
    return int(c)


def absoluteValue(x):  # i think you can read
    if x >= 0:
        pass
    else:
        x *= -1
    return x


def pyth(a, b):  # pythagoras
    return sqrt(square(a) + square(b))


def avarage(list):  # calculates avarage of the giving list
    top = 0
    for i in list:
        top += i
    return top / len(list)


def standardDevitation(list):  # calculates the list's standard devitation
    ava = avarage(list)
    top = 0
    for i in list:
        top += square(i - ava)
    fin = top / (len(list) - 1)
    return round(sqrt(fin), 8)


## bignum / litnum = goldrat
def shortGold(x):  # the giving nuber is the little one, it gives you the big one
    return x * goldenRatio


def longGold(x):  # the giving nuber is the big one, it gives you the little one
    return x / goldenRatio


def totalGold(total):  # the giving one is sum of big one and little one, it gives you a list
    little = total / (goldenRatio + 1)
    big = total - little
    return [round(little, 10), round(big, 10)]


def listPrimes(b):  # makes a list of prime numbers between a and b
    between = range(1, b)
    primes = []
    for i in between:
        if isPrime(i) == True:
            primes.append(i)
    return primes

def primeDivisiors(x):  # makes a list with that numbers all prime factors
    primes = listPrimes(x // 2 + 2)
    factors = []
    for i in primes:
        while x % i == 0:
            factors.append(i)
            x /= i
    return factors


def distance(a, b, c, d):  # distance from a,b location to c,d location
    x = absoluteValue(a - c)
    y = absoluteValue(b - d)
    return pyth(x, y)

def radian(a):  # turns degree to radian
    return a / pi

def degree(a):
    return a * pi


def ceil(x):  # Return the ceiling of x as integer, the smallest integer value greater than or equal to x
    if x % 1 != 0:
        x = x - (x % 1) + 1
    return int(x)

def floor(x):
    return int(x)

# -----------------------------------------------

def gcd(a, *b):  # greatest common divisor
    divs = primeDivisiors(a)
    temp = []
    x = 1
    for each in b:
        for prime in divs:
            if each % prime == 0:
                each //= prime
                temp.append(prime)
        divs = temp
        temp = []
    
    for i in divs:
        x *= i
    
    return int(x)

# -----------------------------------------------

def hcf(a, *b):  # highest common factor
    bs = []
    bf = 1
    for i in b:
        bs.append(i)
    
    for i in bs:
        bf *= i
    
    x = a
    for i in b:
        x = gcd(x, i)
    
    return a * bf / x

# -----------------------------------------------

