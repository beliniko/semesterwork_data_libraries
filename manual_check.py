from benchutils import bokeh
from benchutils import matplotlib
from benchutils import util

from matplotlib import pyplot as plt

# bokeh.linechart(util.data_generator(1000))
# bokeh.barchart(util.data_generator(1000))
# bokeh.piechart(util.piechart_data_generator(1000))

matplotlib.barchart(util.data_generator(1000))
matplotlib.linechart(util.data_generator(1000))
matplotlib.piechart(util.piechart_data_generator(256))

plt.show()