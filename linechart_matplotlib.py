import matplotlib.pyplot as plt

def datavisu_function(data):
    x, y = data
    plt.plot(x, y)
    plt.xlabel('Days')
    plt.ylabel('Temperature in C°')
    plt.title('Measurment of a device')
    plt.show()
