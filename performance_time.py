import timeit
import matplotlib.pyplot as plt
from io import BytesIO
from bokeh.plotting import figure, show
# from bokeh.io import export_svg
from bokeh.io.export import get_layout_html

import time

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
#     return 123

def linechart_bokeh(data):
    x, y = data
    p = figure(title='Measurement of a device', x_axis_label='Days', y_axis_label='Temperature in C°')
    p.line(x, y)
    # show(p)

    html = get_layout_html(p)

    # print(html)

    # Use a temporary file to save the plot
    # with tempfile.NamedTemporaryFile(delete=False, suffix=".svg") as temp:
    #     export_svg(p, filename=temp.name)
    #     temp_path = temp.name
    # Read the temporary file back into a byte array
    # with open(temp_path, "rb") as f:
    #     img_bytes = f.read()
    # Clean up the temporary file
    # os.remove(temp_path)

def data_generator(data_entry_count):
    x = list(range(1, data_entry_count))
    y = [temp ** 2 for temp in x]
    return x, y

data_generator(11)

# Adjusted for correct functionality
def performance(datavisu_function, timeit_number, *args):
    # Using a lambda function to pass the arguments correctly
    runtime = timeit.timeit(lambda: datavisu_function(*args), number=timeit_number) / timeit_number
    return runtime


# Correct usage
data = data_generator(10000)  # Generate data

def data_vis_mock(data):
    time.sleep(0.2)
    return 123

# warm-up:
performance(linechart_bokeh, 10, data)  # Measure performance

runtime = performance(linechart_bokeh, 100, data)  # Measure performance

print(runtime)

