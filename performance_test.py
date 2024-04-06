import pytest
from benchutils import util
from benchutils import matplotlib
from benchutils import bokeh

# Define test data sizes for parameterization
data_sizes = [10, 100, 1000, 10000]

piechart_data_sizes = [6, 12, 24, 48]

# The benchmark fixture will automatically perform the benchmarking

@pytest.mark.linechart
@pytest.mark.parametrize('data_size', data_sizes)
def test_linechart_matplotlib(benchmark, data_size):
    matplotlib.init()
    data = util.data_generator(data_size)
    testee = lambda: matplotlib.linechart(data)
    result = benchmark(testee)  # Measure the time taken to calculate the 10th Fibonacci number
    assert result

@pytest.mark.linechart
@pytest.mark.parametrize('data_size', data_sizes)
def test_linechart_bokeh(benchmark, data_size):
    data = util.data_generator(data_size)
    testee = lambda: bokeh.linechart(data)
    result = benchmark(testee)  # Measure the time taken to calculate the 10th Fibonacci number
    assert result

@pytest.mark.barchart
@pytest.mark.parametrize('data_size', data_sizes)
def test_barchart_matplotlib(benchmark, data_size):
    matplotlib.init()
    data = util.data_generator(data_size)
    testee = lambda: matplotlib.barchart(data)
    result = benchmark(testee)  # Measure the time taken to calculate the 10th Fibonacci number
    assert result

@pytest.mark.barchart
@pytest.mark.parametrize('data_size', data_sizes)
def test_barchart_bokeh(benchmark, data_size):
    data = util.data_generator(data_size)
    testee = lambda: bokeh.barchart(data)
    result = benchmark(testee)  # Measure the time taken to calculate the 10th Fibonacci number
    assert result

@pytest.mark.piechart
@pytest.mark.parametrize('data_size', piechart_data_sizes)
def test_pie_matplotlib(benchmark, data_size):
    matplotlib.init()
    data = util.piechart_data_generator(data_size)
    testee = lambda: matplotlib.piechart(data)
    result = benchmark(testee)  # Measure the time taken to calculate the 10th Fibonacci number
    assert result

@pytest.mark.piechart
@pytest.mark.parametrize('data_size', piechart_data_sizes)
def test_pie_bokeh(benchmark, data_size):
    data = util.piechart_data_generator(data_size)
    testee = lambda: bokeh.piechart(data)
    result = benchmark(testee)  # Measure the time taken to calculate the 10th Fibonacci number
    assert result