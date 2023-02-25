from src import *


def main():
    while True:

        print("Введите операцию: сумма(+), сумма с плавающей точкой(+.), умножение(*), деление(/), ")
        operation = input()

        if operation == "+":

            print("Введите 2 числа")

            x1, x2 = map(int, input().split())
            neg_x1 = -1 * x1
            neg_x2 = -1 * x2

            print(f"{x1} + {x2} = ", end="")
            res = addition(to_binary_straight(x1), to_binary_straight(x2))
            print(straight_to_int(res))
            print(f"Ответ в бинарном виде: {res[-1::-1]}")

            print(f"-{x1} + {x2} = ", end="")
            res = addition(to_binary_addition(neg_x1), to_binary_straight(x2))
            print(translation_helper(res))
            print(f"Ответ в бинарном виде: {res[-1::-1]}")

            print(f"{x1} - {x2} = ", end="")
            res = addition(to_binary_straight(x1), to_binary_addition(neg_x2))
            print(translation_helper(res))
            print(f"Ответ в бинарном виде: {res[-1::-1]}")

            print(f"-{x1} - {x2} = ", end="")
            res = addition(to_binary_addition(neg_x1), to_binary_addition(neg_x2))
            print(addition_to_int(res))
            print(f"Ответ в бинарном виде: {res[-1::-1]}")

        elif operation == "+.":

            print("Введите 2 числа")

            x1, x2 = map(float, input().split())

            print(f"{x1} + {x2} = ", end="")
            res = float_addition(*float_to_binary(x1, x2))
            print(print_binary_float(res))
            res[1] = res[1][-1::-1]
            res[2] = res[2][-1::-1]
            print(res)

        elif operation == "*":

            print("Введите 2 числа")

            x1, x2 = map(int, input().split())
            neg_x1 = -1 * x1
            neg_x2 = -1 * x2

            print(f"{x1} * {x2} = ", end="")
            res = multiplication(to_binary_straight(x1), to_binary_straight(x2))
            print(straight_to_int(res))
            print(f"Ответ в бинарном виде: {res[-1::-1]}")

            print(f"-{x1} * {x2} = ", end="")
            res = multiplication(to_binary_straight(neg_x1), to_binary_straight(x2))
            print(straight_to_int(res))
            print(f"Ответ в бинарном виде: {res[-1::-1]}")

            print(f"{x1} * (-{x2}) = ", end="")
            res = multiplication(to_binary_straight(x1), to_binary_straight(neg_x2))
            print(straight_to_int(res))
            print(f"Ответ в бинарном виде: {res[-1::-1]}")

            print(f"-{x1} * (-{x2}) = ", end="")
            res = multiplication(to_binary_straight(neg_x1), to_binary_straight(neg_x2))
            print(straight_to_int(res))
            print(f"Ответ в бинарном виде: {res[-1::-1]}")

        elif operation == "/":

            print("Введите 2 числа")

            x1, x2 = map(int, input().split())
            neg_x1 = -1 * x1
            neg_x2 = -1 * x2

            print(f"{x1} / {x2} = ", end="")
            res = division(to_binary_straight(x1), to_binary_straight(x2))
            print(straight_to_int(res))
            print(f"Ответ в бинарном виде: {res[-1::-1]}")

            print(f"-{x1} / ({x2}) = ", end="")
            res = division(to_binary_straight(neg_x1), to_binary_straight(x2))
            print(straight_to_int(res))
            print(f"Ответ в бинарном виде: {res[-1::-1]}")

            print(f"{x1} / (-{x2}) = ", end="")
            res = division(to_binary_straight(x1), to_binary_straight(neg_x2))
            print(straight_to_int(res))
            print(f"Ответ в бинарном виде: {res[-1::-1]}")

            print(f"-{x1} / (-{x2}) = ", end="")
            res = division(to_binary_straight(neg_x1), to_binary_straight(neg_x2))
            print(straight_to_int(res))
            print(f"Ответ в бинарном виде: {res[-1::-1]}")

        else:
            break


if __name__ == "__main__":
    main()
