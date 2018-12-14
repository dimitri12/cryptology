# Vigenère Cipher 
# view.py
# Created by Mauro J. Pappaterra on 22 of January 2018.

#START SCREEN
welcome = """
     
         _    ___                  __                     _       __             
        | |  / (_)___ ____  ____  _\_\ ________     _____(_)___  / /_  ___  _____
        | | / / / __ `/ _ \/ __ \/ _ \/ ___/ _ \   / ___/ / __ \/ __ \/ _ \/ ___/
        | |/ / / /_/ /  __/ / / /  __/ /  /  __/  / /__/ / /_/ / / / /  __/ /    
        |___/_/\__, /\___/_/ /_/\___/_/   \___/   \___/_/ .___/_/ /_/\___/_/     
              /____/                                   /_/                       
                                _____,    _..-=-=-=-=-====--,
                             _.'a   /  .-',___,..=--=--==-'`
                            ( _     \ /  //___/-=---=----'
                             ` `\    /  //---/--==----=-'
                          ,-.    | / \_//-_.'==-==---='
                         (.-.`\  | |'../-'=-=-=-=--'
                          (' `\`\| //_|-\.`;-~````~,        _
                               \ | \_,_,_\.'        \     .'_`\\
                                `\            ,    , \    || `\\\\
                                  \    /   _.--\    \ '._.'/  / |
                                  /  /`---'   \ \   |`'---'   \/
                                 / /'          \ ;-. \\
                              __/ /           __) \ ) `|
                            ((='--;)         (,___/(,_/              
    
                  = Encrypt/Decrypt text using different ciphers =  
 """

instructions = """Welcome to Vigenère Cipher. This short program will help you encrypt/decrypt any text 
right from the console or from an external source. You can also export your results!
You might enter 'q' at any time to exit the program.

Enter 's' and press <enter> to begin!"""

# MAIN MENU
menu = """\n::::Select one of the available options:
1 - ENCRYPT: Encrypt a text
2 - DECRYPT: Decrypt an obscured text
3 - CRACK: Crack the Vigenère cipher without a key!
4 - Choose a different cipher to encrypt/decrypt your text
5 - About: Read more about ciphers and cryptology

q - Quit"""

# ABOUT PAGE
about = """ blah blah blah

b - Back to menu"""

# ENCRYPT MENU
encrypt_menu = """\n:::: ENCRYPT TEXT
1 - Enter text in the console
2 - Use an external file
3 - Change Cipher

b - Back to menu"""

# DECRYPT MENU
decrypt_menu = """\n:::: DECRYPT TEXT
1 - Enter text in the console
2 - Use an external file
3 - Change Cipher

b - Back to menu"""

# CIPHER MENU
cipher_menu = """\n:::: Select one of the available ciphers:
1 - Transposition Cipher
2 - Substitution Cipher
3 - Shifter Cipher
4 - Vigenère Cipher (default)

b - Back to menu"""

transposition = "\nEncryption method changed to -> Transposition Cipher"
substitution = "\nEncryption method changed to -> Substituition Cipher"
shifter = "\nEncryption method changed to -> Shifter Cipher"
vigenere = "\nEncryption method changed to -> Vigenère Cipher"

# INPUT TEXT
input_text = "\n>>> You can now start writing the text you want to encrypt/decrypt right in the console!" \
            "\n>>> The only special characters supported are space ( ), comma (,) and period (.)!" \
          "\n>>> Once you have finished with your input, write <done> on a new line and press enter.\n"

# SHIFTER/VIGENERE CIPHER MENU
choose_alphabet = """\n--> Select one of the available alphabets:
1 - English
2 - Swedish (default)
3 - Spanish
4 - Italian
5 - German"""

english = "\nUsing English Alphabet (26 letters)"
swedish = "\nUsing Swedish Alphabet (29 letters)"
spanish = "\nUsing Spanish Alphabet (27 letters)"
italian = "\nUsing Italian Alphabet (23 letters)"
german = "\nUsing German Alphabet (30 letters)"

choose_extras = """\n--> Select one of the available options:
1- Exclude all characters outside the selected alphabet (default)
2- Include numerical characters [0-9]
3- Include all special characters [!,#,?,...]
4- Include both numerical and special characters"""

none = "All other characters will be clear out of the input"
numerical = "Numerical characters will be encrypted (+10 characters)"
special = "Special characters will be encrypted (+40 characters)"
both = "Numerical and special characters will be encrypted (+50 characters)"

input_int = "\n--> Enter the number of letters to shift (Positive numbers shift to the RIGHT -> and negative numbers shift to the <- LEFT):"

input_key = '''

                              8 8          ,o. 
                             d8o8azzzzzzzzd   b                                     
                                           `o' 
                                   
:::: Enter a key to use for encrypting/decrypting the text (max 16 digits):'''

# CRACK MENU
crack_menu = """\n:::: CRACK
1 - Enter text in the console
2 - Use an external file

b - Back to menu"""

triagram_message = "\nComparing triagrams..."

def print_triagrams (results):
    """Prints the results of the method findTriagram from model.py
    The parameter must be formatted asa list of tuples (triagram, distance)"""
    if (len(results) > 0):
        for result in results:
            print("Match found!! Triagram: '" + result[0] + "' <-> Distance: " + str(result[1]) + " spaces")
        print("\nDone! Let's estimate the length of the key...")
    else:
        print ("WARNING! No matching triagrams were found in the ciphertext!")

length_message = "\nEnter the maximum length for the key:"
guess_message = "\nEnter your educated guess for the length of the key..."

def print_lengths (counters):
    """Prints the estimation for key lengths in descending order from most likely to least likely"""
    printout = []
    samples = counters[0]

    if (samples > 0):
        for index, counter in enumerate(counters): # disregard counter for 1
            if (index > 0):
                printout.append ((index + 1, counter))

        for result in sorted(printout, key=lambda x: x[1], reverse=True): # print results descending order
            print("Est. key size: " + str(result[0]) + " -> " + str(result[1]) + " chances in " + str (samples))
    else:
        print("\nWARNING! No estimations for key size available!")

def print_frequency_table(string_frequency, data_frequency, shift = 0):
    """Takes a dictionary depicting the frequency of apparition of characters on a given alphabet
    formats and print out its content."""
    print ("\t\t\t\t--FREQUENCY TABLE-- \n\nGiven Block Letter Frequency \t Selected Alphabet Letter Frequency")
    shift = shift % len (string_frequency)
    index = 0
    while (index < len(data_frequency)):
        print("   " + string_frequency[shift][0] + " " + print_graph(string_frequency[shift][1]) + "      " + data_frequency[index][0] + " " + print_graph(data_frequency[index][1]))
        index += 1

        shift += 1

        if shift >= len (string_frequency): # wrap around
            shift -= len (string_frequency)

def print_graph (frequency):
    graph = ''
    X = '*'
    O = ' '

    if (frequency == 100.0):
        graph = str(frequency) + "%  " + X * 15
    elif (frequency >= 15.0):
        graph = " " + str(frequency) + "%  " + X * 15
    elif (frequency >= 12.0):
        graph = " " + str(frequency) + "%  " + X * 14 + O
    elif (frequency >= 10.0):
        graph = " " + str(frequency) + "%  " + X * 13 + O * 2
    elif (frequency >= 9.0):
        graph = "  " + str(frequency) + "%  " + X * 12 + O * 3
    elif (frequency >= 8.0):
        graph = "  " + str(frequency) + "%  " + X * 11 + O * 4
    elif (frequency >= 7.0):
        graph = "  " + str(frequency) + "%  " + X * 10 + O * 5
    elif (frequency >= 6.0):
        graph = "  " + str(frequency) + "%  " + X * 9 + O * 6
    elif (frequency >= 5.0):
        graph = "  " + str(frequency) + "%  " + X * 8 + O * 7
    elif (frequency >= 4.0):
        graph = "  " + str(frequency) + "%  " + X * 7 + O * 8
    elif (frequency >= 3.0):
        graph = "  " + str(frequency) + "%  " + X * 6 + O * 9
    elif (frequency >= 2.5):
        graph = "  " + str(frequency) + "%  " + X * 5 + O * 10
    elif (frequency >= 2.0):
        graph = "  " + str(frequency) + "%  " + X * 4 + O * 11
    elif (frequency >= 1.5):
        graph = "  " + str(frequency) + "%  " + X * 3 + O * 12
    elif (frequency >= 1.0):
        graph = "  " + str(frequency) + "%  " + X * 2 + O * 13
    elif (frequency >= 0.3):
        graph = "  " + str(frequency) + "%  " + X + O * 14
    elif (frequency >= 0.0):
        graph = "  " + str(frequency) + "%  " + O * 15
    else:
        graph = "  Unknown" + O * 14
    return graph # + '|'

def print_key_index (key, key_index):
    printout = '\nYour Key: '

    for index, char in enumerate (key):
        letter = ''
        if (char == '-1'): # -1 flag for empty char in the key
            letter = '-'
        else:
            letter = char

        if index == key_index:
            printout += '[' + letter + ']'
        else:
            printout += ' ' + letter + ' '

    print (printout)

calibrate_message = """\n:::: Select an option from below
1 - Shift to the left <<<
2 - Shift to the right >>>

3 - Previous letter
4 - Next letter

5 - Change key length

b - Back to menu"""

calibrate_message_done = """\n:::: Select an option from below
1 - Shift to the left <<<
2 - Shift to the right >>>

3 - Previous letter
4 - Next letter

5 - Change key length
6 - USE THIS KEY TO CRACK ENCRYPTION

b - Back to menu"""

def use_key (key):
    return "Using key '" + key + "' to decrypt the cipher-text"

# EXTERNAL FILE
external_file = "\n>>>> Enter the path to an external text file below:"
external_message = "\n::External file contents\n"

# DISPLAY OUTPUT
encrypt_message = "\n::Your encrypted text\n"
decrypt_message = "\n::Your decrypted text\n"

# SAVE TO FILE
save_menu = """\nSave your encrypted/decrypted text as an external text file?
y - yes
n - no"""

save_name = "\nEnter a name to save your file (type 'c' to cancel):"

def save_success (name):
    return "\nYour text has been saved as '" + name + "'"

# ERROR MESSAGES
error_start = "\nInvalid Input: Enter 's' to start or 'q' to quit then press <enter>"
error_input = "\nInvalid Input: Select a valid option from the menu"
error_integer = "\nInvalid Input: Enter an integer number between -9999 and 9999"
error_key = "\nInvalid Input: The key must use 1 to 16 alphabetical characters"
error_path = "\nInvalid Input: Not a valid name or path. Try again, or enter 'c' and press <enter> to cancel\n"
error_length = "\nInvalid Input: Enter an integer number between 2 and 16"
error_empty = "\nInvalid Input: There is no text to encrypt/decrypt! Try one more time..."
error_incomplete = "\nYou must fill in all characters in the key before using it\n"

def error_length_max (max):
    return "\nInvalid Input: Enter an integer number between 2 and " + str(max)

def error_save (path):
    return "\nError could not write into file " + path

def error_save2 (path):
    return "\nError could not write into file " + path +"\nUnexpected error:"

cancel = "\nCANCEL BY USER"
exit = """\n              <>==(|==============> Exit by User <==============|)==<>\n"""