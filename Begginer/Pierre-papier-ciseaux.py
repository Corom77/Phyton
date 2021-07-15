import random 
ordi_points = 0
player_points = 0
nb_manche = 0

def start_function():
    global nb_manche
    nb_manche = int(input("Combien de manche voulez-vous jouer?"))
    who_win()

def random_choice():
    return random.randint(1,3)

def number_to_sign(number):
    if number == 1:
        return "Pierre"
    elif number == 2:
        return "Ciseaux"
    else:
        return "Feuille"

def check_win(ordi,player,nb_manche):
    if ordi >= nb_manche:
        print(f"L'ordinateur à gagné.L'ordi a {ordi} points et vous avez {player} points.")
        exit()
    elif player>=nb_manche:
        print(f"Vous avez gagné.L'ordi a {ordi} points  et vous avez {player} points.")
        exit()
    else:
        print(f"L'ordinateur à {ordi} points , et vous avez {player} points.")
        who_win()


def who_win():
    global ordi_points,player_points,nb_manche
    ordiChoice = number_to_sign(random_choice()) 
    userChoice = str(input("Quel est le signe que vous voulez jouer?"))

    #@dev Pierre Cases
    if ordiChoice == "Pierre" and  userChoice == "ciseaux":
        print(f"L'ordinateur a joué {ordiChoice}. Vous avez perdu.")
        ordi_points +=1
       
    if ordiChoice == "Pierre" and  userChoice == "feuille":
        print(f"L'ordinateur a joué {ordiChoice}. Vous avez gagné.")
        player_points +=1
        
    if ordiChoice == "Pierre" and  userChoice == "pierre":
        print(f"L'ordinateur a joué {ordiChoice}. Vous êtes donc à equalité.")
    
    #@dev Ciseaux Cases
    if ordiChoice == "Ciseaux" and  userChoice == "feuille":
        print(f"L'ordinateur a joué {ordiChoice}. Vous avez perdu.")
        ordi_points +=1
        
    if ordiChoice == "Ciseaux" and  userChoice == "pierre":
        print(f"L'ordinateur a joué {ordiChoice}. Vous avez gagné.")
        player_points +=1

    if ordiChoice == "Ciseaux" and  userChoice == "ciseaux":
        print(f"L'ordinateur a joué {ordiChoice}. Vous êtes donc à equalité.")

    
    #@dev Feuille Cases
    if ordiChoice == "Feuille" and  userChoice == "pierre":
        print(f"L'ordinateur a joué {ordiChoice}. Vous avez perdu.")
        ordi_points +=1
  
    if ordiChoice == "Feuille" and  userChoice == "ciseaux":
        print(f"L'ordinateur a joué {ordiChoice}. Vous avez gagné.")
        player_points +=1
 
    if ordiChoice == "Feuille" and  userChoice == "feuille":
        print(f"L'ordinateur a joué {ordiChoice}. Vous êtes donc à equalité.")
    check_win(ordi_points,player_points,nb_manche)

start_function()
