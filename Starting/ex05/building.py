import sys


def main():
    """
    Takes a single string argument and displays
    the sums of its upper-case letters, lower-case letters,
    punctuation characters, digits, and spaces.
    """
    if len(sys.argv) != 2:
        raise AssertionError("Incorrect number of arguments.")

    text = sys.argv[1]

    counts = {
        "upper": 0,
        "lower": 0,
        "punctuation": 0,
        "space": 0,
        "digit": 0,
    }

    for c in text:
        if c.isupper():
            counts["upper"] += 1
        elif c.islower():
            counts["lower"] += 1
        elif c.isdigit():
            counts["digit"] += 1
        elif c.isspace():
            counts["space"] += 1
        else:
            counts["punctuation"] += 1

    print(f"The text contains {len(text)} characters:")
    print(f"{counts['upper']} upper letters")
    print(f"{counts['lower']} lower letters")
    print(f"{counts['punctuation']} punctuation marks")
    print(f"{counts['space']} spaces")
    print(f"{counts['digit']} digits")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
