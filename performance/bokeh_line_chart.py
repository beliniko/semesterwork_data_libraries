import timeit
from bokeh.plotting import figure, show
from bokeh.io.export import get_screenshot_as_png, export_png
from io import BytesIO
def runtime_of_linechart():
    x = list(range(1, 20001))
    y = [temp**2 for temp in x]
    p = figure(title='Measurement of a device', x_axis_label='Days', y_axis_label='Temperature in C°')
    p.line(x, y)
    img_bytes = BytesIO()  # Erstellen eines BytesIO-Objekts als Ziel für das PNG
    export_png(p, filename=img_bytes)  # Speichern des PNG in BytesIO
    return img_bytes  # Rückgabe des BytesIO-Objekts


runtime = timeit.timeit(stmt=runtime_of_linechart, number=5)
print(f'Runtime of the linechart with bokeh: {runtime / 5}, seconds')