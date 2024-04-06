from io import BytesIO
import matplotlib.pyplot as plt

def init():
    plt.clf()
    plt.cla()

def render(figure):
    # Create a BytesIO object
    svg_file = BytesIO()
    # Save the figure to the BytesIO object as SVG
    # The 'format' argument ensures the plot is saved as an SVG
    figure.savefig(svg_file, format='svg')
    # Seek to the beginning of the BytesIO object so you can read from it
    svg_file.seek(0)
    # Read the content of the BytesIO object
    svg_bytes = svg_file.getvalue()
    # At this point, svg_bytes contains the SVG data
    return svg_bytes

def linechart(data):
    x, y = data
    plt.plot(x, y)
    plt.xlabel('Days')
    plt.ylabel('Temperature in C°')
    plt.title('Measurment of a device')
    # plt.show()
    return render(plt)

def barchart(data):
    x, y = data
    plt.bar(x, y)
    plt.xlabel('Days')
    plt.ylabel('Temperature in C°')
    plt.title('Measurment of a device')
    # plt.show()
    return render(plt)

def piechart(data):
    labels, sizes = zip(*data)
    plt.pie(sizes, labels=labels)
    # plt.show()
    return render(plt)
