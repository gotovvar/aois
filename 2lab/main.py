from src import *


def main():
    while True:
        print("Введите логическую формулу")
        formula = input()
        if formula == 'end':
            break
        result = LogicFormula(formula)
        result()


if __name__ == "__main__":
    main()


"!((a+!b)*(a*!c))"