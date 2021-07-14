import random
#Initialisation du jeu.
x = int(input("Jusqu'a combien de chifre voulez-vous jouer?"))
result = random.randint(1,x)
respond = 0
nb_tentative = 0

#On joue jusqu'à temps que le joueur trouve la bonne réponse.
while respond!= result:
    respond = int(input("Quel est le chifre auquel vous pensez?"))
    nb_tentative +=1

#Boucles pour l'orthographe singulier/pluriel du mot "tentative".
if nb_tentative == 1:
    print(f"Super vous avez trouvé {result} en {nb_tentative} tentative, et c'est la bonne réponse.")
else
    print(f"Super vous avez trouvé {result} en {nb_tentative} tentatives, et c'est la bonne réponse.")
