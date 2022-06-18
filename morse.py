import itertools


MORSE_CODE = {
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
    "...---...": "SOS"
}


def decode_bits_initial(bits):
    bits = bits.strip('0')
    speed = min(len(list(g)) for i, g in itertools.groupby(bits))
    divided = ''.join(bits[i] for i in range(0, len(bits), speed))
    return divided.replace('111', '-').replace('1', '.').replace('0000000', '   ').replace('000', ' ').replace('0', '')


def decode_bits(bits):
    bits = bits.strip('0')
    speed = min(len(list(g)) for i, g in itertools.groupby(bits))
    return bits[::speed].replace('111', '-').replace('1', '.').replace('0000000', '   ').replace('000', ' ').replace('0', '')


def decode_morse(morse_code):
    return ' '.join(''.join(MORSE_CODE[c] for c in w.split()) for w in morse_code.strip().split('   '))


bits = decode_bits('111000111')
print(bits)
print(decode_morse(bits))
