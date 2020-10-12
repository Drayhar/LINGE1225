# TP1 - Programmation LSM
# Vincent Bauffe (en consultance) 2020-2021

# Exercice 1


def pair(nbr):
    if nbr < 2:
        return 0
    somme = 0
    for i in range(2, nbr, 2):
        print(i)
        somme += i
    return somme


assert pair(10) == 20
assert pair(-9) == 0

# Exercice 2


def carre(n):
    line = "*" * n
    for _ in range(n):
        print(line)


def triangle1(n):
    for i in range(1, n+1):
        print("*" * i)


def triangle2(n):
    for i in range(1, n+1):
        print(" " * (n-i) + "*" * i)


# Exercice 3

def fact(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    facto = n
    for i in range(1, n):
        facto *= (n-i)
    return facto


assert fact(6) == 720
assert fact(0) == 1
assert fact(-9) == None

# Exercice 4


def fibo(n):
    if n < 0:
        return 0
    if n <= 1:
        return n
    f1 = 0
    f2 = 1
    fn = 0
    for _ in range(1, n):
        fn = f1 + f2
        f1 = f2
        f2 = fn
    return fn


assert fibo(8) == 21
assert fibo(1) == 1
assert fibo(-5) == 0

# Exercice 5


def distance(m):
    if m <= 0:
        return 0
    distLune = 3844e8  # Conversion en mm
    n = 0
    while m < distLune:
        m *= 2
        n += 1
    return n


assert distance(0.1) == 42
assert distance(-1) == 0
