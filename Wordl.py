import csv
import random as rand

state = [u'\u2B1B', u'\U0001F7E8', u'\U0001F7E9']

# Initialise the game by loading the list of word and choosing one randomly
def initGame(settings):
    word_list = loadList(settings[0])

    guess_state = []
    for i in range(settings[0]):
        guess_state.append(0)
    
    guess_word = randomWord(word_list)

    return guess_word, guess_state, word_list

# Start the game loop
def game(settings):
    guess_word, guess_state, word_list = initGame(settings)

    printState(guess_state)
    
    for i in range(settings[1]):
        word = askWord(settings, word_list)
        guess_state = wordCheck(word, guess_word)
        printState(guess_state)
        win = hasWin(guess_state)
        if (win):
            print("Vous avez gagne!")
            break
    
    if not win:
        print(f"Vous avez perdu, le mot etait {guess_word}!")

# Ask the user how long the word should be
# and how many try he want
def gameSettings():
    length_word = int(input("Avec quelle longueur de mot voulez-vous jouer? (5-20): "))
    tries = int(input("Combien d'essais voulez-vous avoir? (0<): "))
    return (length_word, tries)

# Ask the user if he want to replay
def replay():
    replay = input("Voulez-vous jouer une autre partie? (Y/N): ")
    return replay in ['Y', 'y', 'Yes', 'yes', 'o', 'oui']

# Check if the letters of the user's word match the guess word.
# Green if letter is in the word and in the right position
# Yellow if letter is in the word
# Gray if letter is not in the word
def wordCheck(word, guess_word):
    guess_word_mask = list(guess_word)
    guess_state = greenCheck(word, guess_word_mask)
    yellowCheck(word, guess_word_mask, guess_state)
    return guess_state

# Check for green letters
def greenCheck(word, mask_word):
    guess_state = []
    for i in range(len(word)):
        guess_state.append(0)
        for j in range(len(mask_word)):
            if word[i] == mask_word[j] and i==j:
                guess_state[i] = 2
                mask_word[j] = '_'
                break
    return guess_state

# Check for yellow letters
def yellowCheck(word, mask_word, guess_state):
    for i in range(len(word)):
        for j in range(len(mask_word)):
            if word[i] == mask_word[j] and guess_state[i] != 2:
                guess_state[i] = 1
                mask_word[j] = '_'
                break

# Print the state of the guess word
def printState(guess_state):
    for el in guess_state:
        print(state[el], end = '')
    print('')

# Ask the user to guess the word
# Ask again if the word is not of the right length or is not a French word
def askWord(setting, word_list):
    word = input()
    if len(word) != settings[0]:
        print("ERREUR: La longueur du mot est incorrecte!")
        return askWord(setting, word_list)
    elif not ([word] in word_list):
        print("ERREUR: Ce mot n'est pas francais!")
        return askWord(setting, word_list)

    return word

# Check if the user has win
def hasWin(guess_state):
    return all(x==2 for x in guess_state)

# Load the list of word that has the right length
def loadList(length_word):
    with open(f'mot_{length_word}.csv', 'r') as mots:
        word_list = list(csv.reader(mots))
    return word_list

# Pick a random word in the list
def randomWord(word_list):
    return rand.choice(word_list)[0]

# Main game loop
if __name__ == '__main__':
    while True:
        settings = gameSettings()
        game(settings)
        if (not replay()):
            break
