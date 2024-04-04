import pytest
import matplotlib.pyplot as plt
from io import BytesIO

def data_generator(data_entry_count):
    x = list(range(1, data_entry_count))
    y = [temp ** 2 for temp in x]
    return x, y

def linechart_matplotlib(data):
    x, y = data
    plt.plot(x, y)
    plt.xlabel('Days')
    plt.ylabel('Temperature in C°')
    plt.title('Measurment of a device')
    #plt.show()
    # Create a BytesIO object
    svg_file = BytesIO()
    # Save the figure to the BytesIO object as SVG
    # The 'format' argument ensures the plot is saved as an SVG
    plt.savefig(svg_file, format='svg')
    # Seek to the beginning of the BytesIO object so you can read from it
    svg_file.seek(0)
    # Read the content of the BytesIO object
    svg_bytes = svg_file.getvalue()
    # At this point, svg_bytes contains the SVG data
    return svg_bytes
    # return 123

def test_linechart_matplotlib(benchmark):
    # The benchmark fixture will automatically perform the benchmarking
    data = data_generator(100)
    ll = lambda: TODO_FIX_ME(data)
    result = benchmark(ll, data)  # Measure the time taken to calculate the 10th Fibonacci number

    # You can also assert the result to ensure correctness
    assert result == 123