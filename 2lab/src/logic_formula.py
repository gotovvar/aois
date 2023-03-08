from .table import *


class LogicFormula:
    def __init__(self, formula: str):
        self.__formula = formula
        self.__table = Table(formula)
        self.__sknf = self.__create_sknf()
        self.__sdnf = self.__create_sdnf()

    def __call__(self):
        print("Таблица истинности:")
        print("a", "b", "c", "result", sep='\t')
        for i in range(8):
            print(self.__table[i].x1, self.__table[i].x2, self.__table[i].x3, self.__table[i].result, sep='\t')
        print("СКНФ: ")
        print(self.__sknf)
        print("СДНФ: ")
        print(self.__sdnf)

    def __create_sknf(self):
        sknf = ''
        for i in range(8):
            if self.__table[i].result == 0:
                if sknf:
                    sknf += '*'
                sknf += '(a+' if self.__table[i].x1 == 0 else '(!a+'
                sknf += 'b+' if self.__table[i].x2 == 0 else '!b+'
                sknf += 'c)' if self.__table[i].x3 == 0 else '!c)'
            else:
                continue
        return sknf

    def __create_sdnf(self):
        sdnf = ''
        for i in range(8):
            if self.__table[i].result == 1:
                if sdnf:
                    sdnf += '+'
                sdnf += '(!a*' if self.__table[i].x1 == 0 else '(a*'
                sdnf += '!b*' if self.__table[i].x2 == 0 else 'b*'
                sdnf += '!c)' if self.__table[i].x3 == 0 else 'c)'
            else:
                continue
        return sdnf
