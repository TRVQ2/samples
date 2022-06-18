BITS_SEPARATOR = "0"
MORSE_SEPARATOR = " "

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
    MORSE_SEPARATOR: MORSE_SEPARATOR  # E.G. STR_SEPARATOR
}

BIT_TO_MORSE = {"111": "-", "1": ".", BITS_SEPARATOR: MORSE_SEPARATOR}

CHAR_TO_MORSE = {}
for i in MORSE_TO_CHAR:
    CHAR_TO_MORSE[MORSE_TO_CHAR[i]] = i

MORSE_TO_BIT = {}
for i in BIT_TO_MORSE:
    MORSE_TO_BIT[BIT_TO_MORSE[i]] = i


def split(str, split_char=" "):
    out = []
    temp = ''
    for i in str:
        if i == split_char and temp != '':
            out.append(temp)
            temp = ''
        else:
            temp += i
    out.append(temp)
    return out


def bits_to_morse(bits):
    bits = bits.strip(BITS_SEPARATOR)
    import itertools
    speed = min(len(list(g)) for i, g in itertools.groupby(bits))
    # import re
    # speed = min(len(m) for m in re.findall(r'1+|0+', bits))
    return
    ''.join(BIT_TO_MORSE[b] for b in split(bits[::speed], BITS_SEPARATOR))


def morse_to_str(morse):
    return
    ''.join(MORSE_TO_CHAR[c] for c in split(morse.strip(), MORSE_SEPARATOR))


def str_to_morse(str):
    return MORSE_SEPARATOR.join(CHAR_TO_MORSE[c] for c in str.strip())


def morse_to_bits(morse):
    return BITS_SEPARATOR.join(MORSE_TO_BIT[c] for c in morse.strip())


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
