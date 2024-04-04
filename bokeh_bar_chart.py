import timeit
from bokeh.plotting import figure, show
from bokeh.io.export import get_screenshot_as_png, export_png
from io import BytesIO

def runtime_of_barchart():
    x = list(range(1, 20001))
    y = [temp**2 for temp in x]
    p = figure(title='Measurement of a device', x_axis_label='Days', y_axis_label='Temperature in C°')
    p.vbar(x=x, top=y, legend_label="Rate", width=0.5, bottom=0, color="red")
    show(p)

runtime = timeit.timeit(stmt=runtime_of_barchart, number=5)
print(f'Runtime of the barchart with bokeh: {runtime / 5}, seconds ')

def bokeh_linechart_svg():
    x = list(range(1, 20001))
    y = [temp**2 for temp in x]
    p = figure(title='Measurement of a device', x_axis_label='Days', y_axis_label='Temperature in C°')
    p.line(x, y)
    p.output_backend = "svg"