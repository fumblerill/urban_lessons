data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(*args):
    s = 0
    args = args[0]

    for item in args:
        if isinstance(item, (list, tuple, dict, set)):
            s += calculate_structure_sum(item)
        elif isinstance(item, str):
            s += len(item)
        else:
            s += item

    return s

print(calculate_structure_sum(data_structure))