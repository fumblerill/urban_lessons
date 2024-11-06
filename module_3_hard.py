data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data):
    s = 0

    if isinstance(data, (list, tuple, set)):
        for item in data:
            s += calculate_structure_sum(item)
    elif isinstance(data, dict):
        for key, value in data.items():
            s += calculate_structure_sum(key)
            s += calculate_structure_sum(value)
    elif isinstance(data, str):
        s += len(data)
    elif isinstance(data, int):
        s += data

    return s

print(calculate_structure_sum(data_structure))