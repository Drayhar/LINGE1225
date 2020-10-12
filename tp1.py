# TP1 - Programmation LSM
# Vincent Bauffe (en consultance) 2020-2021

from math import pi

# Exercice 1


def heure(secondes):
    # Ici on utilise la division entière "//" et on récupère le reste
    # de la division avec "%"
    heures = secondes // 3600
    minutes = (secondes % 3600) // 60
    secondes = (secondes % 3600) % 60
    # C'est une manière de formater une string, sinon on aurait pu utiliser :
    # print(heure + " heures" + minutes + " minutes" + secondes + " secondes")
    print(f"{heures} heures, {minutes} minutes et {secondes} secondes")


# Exercice 2

def moyenne(arg1, arg2):
    return (arg1 + arg2) / 2


def main():
    # On peut passer un message directement dans la demande d'input. On assigne
    # ensuite la valeur rentrée à une variable
    arg1 = input("Entrez le premier nombre :")
    arg2 = input("Entrez le premier nombre :")
    # On réutilise la fonction d'avant
    mean = moyenne(float(arg1), float(arg2))
    # De nouveau, format rapide, une autre option est
    # print("La moyenne est : {}".format(mean))
    print(f"La moyenne est : {mean}")

# Exercice 3


def volume(arg1):
    return 4 * pi * arg1**3 / 3


def surface(arg1):
    return 4 * pi * arg1**2

# Exercice 4


def max():
    a = int(input("Veuillez entrer une première valeur"))
    b = int(input("Veuillez entrer une seconde valeur"))
    c = int(input("Veuillez entrer une troisième valeur"))

    # On teste des conditions l'une après l'autre. Le "and" signifie que
    # les deux conditions doivent être remplies en même temps. Un "or"
    # se satisfait d'une seule des deux conditions ou des deux
    if a >= b and a >= c:
        max = a
    elif b >= a and b >= c:
        max = b
    elif c >= a and c >= b:
        max = c

    print(f"Le maximum est {max}")

    if a == b or a == c or b == c:
        print("Mais vous avez introduit des valeurs identiques !")

# Exercice 5


def amende(vmax, v):
    # On prend la valeur absolue pour être sûr
    depassement = abs(vmax - v)
    fine = 5 * depassement
    # Deux "if" en série, attention à ne pas utiliser "elif" ! Parce
    # qu'on doit tester les deux cas
    if fine < 12.5:
        fine = 12.5
    if depassement > 10:
        fine *= 2
    return fine + 1


# Des tests rapides, tant que la condition est remplie il ne se passe rien,
# dans le cas contraire, ça renvoie une erreur. On peut personnaliser le message
assert amende(50, 62) == 120, "La valeur renvoyée n'est pas bonne"
assert amende(50, 51) == 12.5
