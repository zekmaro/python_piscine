import numpy as np
from typing import Union

Number = Union[int, float]

def check_numeric_type(lst: list[int | float], lst_name: str) -> bool:
    """"
    Check if the list is of type int or float. Raise TypeError if not.
    """
    if not isinstance(lst, list):
        raise TypeError(f"{lst_name} must be a list.")
    if not all(isinstance(i, (int, float)) for i in lst):
        raise TypeError(f"All elements in {lst_name} must be int or float.")


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """"
    Calculate the BMI of a person given their height and weight.
    """
    check_numeric_type(height, "Height")
    check_numeric_type(weight, "Weight")

    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be of the same length.")

    return (np.array(weight) / (np.array(height) ** 2)).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """"
    Apply a limit to the BMI list.
    """
    check_numeric_type(bmi, "BMI")

    if not isinstance(limit, (int, float)):
        raise TypeError("Limit must be an integer or float.")
    if limit <= 0:
        raise ValueError("Limit must be a positive number.")

    return [b > limit for b in bmi]
