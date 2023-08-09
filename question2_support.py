import pandas as pd


def convert_to_base(number, base):
    digits = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ''

    while number > 0:
        remainder = number % base
        result = digits[remainder] + result
        number //= base

    return result


# Tests all possible bases to this function
# As f(15840) = cGp and f(42541) = Zcz this should test which bases has the first digit of the 15840 conversion and second digit of 42541 conversion equal.
for base in range(2, 63):
    result_1 = convert_to_base(15840, base)
    result_2 = convert_to_base(42541, base)

    # Checks the required match and if it has the same size as the outputs
    if result_1[0] == result_2[1] and len(result_1) == 3 and len(result_2) == 3:
        print(
            f"One base that matches this results is: {base}           results: ({result_1} and {result_2})")
