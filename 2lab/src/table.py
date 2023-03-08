from .table_row import *
from .constants import *


class Table:
    def __init__(self, formula: str):
        self.__table = self.__create_table(VALUES, formula)

    def __getitem__(self, item):
        return self.__table[item]

    def __create_table(self, data: list, formula: str):
        table = [TableRow(*row) for row in data]
        for i in range(len(VALUES)):
            table[i].result = self.__result(formula, table[i].x1, table[i].x2, table[i].x3)
        return table

    def __result(self, formula, x1, x2, x3):
        stack = []
        polska = self.__translation_to_polska(formula, x1, x2, x3)
        for i in polska:
            if i.isdigit():
                stack.append(i)
            elif i == '+':
                cnt1, cnt2 = stack.pop(), stack.pop()
                stack.append(1 if int(cnt1) or int(cnt2) else 0)
            elif i == '*':
                cnt1, cnt2 = stack.pop(), stack.pop()
                stack.append(1 if int(cnt1) and int(cnt2) else 0)
            elif i == '!':
                cnt1 = stack.pop()
                stack.append(0 if int(cnt1) else 1)
        return stack.pop()

    @staticmethod
    def __translation_to_polska(formula, x1, x2, x3):
        temp, result = [], []
        formula = formula.replace("a", str(x1))
        formula = formula.replace("b", str(x2))
        formula = formula.replace("c", str(x3))

        for t in formula:
            if t.isdigit():
                result.append(t)
            elif t == '(':
                temp.append(t)
            elif t == ')':
                top = temp.pop()
                while top != '(':
                    result.append(top)
                    top = temp.pop()
            else:
                while temp and OPERATIONS[temp[-1]] >= OPERATIONS[t]:
                    result.append(temp.pop())
                temp.append(t)
        while temp:
            result.append(temp.pop())
        return result
