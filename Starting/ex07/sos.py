import sys


def main():
    """
    Program that takes a string and converts it to Morse code.
    """

    MORSE_CODE_DICT = {
        'A': '.-', 'B': '-...',
        'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-',
        'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--',
        'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.',
        '0': '-----', ', ': '--..--', '.': '.-.-.-',
        '?': '..--..', '/': '-..-.', '-': '-....-',
        '(': '-.--.', ')': '-.--.-', ' ': '/',
    }

    if len(sys.argv) != 2:
        raise AssertionError("Incorrect number of arguments.")

    text = sys.argv[1].upper()

    try:
        morse_code = ' '.join(MORSE_CODE_DICT[c] for c in text)
    except KeyError:
        raise AssertionError("the arguments are bad")

    print(morse_code)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
