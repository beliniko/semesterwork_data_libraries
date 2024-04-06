def data_generator(data_entry_count):
    x = list(range(1, data_entry_count))
    y = [temp ** 2 for temp in x]
    return x, y
