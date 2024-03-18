import timeit
import matplotlib.pyplot as plt


def runtime_of_linechart():
    x = list(range(1, 6))
    y = [temp**2 for temp in x]
    plt.plot(x, y)
    plt.xlabel('Days')
    plt.ylabel('Temperature in C°')
    plt.title('Measurment of a device')
    file_name = f'line_chart_.png'
    plt.savefig(file_name)
    plt.close()


runtime = timeit.timeit(stmt=runtime_of_linechart, number=5)
print(f'Runtime of the linechart with matplotlib: {runtime / 5}, seconds ')
