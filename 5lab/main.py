from src import *
from prettytable import PrettyTable


def _make_table():
    elements = ['a', 'b', 'c', 'd', 'function']
    fields_names = [element for element in elements]
    table = PrettyTable(fields_names)
    for function_value in function_values:
        row = [x_value for x_value in function_value.arguments.values()]
        row.append(function_value.value)
        table.add_row(row)
    return table

def main():
    table_h1 = create_sdnf_table(TABLE_H1)
    table_h2 = create_sdnf_table(TABLE_H2)
    table_h3 = create_sdnf_table(TABLE_H3)

    short_form_h1 = get_minimized(table_h1, 'sdnf')
    short_form_h2 = get_minimized(table_h2, 'sdnf')
    short_form_h3 = get_minimized(table_h3, 'sdnf')

    min_h1 = deadlock_calculated_tabular(create_sdnf(TABLE_H1), short_form_h1, '+')
    min_h2 = deadlock_calculated_tabular(create_sdnf(TABLE_H2), short_form_h2, '+')
    min_h3 = deadlock_calculated_tabular(create_sdnf(TABLE_H3), short_form_h3, '+')

    print("h1:", create_sdnf(TABLE_H1))
    print("h2:", create_sdnf(TABLE_H2))
    print("h3:", create_sdnf(TABLE_H3))

    print("Min h1:", min_h1.replace("d", "q3'").replace("c", "q2'").replace("b", "q1'").replace("a", "V"))
    print("Min h2:", min_h2.replace("d", "q3'").replace("c", "q2'").replace("b", "q1'").replace("a", "V"))
    print("Min h3:", min_h3.replace("d", "q3'").replace("c", "q2'").replace("b", "q1'").replace("a", "V"))


if __name__ == '__main__':
    main()
