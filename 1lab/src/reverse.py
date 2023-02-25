def to_binary_unsigned(x: int) -> list:
    binary_x = []
    x = abs(x)
    while x:
        binary_x.insert(0, x % 2)
        x //= 2
    for i in range(8 - len(binary_x)):
        binary_x.insert(0, 0)
    return binary_x


def to_binary_straight(x: int) -> list:
    binary_x = to_binary_unsigned(x)
    if x < 0:
        binary_x[0] = 1
    else:
        binary_x[0] = 0
    return binary_x


def straight_to_int(binary_x: list) -> int:
    x = 0
    binary_x.reverse()
    for i in range(0, len(binary_x) - 1):
        x += binary_x[i] * 2 ** i
    if binary_x[-1] == 1:
        x *= -1
    return x


def to_binary_reverse(x: int) -> list:
    binary_x = to_binary_straight(x)
    for i in range(1, len(binary_x)):
        if binary_x[i] == 1:
            binary_x[i] = 0
        else:
            binary_x[i] = 1
    return binary_x


def reverse_to_int(binary_x: list) -> int:
    for i in range(1, len(binary_x)):
        if binary_x[i] == 1:
            binary_x[i] = 0
        else:
            binary_x[i] = 1
    return straight_to_int(binary_x)


def to_binary_addition(x: int) -> list:
    binary_x = to_binary_reverse(x)
    binary_x[-1] += 1
    for i in range(len(binary_x) - 1, 0, -1):
        if binary_x[i] == 2:
            if i - 1 != 0:
                binary_x[i - 1] += 1
            binary_x[i] = 0
        else:
            break
    return binary_x


def addition_to_int(binary_x: list) -> int:
    binary_x[-1] -= 1
    for i in range(len(binary_x) - 1, 0, -1):
        if binary_x[i] == -1:
            if i - 1 != 0:
                binary_x[i - 1] -= 1
            binary_x[i] = 1
        else:
            break
    return reverse_to_int(binary_x)


def translation_helper(binary_x: list) -> int:
    if binary_x[0] == 1:
        return addition_to_int(binary_x)
    else:
        return straight_to_int(binary_x)


def float_to_binary(x1: float, x2: float) -> tuple:
    binary_x1, binary_x2 = [0], [0]
    index_x1 = len(str(x1).split(".")[1])
    index_x2 = len(str(x2).split(".")[1])
    mantissa_x1 = int(str(x1).replace(".", ""))
    mantissa_x2 = int(str(x2).replace(".", ""))
    if index_x1 > index_x2:
        mantissa_x2 = int(str(x2).replace(".", "")) * 10**(index_x1 - index_x2)
    elif index_x2 > index_x1:
        mantissa_x1 = int(str(x1).replace(".", "")) * 10**(index_x2 - index_x1)
    binary_x1.append(to_binary_straight(index_x1))
    binary_x1.append(mantissa_to_binary(mantissa_x1))
    binary_x2.append(to_binary_straight(index_x2))
    binary_x2.append(mantissa_to_binary(mantissa_x2))
    return binary_x1, binary_x2


def mantissa_to_binary(mantissa: int) -> list:
    binary_mantissa = []
    while mantissa:
        binary_mantissa.insert(0, mantissa % 2)
        mantissa //= 2
    for i in range(23 - len(binary_mantissa)):
        binary_mantissa.insert(0, 0)
    return binary_mantissa
