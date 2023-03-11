from src import *


def main():
    print("Введите логическую формулу")
    formula = input()
    result = LogicFormula(formula)
    result()


if __name__ == "__main__":
    main()
