from give_bmi import give_bmi, apply_limit


def main():
    """"
    Program that calculates the BMI of a person given their height and weight.
    """
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"AssertionError: {e}")
        sys.exit(1)