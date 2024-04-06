import pytest
from benchutils import util
from benchutils import matplotlib
from benchutils import bokeh

# Define test data sizes for parameterization
data_sizes = [10, 100, 1000, 10000]

# The benchmark fixture will automatically perform the benchmarking

@pytest.mark.parametrize('data_size', data_sizes)
def test_linechart_matplotlib(benchmark, data_size):
    data = util.data_generator(data_size)
    testee = lambda: matplotlib.linechart(data)
    result = benchmark(testee)  # Measure the time taken to calculate the 10th Fibonacci number
    assert result

@pytest.mark.parametrize('data_size', data_sizes)
def test_linechart_bokeh(benchmark, data_size):
    data = util.data_generator(data_size)
    testee = lambda: bokeh.linechart(data)
    result = benchmark(testee)  # Measure the time taken to calculate the 10th Fibonacci number
    assert result

@pytest.mark.parametrize('data_size', data_sizes)
def test_barchart_matplotlib(benchmark, data_size):
    data = util.data_generator(data_size)
    testee = lambda: matplotlib.barchart(data)
    result = benchmark(testee)  # Measure the time taken to calculate the 10th Fibonacci number
    assert result