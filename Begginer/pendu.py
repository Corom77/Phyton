import random
lives_visual_dict = {
        0: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / \\
               |
           """,
        1: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / 
               |
            """,
        2: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |          
               |
            """,
        3: """
                ___________
               | /        | 
               |/        ( )
               |          
               |          
               |
            """,
        4: """
                ___________
               | /        | 
               |/        
               |          
               |          
               |
            """,
        5: """
                ___________
               | /        
               |/        
               |          
               |          
               |
            """,
        6: """
               |
               |
               |
               |
               |
            """,
        7: "",
    }
words = ["abricot"]
word = random.choice(words).upper()
word_letter = []
reveal_letter = []
len_letter = len(word)
for letter in word:
    word_letter.append(letter)
    reveal_letter.append('*')
lives = 7


def pendu():
    global word_letter,lives,reveal_letter,lives_visual_dict,word,len_letter
    used_letter = []
    while lives != 0 and len_letter !=0:
        user_letter = str(input("Quelle est votre lettre?")).upper()
        if user_letter in word_letter:
            used_letter.append(user_letter)
            temp_letter = []
            index = 0
            for letter in word_letter:
                if letter == user_letter:
                    temp_letter.append(index)
                index+=1
            for pl_index in temp_letter:
                reveal_letter[pl_index]=user_letter
            print(f"C'est une bonne réponse.\n{reveal_letter}.\n Pour rapel vous avez déjà dit {used_letter}.")
            len_letter-=1
        else:
            used_letter.append(user_letter)
            lives-=1
            print(lives_visual_dict[lives])
            print(f"C'est une mauvaise réponse.\n{reveal_letter}.\n Pour rapel vous avez déjà dit {used_letter}.")
    if lives == 0:
        print(f"Tu as perdu le mot était: {word}")
        exit()
    else:
        print("Bravo tu as gagné!")
        exit()
pendu()
