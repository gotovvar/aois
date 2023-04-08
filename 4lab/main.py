from src import *


table_p = create_sknf_table(TABLE_Bi1)
table_s = create_sknf_table(TABLE_Di)

short_form_p = get_minimized(table_p, 'sknf')
short_form_s = get_minimized(table_s, 'sknf')

print("Min P:", deadlock_calculated_tabular(create_sknf(TABLE_Bi1), short_form_p, '*'))
print("Min S:", deadlock_calculated_tabular(create_sknf(TABLE_Di), short_form_s, '*'))

table_y1 = create_sdnf_table(TABLE_Y1)
short_form_y1 = get_minimized(table_y1, 'sdnf')
table_y2 = create_sdnf_table(TABLE_Y2)
short_form_y2 = get_minimized(table_y2, 'sdnf')
table_y3 = create_sdnf_table(TABLE_Y3)
short_form_y3 = get_minimized(table_y3, 'sdnf')
table_y4 = create_sdnf_table(TABLE_Y4)
short_form_y4 = get_minimized(table_y4, 'sdnf')

print("Min Y1:", deadlock_calculated_tabular(create_sdnf(TABLE_Y1), short_form_y1, '+'))
print("Min Y2:", deadlock_calculated_tabular(create_sdnf(TABLE_Y2), short_form_y2, '+'))
print("Min Y3:", deadlock_calculated_tabular(create_sdnf(TABLE_Y3), short_form_y3, '+'))
print("Min Y4:", deadlock_calculated_tabular(create_sdnf(TABLE_Y4), short_form_y4, '+'))
