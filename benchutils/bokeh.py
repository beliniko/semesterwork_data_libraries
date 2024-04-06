from bokeh.plotting import figure
from bokeh.io.export import get_layout_html

def render(figure):
    get_layout_html(figure)

def linechart(data):
    x, y = data
    p = figure(title='Measurement of a device', x_axis_label='Days', y_axis_label='Temperature in C°')
    p.line(x, y)
    return get_layout_html(p)
