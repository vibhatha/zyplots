from matplotlib import pyplot as plt
import numpy as np


class LineChart:

    def __init__(self, data: list = [], legend: list = [], title: str = 'Title',
                 xaxis_title: str = 'x-axis', yaxis_title: str = 'y-axis', xticks: list = [],
                 fig_save_path:str=''):
        self._data = data
        self._legend = legend
        self._title = title
        self._xaxis_title = xaxis_title
        self._yaxis_title = yaxis_title
        self._xticks = xticks
        self._fig_save_path = fig_save_path

    def plot(self):
        print(self._data, self._legend)
        x = np.array(self._xticks)
        fig, ax = plt.subplots()

        for item in self._data:
            ax.plot(x, np.array(item))


        ax.set_title(self._title)
        ax.legend(self._legend)
        ax.xaxis.set_label_text(self._xaxis_title)
        ax.yaxis.set_label_text(self._yaxis_title)
        #ax.set_xticklabels(x)
        plt.grid()
        plt.savefig(self._fig_save_path)
        plt.show()
