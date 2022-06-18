import Cube, random

char_list = list()
underlines = list()
counter = 6
temp = 0
win = False

game_list = ["father", "mother", "brother", "sister", "uncle", "aunt"]
game_word = random.choice(game_list)

print("\n\n\n\n\n\n\n\n\n")

for x in range(0, len(game_word)): 
    char_list.append(game_word[x])
    underlines.append("__")

print(underlines)
word_count = len(char_list)

def find_words():
    global counter, word_count, temp
    if words in char_list:
        print("Got one")
        word_count = word_count - 1
        temp = char_list.index(words)
        underlines[temp] = words
        print(underlines)


    else:
        print("Nope")
        counter = counter - 1
        print(underlines)

def check():
    global counter, win, word_count
    if(counter == 6): 
        Cube.hanger()
    if(counter == 5): 
        Cube.hanger_head()
    if(counter == 4):
        Cube.hanger_body()
    if(counter == 3):
        Cube.hanger_hand()
    if(counter == 2):
        Cube.hanger_hands()
    if(counter == 1):
        Cube.hanger_leg()
    if(counter == 0): 
        Cube.hanger_legs()
        win = True
        print("Game Over :(")
        print("The answer was " + game_word)
    if(word_count == 0):
        print("Congrats, you won the game")
        win = True

while win == False: 
    words = Cube.gather()
    find_words()
    check()


