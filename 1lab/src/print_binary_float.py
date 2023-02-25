from .reverse import *


def print_binary_float(binary_x: list) -> float:
    return (-1)**binary_x[0] * straight_to_int(binary_x[2]) * 10**(-straight_to_int(binary_x[1]))
