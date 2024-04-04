import matplotlib.pyplot as plt
from bokeh.plotting import figure, show

def linechart_matplotlib(data):
    x, y = data
    plt.plot(x, y)
    plt.xlabel('Days')
    plt.ylabel('Temperature in C°')
    plt.title('Measurment of a device')
    plt.show()

def linechart_bokeh(data):
    x, y = data
    p = figure(title='Measurement of a device', x_axis_label='Days', y_axis_label='Temperature in C°')
    p.line(x, y)
