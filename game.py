import random
from hangman import draw_hanged_man
from words import words

lives=6
wrong_guesses=0

words=[word.lower() for word in words]

word=random.choice(words)
print("Your word is {}".format(word))
blank_list=[]
for blank in range(len(word)):
    blank_list.append("_")





while "_" in blank_list and lives!=0:
    letter=input("Guess a letter: \n")
    letter=letter.lower()
    if letter in word:
        for character in word:
            if letter==character:
                index=word.index(character)
                blank_list[index]=letter
                print(blank_list)
    else:
        lives=lives-1
        wrong_guesses+=1
        draw_hanged_man(wrong_guesses)
        if lives==0:
            print("You lose!")
if lives!=0:
    print("Congratulations! You won. Your word is {}".format(word))



