# TP1 - Programmation LSM
# Vincent Bauffe (en consultance) 2020-2021

# Exercice 1


def nbr_mot(mot):
    listeMot = mot.strip().split(" ")
    nbr = 0
    for mot in listeMot:
        if mot != "":
            nbr += 1
    return nbr


assert nbr_mot("Ceci est une chaîne de caractères") == 6
assert nbr_mot("Ceci") == 1
assert nbr_mot(" ") == 0
assert nbr_mot(" a     b ") == 2

# Exercice 2


def anagramme(str1, str2):
    if len(str1) != len(str2):
        return False
    for letter in str1:
        if not letter in str2:
            return False
    return True


assert anagramme("maire", "aimer") == True
assert anagramme("maire", "mari") == False
assert anagramme("maire", "mpire") == False
assert anagramme("maire", "marie") == True
assert anagramme("maire", "marie   ") == False

# Exercice 3


def changer(str):
    newStr = ""
    for i in str:
        if i == "r":
            newStr += "l"
        else:
            newStr += i
    return newStr


strIn = "Et ce grand dragon, cet ancien serpent"
strOut = "Et ce gland dlagon, cet ancien selpent"
assert changer(strIn) == strOut

# Exercice 4


def miroir(mot):
    return mot[::-1]


assert miroir("Tp3 LINGE1225") == "5221EGNIL 3pT"


# Exercie 5

def verifierMul(l, n):
    if n == 0:
        return True
    for nbr in l:
        if nbr % n != 0:
            return False
    return True


l = [0, 7, 14, 21]
assert verifierMul(l, 7) == True
assert verifierMul(l, 2) == False
assert verifierMul(l, 0) == True

# Exercice 6


def merge_two_lists(lst1, lst2):
    merged = []
    size1, size2 = len(lst1), len(lst2)
    i, j = 0, 0

    while i < size1 and j < size2:
        if lst1[i] <= lst2[j]:
            merged.append(lst1[i])
            i += 1
        else:
            merged.append(lst2[j])
            j += 1

    merged += lst1[i:] + lst2[j:]
    return merged


lst1 = [1, 3, 5, 7, 8, 8]
lst2 = [2, 4, 6, 8]
assert merge_two_lists(lst1, lst2) == [1, 2, 3, 4, 5, 6, 7, 8, 8, 8]


# Exercice 1 sup

def tribulles(l):
    n = len(l)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l


l = [1, 9, 3, 8, 4, 2]
assert tribulles(l) == [1, 2, 3, 4, 8, 9]
