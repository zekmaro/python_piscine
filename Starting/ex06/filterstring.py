import sys

def main():
    """
    Program that accepts two arguments: a string (S), and an integer (N).
    Return a list of words from S that have a length greater than N.
    """
    if len(sys.argv) != 3:
        raise AssertionError("Incorrect number of arguments.")

    text = sys.argv[1]
    try:
        N = int(sys.argv[2])
    except ValueError:
        raise AssertionError("Second argument is not an integer.")

    if N < 0:
        raise AssertionError("Argument is negative.")

    words = text.split()
    filtered_words = [word for word in words if (lambda w: len(w) > N)(word)]
    print(filtered_words)


if __name__ == "__main__":
    main()
