from src import *


def main():
    print("Введите логическую формулу")
    formula = input()
    result = LogicFormula(formula)
    result()


if __name__ == "__main__":
    main()
"!((a+!b)*(a*!c))"
"(!a*!b*c)+(!a*b*!c)+(!a*b*c)+(a*b*!c)"
