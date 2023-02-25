from .reverse import *


def addition(binary_x1: list, binary_x2: list) -> list:
    binary_res = []
    carry = False

    for j in range(abs(len(binary_x1) - len(binary_x2))):
        binary_x2.insert(1, 0)

    for i in range(len(binary_x2), 0, -1):
        if binary_x1[i - 1] + binary_x2[i - 1] == 2 and carry:
            binary_res.insert(0, 1)
            carry = True
        elif binary_x1[i - 1] + binary_x2[i - 1] == 2:
            binary_res.insert(0, 0)
            carry = True
        elif binary_x1[i - 1] + binary_x2[i - 1] == 1 and carry:
            binary_res.insert(0, 0)
            carry = True
        elif binary_x1[i - 1] + binary_x2[i - 1] == 0 and carry:
            binary_res.insert(0, 1)
            carry = False
        else:
            binary_res.insert(0, binary_x1[i - 1] + binary_x2[i - 1])
            carry = False

    return binary_res


def multiplication(binary_x1: list, binary_x2: list) -> list:
    sing = binary_x1[0] == binary_x2[0]
    binary_res = [0] * 16
    for i in range(len(binary_x2) - 1, 0, -1):
        if binary_x2[i] == 1:
            binary_res = addition(binary_res, binary_x1.copy())
        binary_x1.append(0)
    if sing:
        binary_res[0] = 0
    else:
        binary_res[0] = 1
    return binary_res


def division(binary_dividend: list, binary_divider: list) -> list:
    sing = binary_dividend[0] == binary_divider[0]
    binary_res = [0, 0, 0, 0, 0, 0, 0, 0]
    one = [0, 0, 0, 0, 0, 0, 0, 1]
    binary_dividend[0], binary_divider[0] = 0, 1
    binary_divider = to_binary_addition(straight_to_int(binary_divider))
    value = addition(binary_dividend,  binary_divider)
    if value[0] == 0:
        while binary_dividend[0] != 1:
            binary_dividend = addition(binary_dividend,  binary_divider)
            if binary_dividend[0] != 1:
                binary_res = addition(binary_res, one)
    if sing:
        return binary_res
    else:
        binary_res[0] = 1
        return binary_res


def float_addition(binary_x1: list, binary_x2: list) -> list:
    binary_res = [0]
    one = [0, 0, 0, 0, 0, 0, 0, 1]
    flag_dif = binary_x1[1].index(1) < binary_x2[1].index(1)
    while binary_x1[1] != binary_x2[1]:
        if flag_dif:
            binary_x2[1] = addition(binary_x2[1], one)
        else:
            binary_x1[1] = addition(binary_x1[1], one)
    mantissa = addition(binary_x1[2], binary_x2[2])
    binary_res.append(binary_x1[1])
    binary_res.append(mantissa)
    return binary_res
