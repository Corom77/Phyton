'''
@Title Guess my number
@author Familybubu
@notice Think to a number and the computer will try to find it.
'''

#@dev Importation des modules.
import random

#Initialisation
start = True
nb_max = 0
nb_alea = []
nb_tentative = 0 

#@dev Fonction qui permet de compter le nombre d'élements dans une liste.
#@param LE nom de la liste à compter.
#@return Le nombre d'élement dans la liste.
def count_list(list_name):
    c=0
    for n in list_name:
        c+=1
    return c

#@dev Fonction qui permet de démarer le jeu.
def start_function():
    global start
    global nb_max
    global nb_alea
    if start == True:
        nb_max = int(input("Entre 0 et quel chifre voulez vous jouer?"))
        for n in range(0, nb_max+1):
            nb_alea.append(n)
        guess()
    else:
        return ""

#@dev Fonction qui permet de générer un nombre aléatoire.
#@param Le nombre maximum.
#@return Le nombre aléatoire compris entre 0 et le nombre maximum.
def randomnumber(nb_max):
    global nb_alea
    print(nb_alea)
    x = random.randint(0,count_list(nb_alea)-1)
    return xx
    
#@dev Fonction qui permet de dire à l'utilisateur quel nombre l'ordinateur à penser.  
def guess():
    global start
    global nb_max
    global nb_alea
    global nb_tentative
    start = False
    good = ["Yes","yes","y","Y","O","o","Oui","OUI","oui"]
    result = "Non"
    aa = randomnumber(nb_max)
    while result not in good:
        print(f"Je pense à {aa}.")
        nb_alea.remove(aa)
        result = str(input("Est-ce le bon nombre?"))
        if result in good:
            if nb_tentative == 1:
                print(f"L'ordinateur a trouvé le bon nombre en {nb_tentative} tentative!")
            else:
                print(f"L'ordinateur a trouvé le bon nombre en {nb_tentative} tentatives!")

            exit()
        else:
            nb_tentative+=1
            guess()

start_function()
