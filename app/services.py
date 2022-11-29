import math

from app.constants import magnitudes


def formatter(input_number):
    """
       Returns a truncated, prettified string version of a float number that supports millions, billions and trillions

               Parameters:
                       input_number (float): A float number

               Returns:
                       output (str): Prettified string version
    """
    input_number = float(input_number)
    n_thousands_order = int(math.floor(0 if input_number == 0 else math.log10(abs(input_number)) / 3))
    magnitude_idx = max(0, min(len(magnitudes) - 1, n_thousands_order))
    n_magnitude = input_number / 10 ** (3 * magnitude_idx)
    if "{:.1f}".format(n_magnitude) == "{:.0f}".format(n_magnitude) + ".0":
        return '{:.0f}{}'.format(n_magnitude, magnitudes[magnitude_idx])
    else:
        return '{:.1f}{}'.format(n_magnitude, magnitudes[magnitude_idx])
