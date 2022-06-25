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


def decodeBits(bits):
    bits = bits.strip('0')
    # import re
    # speed = min(len(m) for m in re.findall(r'1+|0+', bits))
    import itertools
    bits = bits[::min(len(list(g)) for i, g in itertools.groupby(bits))] \
        .replace('111', '-') \
        .replace('1', '.') \
        .replace('0000000', '   ') \
        .replace('000', ' ') \
        .replace('0', '')
    return ''.join(bits)


def decodeMorse(morse):
    morse = morse.strip().split('   ')
    return ' '.join(''.join(MORSE_CODE[c] for c in w.split()) for w in morse)


bits = '101110111011100011101110111000101010100011101000000010111011100010001'
print(bits)
morse = decodeBits(bits)
print(morse)
print(decodeMorse(morse))
