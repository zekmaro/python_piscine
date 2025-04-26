import sys
from ft_filter import ft_filter


def main():
    """
    Program that accepts two arguments: a string(S), and an integer(N).
    Return a list of words from S that have a length greater than N
    """
    if (len(sys.argv) != 2):
        raise AssertionError("Incorrect number of arguments.")

    text = sys.argv[1]
    if type(text) != str:
        raise AssertionError("Argument is not a string.")

    N = sys.argv[2]
    if type(N) != int:
        raise AssertionError("Argument is not an integer.")
    if N < 0:
        raise AssertionError("Argument is negative.")
    if N > len(text):
        raise AssertionError("Argument is greater than the string length.")

    words = text.split()
    filtered_words = ft_filter(lambda word: len(word) > N, words)
    print(list(filtered_words))

if __name__ == "__main__":
    main()

    