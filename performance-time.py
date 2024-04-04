import timeit
import matplotlib.pyplot as plt
from io import BytesIO
from bokeh.plotting import figure, show
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

def linechart_bokeh(data):
    x, y = data
    p = figure(title='Measurement of a device', x_axis_label='Days', y_axis_label='Temperature in C°')
    p.line(x, y)
    show(p)
def data_generator(data_entry_count):
    x = list(range(1, data_entry_count))
    y = [temp ** 2 for temp in x]
    return x, y

data_generator(11)

timeit_number = 10

# Adjusted for correct functionality
def performance(datavisu_function, *args):
    # Using a lambda function to pass the arguments correctly
    runtime = timeit.timeit(lambda: datavisu_function(*args), number=timeit_number) / timeit_number
    return runtime


# Correct usage
data = data_generator(11)  # Generate data
runtime = performance(linechart_matplotlib, data)  # Measure performance

print(runtime)