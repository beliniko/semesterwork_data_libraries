import timeit
import matplotlib.pyplot as plt


def runtime_of_barchart():
    x = list(range(1, 6))
    y = [temp ** 2 for temp in x]
    plt.bar(x, y)
    plt.xlabel('Days')
    plt.ylabel('Temperature in C°')
    plt.title('Measurement of a device')
    file_name = f'line_chart_.png'
    plt.savefig(file_name)
    plt.close()


runtime = timeit.timeit(stmt=runtime_of_barchart, number=5)
average = runtime / 5
print(f'Runtime of the barchart with matplotlib: {average}, seconds ')
