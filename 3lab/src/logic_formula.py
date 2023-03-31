from .table import *


class LogicFormula:
    def __init__(self, formula: str):
        self.__formula = formula
        self.__table = Table(formula)

        self.__sdnf = self.__create_sdnf()
        self.__sknf = self.__create_sknf()

        self.__sknf_short_form = self.get_minimized("sknf")
        self.__sdnf_short_form = self.get_minimized("sdnf")

        self.__sknf_calculate_deadlock = self.calculated_deadlock("sknf")
        self.__sdnf_calculate_deadlock = self.calculated_deadlock("sdnf")

        self.__sknf_deadlock_calculated_tabular = self.deadlock_calculated_tabular("sknf")
        self.__sdnf_deadlock_calculated_tabular = self.deadlock_calculated_tabular("sdnf")

        self.__sknf_deadlock_tabular = self.deadlock_tabular("sknf")
        self.__sdnf_deadlock_tabular = self.deadlock_tabular("sdnf")

    def __call__(self):
        print("Таблица истинности:")
        print("a", "b", "c", "result", sep='\t')
        for i in range(len(VALUES)):
            print(self.__table[i].x1, self.__table[i].x2, self.__table[i].x3, self.__table[i].result, sep='\t')
        print("СКНФ:", self.__sknf)
        print("СДНФ:", self.__sdnf)
        print("ТДНФ(расчетный метод):", self.__sdnf_calculate_deadlock)
        print("ТКНФ(расчетный метод):", self.__sknf_calculate_deadlock)
        print("ТДНФ(таблично-расчетный метод):", self.__sdnf_deadlock_calculated_tabular)
        print("ТКНФ(таблично-расчетный метод):", self.__sknf_deadlock_calculated_tabular)
        print("ТДНФ(табличный метод):", self.__sdnf_deadlock_tabular)
        print("ТКНФ(табличный метод):", self.__sknf_deadlock_tabular)

    def __is_constant_function(self, name):
        if name == "sdnf":
            value = 1
        else:
            value = 0
        constant = True
        for i in range(len(VALUES)):
            if self.__table[i].result != value:
                constant = False
                break
        return constant

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

    def __create_sdnf_table(self):
        sdnf_table = []
        for i in range(len(VALUES)):
            if self.__table[i].result == 1:
                sdnf_table.append([self.__table[i].x1, self.__table[i].x2, self.__table[i].x3])
        return sdnf_table

    def __create_sknf_table(self):
        sknf_table = []
        for i in range(len(VALUES)):
            if self.__table[i].result == 0:
                sknf_table.append([self.__table[i].x1, self.__table[i].x2, self.__table[i].x3])
        return sknf_table

    @staticmethod
    def __delete_duplicate(table):
        new_table = []
        for vector in table:
            if vector not in new_table:
                new_table.append(vector)
        return new_table

    @staticmethod
    def __create_short_logic_table(table) -> list:
        result = []
        if not len(table):
            return []

        for i in range(len(table[0])):
            short_logic_table = LogicFormula.__start_glued(table)
            table = LogicFormula.__delete_duplicate(short_logic_table)
            result = table
        return LogicFormula.__delete_duplicate(result)

    @staticmethod
    def __start_glued(table):
        short_logic_table = []
        index = []
        for i in range(len(table)):
            is_not_gluing = False
            for j in range(i+1, len(table)):
                false_index = LogicFormula.__gluing_of_vectors(table[i], table[j])
                if false_index >= 0:
                    is_not_gluing = True
                    index.append(j)
                    new_vector = table[i].copy()
                    new_vector[false_index] = None
                    short_logic_table.append(new_vector)
            if not is_not_gluing and i not in index:
                short_logic_table.append(table[i])
        return short_logic_table if short_logic_table else table

    @staticmethod
    def __gluing_of_vectors(first_vector, second_vector):
        result_vector = []
        for i in range(len(first_vector)):
            result_vector.append(first_vector[i] == second_vector[i])
        if result_vector.count(False) == 1:
            return result_vector.index(False)
        return -1

    def get_minimized(self, name):
        if name == "sdnf":
            table = self.__create_sdnf_table()
            create_short_form = self.__create_short_sdnf_form
        else:
            table = self.__create_sknf_table()
            create_short_form = self.__create_short_sknf_form
        short_logic_table = self.__create_short_logic_table(table)
        short_form = create_short_form(short_logic_table)
        return short_form

    @staticmethod
    def __create_short_sdnf_form(sdnf_table):
        short_form = ""
        elements = {'0': 'a', '1': 'b', '2': 'c'}
        for i in range(len(sdnf_table)):
            if short_form:
                short_form += '+'
            short_form += '('
            for j in range(len(sdnf_table[i])):
                if sdnf_table[i][j] is not None:
                    short_form += '!' + elements[str(j)] if sdnf_table[i][j] == 0 else elements[str(j)]
                    short_form += '*'
            short_form = short_form.rstrip('*') + ')'
        return short_form if short_form else "Не существует"

    @staticmethod
    def __create_short_sknf_form(sknf_table):
        short_form = ""
        elements = {'0': 'a', '1': 'b', '2': 'c'}
        for i in range(len(sknf_table)):
            if short_form:
                short_form += '*'
            short_form += '('
            for j in range(len(sknf_table[i])):
                if sknf_table[i][j] is not None:
                    short_form += elements[str(j)] if sknf_table[i][j] == 0 else '!' + elements[str(j)]
                    short_form += '+'
            short_form = short_form.rstrip('+') + ')'
        return short_form if short_form else "Не существует"

    @staticmethod
    def __is_includes(term_of_short, term_of_base):
        is_includes = True
        for term in term_of_short:
            if term not in term_of_base:
                is_includes = False
        return is_includes

    @staticmethod
    def __fill_calculated_tabular_table(formula, short_form, sign):
        sign = '+' if sign == '*' else '*'
        table = dict()
        for col in formula:
            table[col] = dict()
        for col in formula:
            for row in short_form:
                if LogicFormula.__is_includes(row[1:-1].split(sign), col[1:-1].split(sign)) and len(row[1:-1]) > 2:
                    table[col][row] = 1
                else:
                    table[col][row] = 0
        return table

    @staticmethod
    def __is_important(formula, vector):
        if vector.count(None) == 1:
            none_index = vector.index(None)
            first_vector, second_vector = vector.copy(), vector.copy()
            second_vector[none_index], first_vector[none_index] = 0, 1
            return Table.result(formula, *first_vector) == Table.result(formula, *second_vector)
        return False

    def calculated_deadlock(self, name):
        if self.__is_constant_function(name):
            return 1 if name == 'sdnf' else 0
        if name == "sdnf":
            sign = '+'
            short_form = self.__sdnf_short_form
            short_logic_table = self.__create_short_logic_table(self.__create_sdnf_table())
        else:
            sign = '*'
            short_form = self.__sknf_short_form
            short_logic_table = self.__create_short_logic_table(self.__create_sknf_table())
        terms = short_form.split(sign)
        if len(terms) <= 2:
            return sign.join(terms)
        for i in range(len(short_logic_table)):
            formula = short_form.split(sign)
            formula.pop(i)
            formula = sign.join(formula)
            if self.__is_important(formula, short_logic_table[i]):
                terms[i] = ""
        terms = sign.join(terms).strip(sign)
        while sign * 2 in terms:
            terms = terms.replace(sign * 2, sign)
        return terms

    def deadlock_calculated_tabular(self, name):
        if self.__is_constant_function(name):
            return 1 if name == 'sdnf' else 0
        if name == "sdnf":
            sign = '+'
            short_form = self.__sdnf_short_form.split(sign)
            formula = self.__sdnf.split(sign)
        else:
            sign = '*'
            short_form = self.__sknf_short_form.split(sign)
            formula = self.__sknf.split(sign)
        if len(short_form) == 1:
            return ''.join(short_form)
        terms = []
        for i in short_form:
            if len(i) <= 4:
                terms.append(i)
        table = self.__fill_calculated_tabular_table(formula, short_form, sign)
        for term in formula:
            count_of_one = list(table[term].values()).count(1)
            if count_of_one == 1:
                for implicate_from_short in short_form:
                    if table[term][implicate_from_short] == 1 and implicate_from_short not in terms:
                        terms.append(implicate_from_short)
        return sign.join(terms)

    def __fill_tabular_table(self):
        table = self.__create_sdnf_table()
        tabular_table = dict()
        for col in VALUES_A:
            tabular_table[col] = dict()
        for col in VALUES_A:
            for row in VALUES_B_C:
                if [col, row[0], row[1]] in table:
                    tabular_table[col][row] = 1
                else:
                    tabular_table[col][row] = 0
        return tabular_table

    @staticmethod
    def __is_includes_in_area(original_vector, areas):
        for area in areas:
            is_includes = False
            for constituent in original_vector:
                if constituent not in area:
                    is_includes = True
            if not is_includes:
                return False
        return True

    @staticmethod
    def __is_extra_area(original_vector, areas):
        is_includes_count = 0
        for constituent in original_vector:
            for area in areas:
                if constituent in area and area != original_vector:
                    is_includes_count += 1
                    break
        return is_includes_count != len(original_vector)


    @staticmethod
    def __checking_signle_area(table, value, areas):
        for constituent in VALUES_A:
            for j in range(len(VALUES_B_C)):
                if table[constituent][VALUES_B_C[j]] == value\
                  and LogicFormula.__is_includes_in_area([[constituent, *VALUES_B_C[j]]], areas):
                    areas.append([[constituent, *VALUES_B_C[j]]])
        return areas

    @staticmethod
    def __checking_line_of_two_area(table, value, areas):
        for constituent in VALUES_A:
            for j in range(len(VALUES_B_C)):
                if table[constituent][VALUES_B_C[0]] == table[constituent][VALUES_B_C[-1]] == value:
                    area = [[constituent, *VALUES_B_C[0]], [constituent, *VALUES_B_C[-1]]]
                    if LogicFormula.__is_includes_in_area(area, areas):
                        areas.append(area)
                if j + 1 < len(VALUES_B_C):
                    if table[constituent][VALUES_B_C[j + 1]] == table[constituent][VALUES_B_C[j]] == value:
                        area = [[constituent, *VALUES_B_C[j + 1]], [constituent, *VALUES_B_C[j]]]
                        if LogicFormula.__is_includes_in_area(area, areas):
                            areas.append(area)
                if constituent + 1 < 2:
                    if table[constituent + 1][VALUES_B_C[j]] == table[constituent][VALUES_B_C[j]] == value:
                        area = [[constituent + 1, *VALUES_B_C[j]], [constituent, *VALUES_B_C[j]]]
                        if LogicFormula.__is_includes_in_area(area, areas):
                            areas.append(area)
        return areas

    @staticmethod
    def __checking_square_area(table, value, areas):
        for j in range(len(VALUES_B_C)):
            if j + 1 < len(VALUES_B_C):
                if table[0][VALUES_B_C[j + 1]] == table[0][VALUES_B_C[j]] == value\
                  and table[1][VALUES_B_C[j + 1]] == table[1][VALUES_B_C[j]] == value:
                    area = [[0, *VALUES_B_C[j+1]], [0, *VALUES_B_C[j]], [1, *VALUES_B_C[j+1]], [1, *VALUES_B_C[j]]]
                    if LogicFormula.__is_includes_in_area(area, areas):
                        areas.append(area)
        if table[0][VALUES_B_C[0]] == table[0][VALUES_B_C[-1]] == value \
                and table[1][VALUES_B_C[0]] == table[1][VALUES_B_C[-1]] == value:
            area = [[0, *VALUES_B_C[0]], [0, *VALUES_B_C[-1]], [1, *VALUES_B_C[0]], [1, *VALUES_B_C[-1]]]
            if LogicFormula.__is_includes_in_area(area, areas):
                areas.append(area)
        return areas

    @staticmethod
    def __checking_line_of_four_area(table, value, areas):
        for constituent in VALUES_A:
            is_line = True
            for j in range(len(VALUES_B_C)):
                if table[constituent][VALUES_B_C[j]] != value:
                    is_line = False
                    break
            area = [[constituent, *VALUES_B_C[0]], [constituent, *VALUES_B_C[1]],
                    [constituent, *VALUES_B_C[2]], [constituent, *VALUES_B_C[3]]]
            if is_line and LogicFormula.__is_includes_in_area(area, areas):
                areas.append(area)
        return areas

    @staticmethod
    def __minimizing_areas(areas):
        result = areas.copy()
        for i in range(len(areas)):
            if not LogicFormula.__is_extra_area(areas[i], result):
                result.remove(areas[i])
        return result

    def deadlock_tabular(self, name):
        if self.__is_constant_function(name):
            return 1 if name == 'sdnf' else 0
        if name == "sdnf":
            sign, value = '+', 1
            short_form, create_short_form = self.__sdnf_short_form.split(sign), self.__create_short_sdnf_form
        else:
            sign, value = '*', 0
            short_form, create_short_form = self.__sknf_short_form.split(sign), self.__create_short_sknf_form

        if len(short_form) == 1:
            return ''.join(short_form)

        areas, result = [], []
        table = self.__fill_tabular_table()

        areas = self.__checking_line_of_four_area(table, value, areas)
        areas = self.__checking_square_area(table, value, areas)
        areas = self.__checking_line_of_two_area(table, value, areas)
        areas = self.__checking_signle_area(table, value, areas)

        areas = self.__minimizing_areas(areas)

        for area in areas:
            result.extend(self.__create_short_logic_table(area))
        return create_short_form(result)
