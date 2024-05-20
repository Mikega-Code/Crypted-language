import random
import string

def text_to_morse(text):
    morse_dict = {
        'A': '01', 'B': '1000', 'C': '1010', 'D': '100', 'E': '0',
        'F': '0010', 'G': '110', 'H': '0000', 'I': '00', 'J': '0111',
        'K': '101', 'L': '0100', 'M': '11', 'N': '10', 'O': '111',
        'P': '0110', 'Q': '1101', 'R': '010', 'S': '000', 'T': '1',
        'U': '001', 'V': '0001', 'W': '011', 'X': '1001', 'Y': '1011',
        'Z': '1100',
    }

    morse_code = ''
    for char in text:
        morse_char = morse_dict.get(char.upper(), '')
        if char == ' ':
            morse_code += ' '
        elif morse_char:
            morse_code += morse_char + ' '

    return morse_code.strip()

# MORSE TO TEXT
def morse_to_text(morse_code):
    morse_dict = {'01': 'A', '1000': 'B', '1010': 'C', '100': 'D', '0': 'E', '0010': 'F',
                  '110': 'G', '0000': 'H', '00': 'I', '0111': 'J', '101': 'K', '0100': 'L',
                  '11': 'M', '10': 'N', '111': 'O', '0110': 'P', '1101': 'Q', '010': 'R',
                  '000': 'S', '1': 'T', '001': 'U', '0001': 'V', '011': 'W', '1001': 'X',
                  '1011': 'Y', '1100': 'Z', ' ': ' '}

    morse_words = morse_code.split(' ')
    text = ''
    for word in morse_words:
        if word in morse_dict:
            text += morse_dict[word]
        else:
            text += ' '
    return text

# ENCRYPTOR
def encryptor(text):
    transformed_text = ''
    for char in text:
        if char == '1':
            transformed_text += random.choice(string.ascii_uppercase[14:])
        elif char == '0':
            transformed_text += random.choice(string.ascii_uppercase[:12])
        elif char == ' ':
            transformed_text += 'M'
    return transformed_text

# DECRYPTOR
def texte_to_code(texte):
    code = ''
    for lettre in texte.upper():
        if 'A' <= lettre <= 'L':
            code += '0'
        elif 'N' <= lettre <= 'Z':
            code += '1'
        elif lettre == 'M':
            code += ' '
        elif lettre == "MM":
            code += "  "
    return code

what_to_do = int(input("1 : Cryptage , 2 : Decryptage   :   "))


if what_to_do == 1:
    crypt = str(input("Entrez le texte à traduire en code J-A : "))
    code_morse = text_to_morse(crypt)
    code_j_a = encryptor(code_morse)
    print("Le texte crypté est : ", code_j_a)

elif what_to_do == 2:
    decrypt = str(input("Entrez le texte : "))
    code = texte_to_code(decrypt)
    result = morse_to_text(code)
    print("Le texte est : ", result)

