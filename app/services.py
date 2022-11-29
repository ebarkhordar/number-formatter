import math

from app.constants import magnitudes


def formatter(n):
    n = float(n)
    n_thousands_order = int(math.floor(0 if n == 0 else math.log10(abs(n)) / 3))
    magnitude_idx = max(0, min(len(magnitudes) - 1, n_thousands_order))
    n_magnitude = n / 10 ** (3 * magnitude_idx)
    if "{:.1f}".format(n_magnitude) == "{:.0f}".format(n_magnitude) + ".0":
        return '{:.0f}{}'.format(n_magnitude, magnitudes[magnitude_idx])
    else:
        return '{:.1f}{}'.format(n_magnitude, magnitudes[magnitude_idx])
