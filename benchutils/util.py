def data_generator(data_entry_count):
    x = list(range(1, data_entry_count))
    y = [temp ** 2 for temp in x]
    return x, y


def piechart_data_generator(size):
    labels = [f"Label-{i+1}" for i in range(size+1)]
    values = list(range(1, size+1))
    data = list(map(lambda x, y: (x, y), labels, values))
    return data

