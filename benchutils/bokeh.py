from bokeh.plotting import figure
from bokeh.io.export import get_layout_html
from bokeh.palettes import Category20_20
from bokeh.plotting import figure, show
from bokeh.transform import cumsum
import pandas as pd
from math import pi

def init():
    return None

def render(figure):
    return get_layout_html(figure)

def linechart(data):
    x, y = data
    p = figure(title='Measurement of a device', x_axis_label='Days', y_axis_label='Temperature in C°')
    p.line(x, y)
    # show(p)
    return render(p)

def barchart(data):
    x, y = data
    p = figure(title='Measurement of a device', x_axis_label='Days', y_axis_label='Temperature in C°')
    p.vbar(x=x, top=y, legend_label="Rate", width=0.5, bottom=0, color="red")
    # show(p)
    return render(p)

def piechart(data):
    x = dict(data)
    bokeh_data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'country'})
    bokeh_data['angle'] = bokeh_data['value'] / bokeh_data['value'].sum() * 2*pi
    colors = [Category20_20[i % len(Category20_20)] for i in range(len(x))]
    bokeh_data['color'] = colors

    p = figure(height=350, title="Pie Chart", toolbar_location=None,
               tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='country', source=bokeh_data)

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None
    # show(p)
    return render(p)
