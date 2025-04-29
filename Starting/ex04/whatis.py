import sys


def main():
    if len(sys.argv) > 2:
        raise AssertionError("More than one argument is provided.")
    elif len(sys.argv) < 2:
        raise AssertionError("No argument is provided.")
    
    try:
        number = int(sys.argv[1])
    except ValueError:
        raise AssertionError("Argument is not an integer.")
    
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
