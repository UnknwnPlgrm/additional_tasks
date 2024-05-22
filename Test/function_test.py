from Src import tasks_10_1

test_list = [
    {'name':'kartoshka', 'price':100, 'category':'vegetable', 'quantity':10},
    {'name':'morkov', 'price':140, 'category':'vegetable', 'quantity':20},
    {'name':'luk', 'price':80, 'category':'vegetable', 'quantity':8},
    {'name':'chesnok', 'price':90, 'category':'vegetable', 'quantity':30},
    {'name':'svekla', 'price':180, 'category':'vegetable', 'quantity':5},
    {'name':'yabloko', 'price':160, 'category':'fruit', 'quantity':40},
    {'name':'sliva', 'price':40, 'category':'fruit', 'quantity':80},
    {'name':'mandarin', 'price':110, 'category':'fruit', 'quantity':50},
    {'name':'chernika', 'price':200, 'category':'berry', 'quantity':6},
    {'name':'arbuz', 'price':250, 'category':'berry', 'quantity':2},
    {'name':'klubnika', 'price':220, 'category':'berry', 'quantity':7}
]
category = ('berry')

print(tasks_10_1.sorted_products_list(test_list, category))