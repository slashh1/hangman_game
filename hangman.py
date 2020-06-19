# Write your code here
import random
print('H A N G M A N\n')
lis = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(lis)
set_inp = set(word)
output_display = list('-'*len(word))
entered_letters = set()


def game():
    i = 0
    while i < 8:
        print(''.join(output_display))
        letter = input('Input a letter: ')
        if letter == 'exit':
            return -1
        if not len(letter) == 1:
            print('You should input a single letter')
        elif not (letter.islower() and letter.isalpha()):
            print('It is not an ASCII lowercase letter')
        elif letter in entered_letters:
            print('You already typed this letter')
        elif letter in set_inp:
            countval = word.count(letter)
            x = -1
            while(countval > 0):
                # insert char in position
                x = word.index(letter, x+1)
                output_display[x] = letter
                countval -= 1
            if '-' not in output_display:
                print('\n'+''.join(output_display))
                print('You guessed the word!')
                print('You survived!')
                break
        else:
            print('No such letter in the word')
            i += 1
            if i >= 8:
                break
        entered_letters.add(letter)
        print('\n')
    if i >= 8:
        print('You are hanged!')


    # program should also consider non present charechters typed twice and not take off turn
while(True):
    stop = input('Type "play" to play the game, "exit" to quit:')
    if stop == 'exit':
        break
    if stop == 'play':
        retval = game()
        if retval == -1:
            break
        word = random.choice(lis)
        set_inp = set(word)
        output_display = list('-'*len(word))
        entered_letters = set()
