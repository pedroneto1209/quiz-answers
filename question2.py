import pandas as pd


def toBase62(number):
    result = ''

    while number > 0:
        remainder = number % 62
        result = digits[
            remainder] + result
        number //= 62

    return result


def main():
    # Base 62 digits
    global digits
    digits = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Read CSV into a dataframe
    df = pd.read_csv('spreadsheet.csv', names=['x', 'y'])

    # Dictionary to map all old digits into the new defined digits
    remap_dict = {}

    # Run into all CSV rows to map which digits in the logs should relate to the original digits of base 62
    for _, row in df.iterrows():

        number_b62 = toBase62(row[0])

        for old_digit in number_b62:

            # Mapping old base 62 digits into new ones defined in the CSV
            remap_dict[old_digit] = row[1][number_b62.index(old_digit)]

    # The numbers in the CSV doesn't contain the digit "l" when converted to base 62
    # By comparing both digit sets it's possible to notice the one digit missing is '5'
    remap_dict['l'] = '5'

    # Sorting found digits to print the new digits to compare to the old one
    sorted_keys = [remap_dict[digit] for digit in digits]
    print("\nThe old base 62 digits are remapped to this new set: \n {}\n".format(
        ''.join(sorted_keys)))

    # Assigning the new digits to the variable so we can run the convert function again to check the results
    digits = [remap_dict[digit] for digit in digits]

    # Calculating new formula accuracy
    correct_conversions = 0
    for _, row in df.iterrows():
        if toBase62(row[0]) == row[1]:
            correct_conversions += 1
    print('New function accuracy of {} %'.format(100*correct_conversions/75))

    # Quiz answers
    print("f(30001) = " + toBase62(30001))
    print("f(55555) = " + toBase62(55555))
    print("f(77788) = " + toBase62(77788))


if __name__ == "__main__":
    main()
