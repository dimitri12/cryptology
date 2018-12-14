# Vigenère Cipher 
# controller.py
# Created by Mauro J. Pappaterra on 22 of January 2018.
import sys
import codecs
from pathlib import Path

# GLOBAL VARIABLES
transposition = False
substitution = False
shifter = False
vigenere = True

frequency_data = []

MAX_LENGTH = 16 # length of key max constant
MIN_LENGTH = 2 # length of key min constant

# MAIN PROGRAM METHOD / START SCREEN
def start(m,v):

    exit = False
    while (not exit):

        print(v.welcome)
        print(v.instructions)

        read = input().lower()

        while (read != 's' and read != 'q'):
            print (v.error_start)
            read = input().lower()

        if (read == 's'):
            exit = main(m,v)

        if (read == 'q'):
            exit = True # quit

    print (v.exit)

# MAIN MENU
def main (m,v):
    print(v.menu)

    read = input().lower()
    while (read != '1' and read != '2' and read != '3' and read != '4'  and read != '5' and read != 'q'):
        print (v.error_input)
        read = input().lower()

    if (read == '1'):
        return encrypt(m,v)
    elif (read == '2'):
        return decrypt(m,v)
    elif (read == '3'):
        return crack(m,v)
    elif (read == '4'):
        return cipher(m,v) # cipher menu
    elif (read == '5'):
        return about(m,v) # about page
    elif (read == 'q'):
        return True # quit

# ABOUT PAGE
def about(m,v):

    print (v.about)

    read = input().lower()
    while (read != 'b' and read != 'q'):
        print (v.error_input)
        read = input().lower()

    if (read == 'b'):
        return main(m,v) # main menu
    elif (read == 'q'):
        return True # quit

# ENCRYPT MENU
def encrypt (m,v):
    print (v.encrypt_menu)

    read = input().lower()
    while (read != '1' and read != '2' and read != '3' and read != 'b' and read != 'q'):
        print(v.error_input)
        read = input().lower()

    if (read == '1' or read == '2'):

        if (read == '1'):
            text = text_input(m,v) # input text from console
        else:
            text = external_file(m,v) # input text from external file

        if (len(text) == 0): # workaround to avoid empty input
            print(v.error_empty)
            return encrypt(m,v)

        # choose encryption method
        if (transposition): # encrypt using transposition cipher
            encryption = m.transposition(text)
            return print_output(m, v, encryption, True)

        elif (substitution): # encrypt using substitution cipher
            encryption = m.substitution_encrypt(text)
            return print_output(m, v, encryption, True)

        elif (shifter): # encrypt using shifter cipher
            char_set = choose_alphabet(m,v) # choose alphabet
            number = int_input(m,v) # choose k

            encryption = m.shift_encrypt(text,number, char_set)
            return print_output(m, v, encryption, True)

        elif (vigenere): # encrypt using vigenère cipher
            char_set = choose_alphabet(m, v)  # choose alphabet
            key = key_input(m, v)  # choose key

            encryption = m.vigenere_encrypt(text, key, char_set)
            return print_output(m, v, encryption, True)

    elif (read == '3'):
        return cipher(m,v) # change cipher menu
    elif (read == 'b'):
        return main(m,v) # main menu
    elif (read == 'q'):
        return True # quit

# DECRYPT MENU
def decrypt (m,v):
    print (v.decrypt_menu)

    read = input().lower()
    while (read != '1' and read != '2' and read != '3' and read != 'b' and read != 'q'):
        print(v.error_input)
        read = input().lower()

    if (read == '1' or read == '2'):
        if (read == '1'):
            text = text_input(m,v) # input text from console
        else:
            text = external_file(m,v) # input text from external file

        if (len(text) == 0): # workaround to avoid empty input
            print(v.error_empty)
            return decrypt(m,v)

        if (len(text) == 0): # workaround to avoid empty input
            print(v.error_empty)
            return decrypt(m,v)

        # choose decryption method
        if (transposition):  # decrypt using transposition cipher
            decryption = m.transposition(text)
            return print_output(m, v, decryption, False)

        elif (substitution): # decrypt using substitution cipher
            decryption = m.substitution_decrypt(text)
            return print_output(m, v, decryption, False)

        elif (shifter): # decrypt using shifter cipher
            char_set = choose_alphabet(m, v)
            number = int_input(m, v)

            decryption = m.shift_decrypt(text, number, char_set)
            return print_output(m, v, decryption, False)

        elif (vigenere): # decrypt using vigenère cipher
            char_set = choose_alphabet(m, v)  # choose alphabet
            key = key_input(m, v)  # choose key

            decryption = m.vigenere_decrypt(text, key, char_set)
            return print_output(m, v, decryption, False)

    elif (read == '3'):
        return cipher(m,v) # cipher menu
    elif (read == 'b'):
        return main(m,v) # main menu
    elif (read == 'q'):
        return True # quit

# CRACK MENU
def crack (m,v):
    cipher_text = ''
    print(v.crack_menu)

    read = input().lower()
    while (read != '1' and read != '2' and read != 'b' and read != 'q'):
        print(v.error_input)
        read = input().lower()

    if (read == '1' or read == '2'):
        if (read == '1'):
            cipher_text = text_input(m,v) # input text from console
        else:
            cipher_text = external_file(m,v) # input text from external file

        if (len(cipher_text) == 0): # workaround to avoid empty input
            print(v.error_empty)
            return crack(m,v)

        char_set = choose_alphabet_crack(m, v)  # choose alphabet

        print(v.triagram_message)

        triagrams = m.find_triagrams(cipher_text)
        v.print_triagrams(triagrams)

        print(v.length_message)
        max_length = length_input(m, v)

        estimates = m.estimate_key_length(triagrams, max_length)
        v.print_lengths(estimates)

        print(v.guess_message)
        guess = guess_input(m,v,max_length)

        block = m.getBlock(cipher_text,guess) # break cipher into blocks and return calibration screen
        return (create_key(m, v, block, guess, char_set))

    elif (read == 'b'):
        return main(m, v)  # main menu
    elif (read == 'q'):
        return True  # quit

def create_key (m, v, cipher_as_blocks, key_length, char_set):
    key = []
    key_index = 0

    while (key_length > 0): # creates the empty key string
        key.append('-1') # flag for empty char space
        key_length -= 1

    index_string = m.getString(cipher_as_blocks, key_index)  # determines the letter key
    frequency = m.getFrequency(index_string, char_set)  # returns the fequency of all letters in such position

    swift = 0
    key[key_index] = char_set[swift]

    v.print_frequency_table(frequency, frequency_data, swift)
    v.print_key_index(key,key_index)

    print(v.calibrate_message)

    read = input().lower()
    while (read != '1' and read != '2' and read != '3' and read != '4' and read != '5' and read != 'b' and read != 'q'):
        print(v.error_input)
        read = input().lower()

    if (read == '1'):  # swift to the left
        swift -= 1
        return calibrate(m, v, cipher_as_blocks, key, key_index, swift, char_set)

    elif (read == '2'):  # swift to the right
        swift += 1
        return calibrate(m, v, cipher_as_blocks, key, key_index, swift, char_set)

    elif (read == '3'):  # previous letter
        swift = 0  # reset swift before changing key index
        key_index -= 1  # change key index

        if (key_index < 0):
            key_index = len(key) - 1  # wrap around
        return calibrate(m, v, cipher_as_blocks, key, key_index, swift, char_set)

    elif (read == '4'):  # next letter
        swift = 0  # reset swift before changing key index
        key_index += 1  # change key index

        if key_index >= len(key):  # wrap around
            key_index = 0
        return calibrate(m, v, cipher_as_blocks, key, key_index, swift, char_set)

    elif (read == '5'):  # change key length
        return change_key_size(m,v,cipher_as_blocks,char_set)

    elif (read == 'b'):
        return main(m, v)  # main menu
    elif (read == 'q'):
        return True  # quit

def calibrate (m,v, cipher_as_blocks, key, key_index, swift, char_set):
    done = True

    for chars in key:
        if (chars == '-1'):
            done = False

    index_string = m.getString(cipher_as_blocks, key_index)  # determines the letter in the block
    frequency = m.getFrequency(index_string, char_set)  # returns the fequency of all letters in such position

    key[key_index] = char_set[swift]

    v.print_frequency_table(frequency, frequency_data, swift)
    v.print_key_index(key, key_index)

    if (not done):
        print(v.calibrate_message)
    else:
        print(v.calibrate_message_done)

    read = input().lower()
    while (read != '1' and read != '2' and read != '3' and read != '4' and read != '5' and read != '6' and read != 'b' and read != 'q'):
        print(v.error_input)
        read = input().lower()

    if (read == '1'):  # swift to the left
        swift -= 1

        if (swift < 0):
            swift = len(char_set) - 1

        return calibrate(m, v, cipher_as_blocks, key, key_index, swift, char_set)

    elif (read == '2'):  # swift to the right
        swift += 1

        if (swift >= len(char_set)): #wraps around
            swift = 0
        return calibrate(m, v, cipher_as_blocks, key, key_index, swift, char_set)

    elif (read == '3'):  # previous letter
        key_index -= 1  # change key index

        if (key_index < 0):
            key_index = len(key) - 1 # wrap around

        if (key[key_index] == '-1'):  # if empty space
            swift = 0 # reset swift before changing key index only if no value is saved
        else:  # else find index of saved character
            for index, char in enumerate(char_set):
                if (key[key_index] == char):  # workaround to not reset frequencies already found
                    swift = index

        return calibrate(m, v, cipher_as_blocks, key, key_index, swift, char_set)

    elif (read == '4'):  # next letter
        key_index += 1  # change key index

        if key_index >= len(key): # wrap around
            key_index = 0

        if (key[key_index] == '-1'):  # if empty space
            swift = 0 # reset swift before changing key index only if no value is saved
        else:  # else find index of saved character
            for index, char in enumerate(char_set):
                if (key[key_index] == char):  # workaround to not reset frequencies already found
                    swift = index

        return calibrate(m, v, cipher_as_blocks, key, key_index, swift, char_set)

    elif (read == '5'):  # change key length
        return change_key_size(m,v,cipher_as_blocks,char_set)

    elif (read == '6'):  # use key
        if (done):
            print (v.use_key("".join(key)))
            decryption = m.vigenere_decrypt("".join(cipher_as_blocks), "".join(key), char_set)
            return print_output(m,v,decryption,False)
        else:
            print (v.error_incomplete)
            return calibrate(m, v, cipher_as_blocks, key, key_index, swift, char_set)

    elif (read == 'b'):
        return main(m, v)  # main menu
    elif (read == 'q'):
        return True  # quit

def change_key_size(m,v, cipher_as_blocks, char_set):
    cipher_text = ''.join(cipher_as_blocks)

    print(v.length_message)
    max_length = length_input(m, v)

    print (v.triagram_message)

    triagrams = m.find_triagrams(cipher_text)
    estimates = m.estimate_key_length(triagrams, max_length)
    v.print_lengths(estimates)

    print(v.guess_message)
    guess = guess_input(m, v, max_length)

    block = m.getBlock(cipher_text, guess)  # break cipher into blocks and return calibration screen
    return (create_key(m, v, block, guess, char_set))

# CIPHER MENU
def cipher (m,v):
    global transposition
    global substitution
    global shifter
    global vigenere

    print (v.cipher_menu)

    read = input().lower()
    while (read != '1' and read != '2' and read != '3' and read != '4' and read != 'b' and read != 'q'):
        print(v.error_input)
        read = input().lower()

    if (read == '1'): # Choose Transposition Cipher
        transposition = True
        substitution = False
        shifter = False
        vigenere = False
        print(v.transposition)
        return main(m,v) # main menu

    elif (read == '2'): # Choose Substitution Cipher
        transposition = False
        substitution = True
        shifter = False
        vigenere = False
        print(v.substitution)
        return main(m,v) # main menu

    elif (read == '3'):  # Choose Shifter Cipher
        transposition = False
        substitution = False
        shifter = True
        vigenere = False
        print(v.shifter)
        return main(m,v) # main menu

    elif (read == '4'):  # Choose Vigenère Cipher
        transposition = False
        substitution = False
        shifter = False
        vigenere = True
        print(v.vigenere)
        return main(m,v) # main menu

    elif (read == 'b'):
        return main(m,v) # main menu
    elif (read == 'q'):
        return True # quit

#INPUT FUNCTIONS

def text_input(m,v):
    """Get user input right in the console, return as single string"""
    text = ""
    line = ""

    print (v.input_text)

    while (line != "<done>"):
        line = input()
        text += line + "\n"

    return text[:-8]

def external_file(m,v):
    """Open and read an external .txt file, return as single string"""
    mode = "r"

    print (v.external_file)
    path = input()
    if (path == 'c'):
        print(v.cancel) # Cancel by user
        return encrypt (m,v) # Encrypt menu
    path = Path(path)

    while (not path.is_file()):
       path = input(v.error_path)
       if (path=='c'):
           print(v.cancel) # Cancel by user
           return encrypt (m,v) # Encrypt menu
       path = Path(path)

    with open(path, mode, encoding='utf8') as newFile:
        text = (newFile.read())
        print(v.external_message)
        print(text)
        newFile.close()

    return text

def choose_alphabet(m,v):
    print (v.choose_alphabet)

    read = input().lower()

    while (read != '1' and read != '2' and read != '3' and read != '4' and read != '5' and read != '' and read != 'b' and read != 'c' and read != 'q'):
        print(v.error_input)
        read = input().lower()

    if (read == '1'):
        print(v.english) # choose English
        return choose_extras(m,v,m.chars_eng)

    elif (read == '2' or read == ''):
        print(v.swedish) # choose Swedish
        return choose_extras(m,v,m.chars_sve)

    elif (read == '3'):
        print(v.spanish) # choose Spanish
        return choose_extras(m,v,m.chars_esp)

    elif (read == '4'):
        print(v.italian)  # choose Italian
        return choose_extras(m,v,m.chars_ita)

    elif (read == '5'):
        print(v.german)  # choose German
        return choose_extras(m,v,m.chars_ger)

    elif (read == 'b' or read == 'c'):
        print(v.cancel) # Cancel by user
        return main(m,v) # main menu
    elif (read == 'q'):
        return True # quit

def choose_extras(m,v,charset):
    print (v.choose_extras)
    read = input().lower()

    while (read != '1' and read != '2' and read != '3' and read != '4' and read != '' and read != 'b' and read != 'c' and read != 'q'):
        print(v.error_input)
        read = input().lower()

    if (read == '1' or read == ''):
        print(v.none) # choose none
        return charset

    elif (read == '2'):
        print(v.numerical) # choose numerical
        return charset + m.chars_numbers

    elif (read == '3'):
        print(v.special) # choose special
        return charset + m.chars_extra

    elif (read == '4'):
        print(v.both)  # choose numerical + special
        return charset + m.chars_numbers + m.chars_extra

    elif (read == 'b' or read == 'c'):
        print(v.cancel) # Cancel by user
        return main(m,v) # main menu
    elif (read == 'q'):
        return True # quit

def choose_alphabet_crack(m,v):
    print (v.choose_alphabet)

    read = input().lower()
    while (read != '1' and read != '2' and read != '3' and read != '4' and read != '5' and read != '' and read != 'b' and read != 'c' and read != 'q'):
        print(v.error_input)
        read = input().lower()

    if (read == '1'):
        print(v.english) # choose English
        set_frequency_language(m, v, m.frequency_eng)
        return m.chars_eng

    elif (read == '2' or read == ''):
        print(v.swedish) # choose Swedish
        set_frequency_language(m, v, m.frequency_sve)
        return m.chars_sve

    elif (read == '3'):
        print(v.spanish) # choose Spanish
        set_frequency_language(m, v, m.frequency_esp)
        return m.chars_esp

    elif (read == '4'):
        print(v.italian)  # choose Italian
        set_frequency_language(m, v, m.frequency_ita)
        return m.chars_ita

    elif (read == '5'):
        print(v.german)  # choose German
        set_frequency_language(m,v,m.frequency_ger)
        return m.chars_ger

    elif (read == 'b' or read == 'c'):
        print(v.cancel) # Cancel by user
        return main(m,v) # main menu
    elif (read == 'q'):
        return True # quit

def set_frequency_language (m,v,language_data):
    global frequency_data
    frequency_data = language_data

def int_input(m,v):
    """Get user input right in the console, return as single int"""
    print (v.input_int)

    number = input()

    while (not (number.lstrip("-").isdigit()) or not (-9999 <= int(number) <= 9999)):
        print(v.error_integer)
        number = input()

    return int(number)

def key_input(m,v):
    """Get user input right in the console, return as single string"""
    print (v.input_key)

    key = input()

    while ((key.lstrip("-").isdigit()) or not (MIN_LENGTH <= len(key) <= MAX_LENGTH) or not check_key(m,v,key)):
        print(v.error_key)
        key = input()

    return key

def check_key(m,v,key):
    """check that at least one of the characters in the key is alphabetic"""
    for char in key:
        if char.isalpha():
            if not char.isnumeric():
                return True
    return False

def length_input(m,v):
    length = input()
    while (not (length.lstrip("-").isdigit()) or not (MIN_LENGTH <= int(length) <= MAX_LENGTH)):
        print(v.error_length)
        length = input()

    return int(length)

def guess_input(m,v, max_length):
    length = input()
    while (not (length.lstrip("-").isdigit()) or not (MIN_LENGTH <= int(length) <= max_length)):
        print(v.error_length_max(max_length))
        length = input()

    return int(length)


# OUTPUT FUNCTIONS

def print_output (m, v, text, flag):
    if (flag):
        print(v.encrypt_message) # True for encryption
    else:
        print (v.decrypt_message) # False for decryption

    print(text)

    print (v.save_menu) # Ask if file should be saved

    read = input().lower()
    while (read != 'y' and read != 'n' and read != 'b' and read != 'q'):
        print(v.error_input)
        read = input().lower()

    if (read == 'y'):

        print (v.save_name) # Name file
        path = input()

        if (path == 'c'):
            print (v.cancel)
        else:
            save_file (m,v,path, text) # Save file

        return main(m, v)

    elif (read == 'n' or read == 'b'):
        return main(m,v) # main menu
    elif (read == 'q'):
        return True # quit

def save_file (m,v,path,text):
    """Save output in an external .txt file"""
    mode = "w"
    try:
        with open(path, mode, encoding='utf8') as file:
            file.write(text)
            file.close()
            print(v.save_success (path))

    except IOError as e:
        print(v.error_save(path)+ "\nI/O error({0}): {1}".format(e.errno, e.strerror))
    except:
        print(v.error_save2(path), sys.exc_info()[0])
        raise