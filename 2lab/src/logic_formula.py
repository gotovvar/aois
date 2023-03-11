from .table import *


class LogicFormula:
    def __init__(self, formula: str):
        self.__formula = formula
        self.__table = Table(formula)
        self.__sdnf = self.__create_sdnf()
        self.__sknf = self.__create_sknf()
        self.__binary_sdnf = self.__create_binary_form('sdnf')
        self.__binary_sknf = self.__create_binary_form('sknf')
        self.__decimal_sdnf = self.__create_decimal_form('sdnf')
        self.__decimal_sknf = self.__create_decimal_form('sknf')
        self.__index = self.__create_index()

    def __call__(self):
        print("Таблица истинности:")
        print("a", "b", "c", "result", sep='\t')
        for i in range(len(VALUES)):
            print(self.__table[i].x1, self.__table[i].x2, self.__table[i].x3, self.__table[i].result, sep='\t')
        print("СКНФ:", self.__sknf)
        print("СДНФ:", self.__sdnf)
        print("СКНФ в бинарном виде:", self.__binary_sknf)
        print("СДНФ в бинарном виде:", self.__binary_sdnf)
        print("СКНФ в десятичном виде:", self.__decimal_sknf)
        print("СДНФ в десятичном виде:", self.__decimal_sdnf)
        print("Индекс:", self.__index)

    def __create_sknf(self) -> str:
        sknf = ''
        for i in range(len(VALUES)):
            if self.__table[i].result == 0:
                if sknf:
                    sknf += '*'
                sknf += '(a+' if self.__table[i].x1 == 0 else '(!a+'
                sknf += 'b+' if self.__table[i].x2 == 0 else '!b+'
                sknf += 'c)' if self.__table[i].x3 == 0 else '!c)'
        return sknf if sknf else "Не существует"

    def __create_sdnf(self) -> str:
        sdnf = ''
        for i in range(len(VALUES)):
            if self.__table[i].result == 1:
                if sdnf:
                    sdnf += '+'
                sdnf += '(!a*' if self.__table[i].x1 == 0 else '(a*'
                sdnf += '!b*' if self.__table[i].x2 == 0 else 'b*'
                sdnf += '!c)' if self.__table[i].x3 == 0 else 'c)'
        return sdnf if sdnf else "Не существует"

    def __create_binary_form(self, name: str) -> str:
        if name == 'sdnf':
            if self.__sdnf == "Не существует":
                return self.__sdnf
            value = 1
        else:
            if self.__sknf == "Не существует":
                return self.__sknf
            value = 0
        binary_result = ''
        for i in range(len(VALUES)):
            if self.__table[i].result == value:
                if binary_result:
                    binary_result += ','
                binary_result += str(self.__table[i].x1)
                binary_result += str(self.__table[i].x2)
                binary_result += str(self.__table[i].x3)
        if value == 1:
            binary_result = '+(' + binary_result + ')'
        else:
            binary_result = '*(' + binary_result + ')'
        return binary_result

    def __create_index(self) -> int:
        binary_form = []
        result = 0
        for i in range(len(VALUES)):
            binary_form.append(self.__table[i].result)
        binary_form.reverse()
        for i in range(len(binary_form)):
            result += 2**i * binary_form[i]
        return result

    def __create_decimal_form(self, name: str) -> str:
        decimal_result = ''
        if name == 'sknf':
            if self.__sknf == "Не существует":
                return self.__sknf
            binary_form = self.__binary_sknf[2:len(self.__binary_sknf) - 1]
            sign = '*'
        else:
            if self.__sdnf == "Не существует":
                return self.__sdnf
            binary_form = self.__binary_sdnf[2:len(self.__binary_sdnf) - 1]
            sign = '+'
        if binary_form:
            binary_form = binary_form.split(',')
        for i in range(len(binary_form)):
            decimal_num = 0
            binary_form[i] = binary_form[i][::-1]
            for j in range(len(binary_form[i])):
                if binary_form[i][j] == '1':
                    decimal_num += 2**j
            decimal_result += str(decimal_num) + ','
        return sign + '(' + decimal_result.rstrip(',') + ')'
