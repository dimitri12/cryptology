# Vigenère Cipher 
# model.py
# Created by Mauro J. Pappaterra on 22 of January 2018.

###########################################GLOBAL VARIABLES

# alphabets for the shifting cipher
all = [' ', ',', '.']
chars_eng = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] + all
chars_sve = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','å','ä','ö'] + all
chars_esp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','á','é','í','ó','ú','ü'] + all
chars_ita = ['a','b','c','d','e','f','g','h','i','l','m','n','o','p','q','r','s','t','u','v','z','à','è','ì','ò','ù'] + all
chars_ger = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','ä','ö','ü','ẞ'] + all

# extra characters for the shifting cipher
chars_numbers = ['0','1','2','3','4','5','6','7','8','9']
chars_extra = ["'",'-','¡','!','¿','?','"','[',']','(',')','{','}','#','@','%','*','=','+','>','<','/',"\\",'|','$','£','€','¥','¢','¥','₽','₩','₪','฿','₫','₴','₹']

# default alphabet for the shifting cipher
chars_default = chars_sve  # + chars_numbers + chars_extra

substitute = { # default dictionary for the substitution cipher using 34 characters
    'a':'6',
    'b':'@',
    'c':'&',
    'd':'$',
    'e':'!',
    'f':'=',
    'g':'#',
    'h':'+',
    'i':'0',
    'j':'5',
    'k':'*',
    'l':'>',
    'm':'<',
    'n':'|',
    'ñ':'3',
    'o':"'",
    'p':'^',
    'q':'~',
    'r':'¨',
    's':'(',
    't':')',
    'u':'{',
    'v':'}',
    'w':'/',
    'x':'%',
    'y':'2',
    'z':'4',
    'å':'1',
    'ä':'7',
    'ö':'9',
    'ü':'Ä',
    'ẞ':'Ö',
    ' ':'£',
    ',':'-',
    '.':'8',
}

# Frequency of letters in % for all languages available (for cracking algorithm)
frequency_eng = [('a',8.5),('b',1.6),('c',3.2),('d',3.9),('e',12.1),('f',2.2),('g',2.1),('h',5.0),('i',7.3),
    ('j',0.2),('k',0.8),('l',4.2),('m',2.5),('n',7.2),('o',7.5),('p',2.1),('q',0.1),('r',6.3),('s',6.7),('t',8.9),
    ('u',2.7),('v',1.1),('w',1.8),('x',0.2),('y',1.7),('z',0.1),(' ',10.0),(',',2.0),('.',2.0)]

frequency_sve = [('a',9.4),('b',1.5),('c',1.5),('d',4.7),('e',10.1),('f',2.0),('g',2.9),('h',2.1),('i',5.8),
    ('j',0.6),('k',3.1),('l',5.3),('m',3.5),('n',8.5),('o',4.5),('p',1.8),('q',0.2),('r',8.4),('s',6.6),('t',7.7),
    ('u',1.9),('v',2.4),('w',0.1),('x',0.2),('y',0.7),('z',0.1),('å',1.3),('ä',1.8),('ö',1.3),(' ',10.0),(',',2.0),('.',2.0)]

frequency_esp = [('a',12.5),('b',1.3),('c',4.4),('d',5.1),('e',13.2),('f',0.8),('g',1.2),('h',0.9),('i',6.9),
    ('j',0.4),('k',0.1),('l',5.8),('m',2.6),('n',7.1),('o',9.0),('p',2.7),('q',0.8),('r',6.6),('s',7.4),('t',4.4),
    ('u',4.0),('v',1.0),('w',0.1),('x',0.2),('y',0.8),('z',0.4),('á',0.1),('é',0.4),('í',0.7),('ó',0.8),('ú',0.2),('ü',0.1),(' ',10.0),(',',2.0),('.',2.0)]

frequency_ita = [('a',11.7),('b',0.9),('c',4.5),('d',3.7),('e',11.8),('f',1.1),('g',1.6),('h',0.6),('i',10.1),
    ('l',6.5),('m',2.5),('n',6.9),('o',9.8),('p',3.0),('q',0.5),('r',6.4),('s',5.0),('t',5.6),('u',3.0),('v',2.1),
    ('w',0.1),('x',0.1),('y',0.1),('z',1.2),('à',0.6),('è',0.3),('ì',0.1),('ò',0.1),('ù',0.1),(' ',10.0),(',',2.0),('.',2.0)]

frequency_ger = [('a',6.3),('b',2.2),('c',2.7),('d',4.9),('e',16.0),('f',1.8),('g',3.0),('h',4.1),('i',7.6),
    ('j',0.3),('k',1.5),('l',3.7),('m',2.7),('n',9.6),('o',2.7),('p',1.1),('q',0.1),('r',7.7),('s',6.4),('t',6.4),
    ('u',3.8),('v',1.0),('w',1.4),('x',0.1),('y',0.1),('z',1.2),('ä',0.5),('ö',0.2),('ü',0.6),('ẞ',0.1),(' ',10.0),(',',2.0),('.',2.0)]

frequency_default = frequency_sve

########################################### ENCRYPTION/DECRYPTION ALGORITHMS

#def encrypt(p,k):
#    encrypted = ""
#    return encrypted

#def decrypt(c,k):
#    decrypted = ""
#    return decrypted

# TRANSPOSITION CIPHER
def transposition (text):
    """Encrypts the given text with a simple transposition cipher that swaps the order
    of the letter. Same algorithm is used for the decryption of an obscured text"""
    return ''.join([ text[x:x+2][::-1] for x in range(0, len(text), 2) ]);

# SUBSTITUTION CIPHER
def substitution_encrypt (text, dictionary = substitute):
    """Encrypts the given text with a simple substitution cipher using a Python dictionary """
    encrypted = ""
    for char in text.lower():
        if char in dictionary:
            encrypted += dictionary[char]
        else:
            encrypted += char # if value not found in dictionary add without encryption

    return encrypted

def substitution_decrypt (text, dictionary = substitute):
    """Decrypts an obscured text using the substitution cipher,
    (must use the same dictionary used for encryption, naturally)"""
    decrypted = ""
    for char in text.lower():
        for key,value in dictionary.items():
            if value == char:
                decrypted += key
    return decrypted

# SHIFTER CIPHER
def shift_encrypt (text, k, chars_set = chars_default):
    """Encrypts a given text using a shift cipher, a given alphabet (list) and a value k (int)
    for  the spaces shifted. Default alphabet is the Swedish with 29 characters"""
    encrypted = ""
    k %= len(chars_set) # it should wrap around after maximum number of chars in the alphabet
    # print(str(k))

    for char in clean_text(text, chars_set):
        j = 0
        while chars_set[j] != char:
            j += 1

        if (j + k < len(chars_set)):  # work around to a avoid index error, after z comes a,b,c...
            encrypted += chars_set[j + k]
        else:
            w = j + k - len(chars_set)
            encrypted += chars_set[w]
            # print(encrypted)

    return encrypted

def shift_decrypt (text, k, chars_set = chars_default):
    """Decrypts an obscured text using the shift cipher,
    (must use the same alphabet and integer k used for encryption, naturally)"""
    decrypted = ""
    k %= len(chars_set) # it should wrap around after maximum number of chars in the alphabet

    for char in clean_text(text, chars_set):
        j = 0
        while chars_set[j] != char:
            j += 1

        if (j - k < len(chars_set)):  # work around to a avoid index error, after z comes a,b,c...
            decrypted += chars_set[j - k]
        else:
            w = j - k - len(chars_set)
            decrypted += chars_set[w]
    return decrypted

# VIGENÈRE CIPHER
def vigenere_encrypt (text, key, chars_set = chars_default):
    encrypted = ""
    key_list = []
    text = clean_text(text, chars_set)

    for character in key.lower():  # iterates every character on a string with a for loop
        for index, letter in enumerate (chars_set):
            if (character == letter):
                key_list.append(index)

    key_size = len (key_list)
    key_index = 0

    for character in clean_text(text, chars_set):
        encrypted += shift_encrypt(character, key_list[key_index], chars_set)
        key_index+= 1

        # FOR TESTING PURPOSES
        # print("character: " + character + "\t key index: "+ str(key_index) + "\t key: " + str(key_list[key_index]))
        # print("message: " + encrypted)

        if (key_index == key_size): # reset counter
            key_index = 0

    return encrypted

def vigenere_decrypt(text, key, chars_set = chars_default):
    decrypted = ""
    key_list = []

    for character in key.lower():  # iterates every character on a string with a for loop
        for index, letter in enumerate(chars_set):
            if (character == letter):
                key_list.append(index)

    key_size = len(key_list)

    key_index = 0

    for character in clean_text(text, chars_set):
        decrypted += shift_decrypt(character, key_list[key_index], chars_set)
        key_index += 1

        if (key_index == key_size): # reset counter
            key_index = 0

    return decrypted

def clean_text (input, chars_set = chars_default):
    """Takes a string and a set of characters, then checks each character and
    gets rid of all characters not included on the set"""
    clean_input = ""

    for char in input.lower():
        if (char in chars_set or char == ' '):
            clean_input += char

    return clean_input


########################################### BREAK VIGENÈRE CIPHER
def find_triagrams (cipherText):
    """Takes a cipher-text as a string, divides in triagrams (3 character sub-strings), searches for
    matches by comparing with the rest of the string (by substrings of 3), returns a list of tuples
    containing the each pair of repeated triagrams found and the calculated distance in between them"""
    triagram_list = []
    results = []

    # FOR TESTING PURPOSES
    #print ('\n' + cipherText + '\n')

    for index,char in enumerate(cipherText): # this loops creates a list of all triagrams on the cipher-text
        new_triagram = cipherText[index:index + 3]

        if (len(new_triagram) == 3):
            triagram_list.append(new_triagram)

    # FOR TESTING PURPOSES
    #print (triagram_list)

    update_index = 0

    for triagram in triagram_list:

        search_index = 3 + update_index
        start_index = search_index

        while search_index < len(cipherText):
            if (len(cipherText[search_index: search_index + 3]) == 3):
                # FOR TESTING PURPOSES
                #print ("comparing " + triagram + " with " + cipherText[search_index: search_index + 3])
                if (triagram == cipherText[search_index: search_index + 3]): # when a match is found
                    distance = search_index - start_index
                    results.append((triagram,distance)) # store values on results array
                    # FOR TESTING PURPOSES
                    #print("Match found on triagram '" + triagram + "', within a distance of " + str(distance) + " spaces")
            search_index += 1
        update_index += 1

    return results

def estimate_key_length(results, max_length):
    """Takes the results from findTriagram() method, and a maximum length for the key,
    and estimates the key length, returns a list of counters where each index
    correspond for their following number (+1) in key length estimation. Index = 0 equals the number of
    samples received"""
    counters = []
    samples = len(results)

    while (max_length > 0):
        counters.append(0)
        max_length -= 1

    for index, counter in enumerate (counters):
        #print (str(index + 1))
        modulus = index + 1

        if (index >= 1):
            for result in results:
                if (result[1] % modulus == 0):
                    counters[index] += 1
        else:
            counters[index] = samples # the first element of the list contains the number of samples
                                      # since there's no use on calculate keys of length 1
    return counters

def getBlock (cipher_text, key_length):
    """Given a cipher text and a key length estimation, this function breaks the cipher text
        in a series of blocks of strings of size of the given length, and returns a single list
        containing the entire cipher_text broke in blocks"""
    total = len(cipher_text)
    block = []

    block_size = total / key_length

    #print(cipher_text)
    #print(str(total))

    index = 0
    while (block_size > 0): # divide the text in blocks
        block.append(cipher_text[index:index+key_length])
        index += key_length
        block_size -=1

    return block


def getString(cipher_as_blocks, index):
    """Given a cipher text divided in blocks and an index, this function returns
    a single string with all the characters in the index provided for each one of the blocks"""
    new_string = ''

    for block in cipher_as_blocks:
        if (index < len(block)):
            # print(block[index])
            new_string += block[index]

    return new_string

def getFrequency (string, alphabet = chars_default):
    """Takes a single block (string) from the cipher-text and an alphabet (as list)
    and calculates the frequency for each of its characters in percentage of appereance.
    It returns a list of tuples containing each character of the alphabet and its frequency as
    a float number."""
    total = len(string)
    results = [] # a list of tuples

    #print (string)

    for char in alphabet:
        counter = 0
        for compare in string:
            if (char == compare):
                counter += 1
        frequency = round(counter * 100 / total,1)
        results.append((char,frequency))
        #print (char + " appears " + str(counter) + " times, making " + str(frequency) + "%")
    #print (results)
    return results