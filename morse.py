BITS_SEP = '0'
BITS_SPACE = '0'
BITS_CHAR_SEP = '000'  # BITS_SEP + BITS_SPACE + BITS_SEP
BITS_WORD_SEP = '0000000'  # (BITS_SEP + BITS_SPACE) * 3 + BITS_SEP
MORSE_SEP = " "
MORSE_SPACE = " "
MORSE_WORD_SEP = "   "  # MORSE_SEP + "MORSE_SPACE" + MORSE_SEP
WORDS_SEP = " "
TEMP_SPACE = '2'  # temporarily instead of BITS_SPACE and MORSE_SPACE
BITS_TEMP_CHAR_SEP = '020'  # BITS_SEP + TEMP_SPACE + BITS_SEP
BITS_TEMP_WORD_SEP = '0202020'  # (BITS_SEP + TEMP_SPACE) * 3 + BITS_SEP
MORSE_TEMP_WORD_SEP = " 2 "  # MORSE_SEP + TEMP_SPACE + MORSE_SEP

MORSE_TO_CHAR = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    ".-.-.-": ".",
    "--..--": ",",
    "..--..": "?",
    ".----.": "'",
    "-.-.--": "!",
    "-..-.": "/",
    "-.--.": "(",
    "-.--.-": ")",
    ".-...": "&",
    "---...": ":",
    "-.-.-.": ";",
    "-...-": "=",
    ".-.-.": "+",
    "-....-": "-",
    "..--.-": "_",
    ".-..-.": '"',
    "...-..-": "$",
    ".--.-.": "@",
    "...---...": "SOS",
    MORSE_SPACE: WORDS_SEP
}

BIT_TO_MORSE = {"111": "-", "1": ".", BITS_SPACE: MORSE_SPACE}

CHAR_TO_MORSE = {}
for i in MORSE_TO_CHAR:
    CHAR_TO_MORSE[MORSE_TO_CHAR[i]] = i
MORSE_TO_CHAR[TEMP_SPACE] = WORDS_SEP  # "2": " "

MORSE_TO_BIT = {}
for i in BIT_TO_MORSE:
    MORSE_TO_BIT[BIT_TO_MORSE[i]] = i
BIT_TO_MORSE[TEMP_SPACE] = MORSE_SPACE  # "2": " "


def bits_to_morse(bits):
    bits = bits.strip(BITS_SEP)
    import itertools
    speed = min(len(list(g)) for i, g in itertools.groupby(bits))
    # import re
    # speed = min(len(m) for m in re.findall(r'1+|0+', bits))
    chars = bits[::speed].replace(BITS_WORD_SEP, BITS_TEMP_WORD_SEP) \
                         .replace(BITS_CHAR_SEP, BITS_TEMP_CHAR_SEP) \
                         .split(BITS_SEP)
    return ''.join(BIT_TO_MORSE[b] for b in chars)


def morse_to_str(morse):
    words = morse.strip() \
                 .replace(MORSE_WORD_SEP, MORSE_TEMP_WORD_SEP) \
                 .split(MORSE_SEP)
    return ''.join(MORSE_TO_CHAR[c] for c in words)


def str_to_morse(str):
    return MORSE_SEP.join(CHAR_TO_MORSE[c] for c in str.strip(WORDS_SEP))


def morse_to_bits(morse):
    return BITS_SEP.join(MORSE_TO_BIT[c] for c in morse.strip(MORSE_SEP))


# morse = bits_to_morse('111000111')
# print(morse)
str = "JOHN WEIN"
print(str)
encoded_str = str_to_morse("JOHN WEIN")
print(encoded_str)
encoded_morse = morse_to_bits(encoded_str)
print(encoded_morse)
decoded_morse = bits_to_morse(encoded_morse)
print(decoded_morse)
decoded_str = morse_to_str(decoded_morse)
print(decoded_str)
