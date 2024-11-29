from random import *
n = randint(0, 100)
essais = 1
u = -1

while u != n and essais < 8:
    entree = input("À quel nombre vous pensez ? ")
    
    if not entree.isdigit():
        print("Erreur : Veuillez entrer uniquement des chiffres.")
        continue
    
    u = int(entree)
    essais = essais + 1
    
    if u > n:
        print("Le nombre est plus petit")
    elif u < n:
        print("Le nombre est plus grand")

if u == n:
    print("Tu as GAGNER !!!!!")
else:
    print("Tu as PERDU !!!!!")
