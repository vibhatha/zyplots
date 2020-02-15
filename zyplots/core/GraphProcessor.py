from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


class GraphProcessor:

    def __init__(self, dataframe: pd.DataFrame, cols=[]):
        if dataframe is None or not cols:
            raise Exception("Dataframe must not be None or Cols is empty")
        self.data_frame = dataframe
        self.usecols = cols
        self.extrac_data_list = None
        self._pre_process_data()

    def _pre_process_data(self):
        size_of_cols = len(self.usecols)
        self.extrac_data_list = []
        for i in range(size_of_cols):
            list_data = self.data_frame[self.usecols[i]]
            self.extrac_data_list.append(list_data.to_list())

    def get_data_list(self):
        return self.extrac_data_list

    def get_xtick_positions(self, num_of_data_types=None):
        xtick_positions = []
        if num_of_data_types % 2 == 0:
            print("Even number of items per xtick")

            d = 2
            for i in range(0, num_of_data_types):
                xtick_positions.append(num_of_data_types - d * i)

        else:
            print("Odd number of items per tick")
            d = 2
            for i in range(0, num_of_data_types):
                xtick_positions.append(num_of_data_types - d * i)

        xtick_positions.reverse()

        return xtick_positions

    def get_y_max(self):
        if self.extrac_data_list is None:
            raise Exception("Data not populated")
        y_maxes = []
        for data in self.extrac_data_list:
            y_maxes.append(np.max(data))
        return max(y_maxes)

    def get_y_min(self):
        if self.extrac_data_list is None:
            raise Exception("Data not populated")
        y_mins = []
        for data in self.extrac_data_list:
            y_mins.append(np.min(data))
        return min(y_mins)

    def plot(self, datasets=None, labels=None, hatches=None,
             colors=None,
             xlabel=None, ylabel=None, xticks=None,
             title=None, xlabelfontsize=12, xlabelfontweight='medium',
             ylabelfontsize=12, ylabelfontweight='medium',
             yticksfontsize=12, yticksfontweight='medium',
             xticksfontsize=12, xticksfontweight='medium',
             titlefontsize=12,
             titlefontweight='bold',
             xtick_positions=None,
             legendfontweight='bold', legendfontsize=16,
             y_max=None,
             fig_size=(24, 12)):
        # BLAS
        x = np.arange(len(xticks))
        print(x)
        fig, ax = plt.subplots(figsize=fig_size)
        # ax.set_yscale('log')
        count = 0

        for dataset, label, hatch, color, xtick_pos in zip(datasets, labels, hatches, colors,
                                                           xtick_positions):
            y = dataset

            # the label locations
            width = 0.16  # the width of the bars

            count = count + 1
            rects1 = ax.bar(x + width / 2 * xtick_pos, y, width=width,
                            label=label, alpha=0.5, color=color, hatch=hatch)

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel(ylabel, fontsize=ylabelfontsize, fontweight=ylabelfontweight)
        ax.set_xlabel(xlabel, fontsize=xlabelfontsize, fontweight=xlabelfontweight)
        ax.set_title(title)
        ax.set_xticks(x)
        # ax.set_yticks(men_means)
        # ax.yaxis.set_tick_params(labelsize=10)
        ax.set_xticklabels(xticks, fontsize=xticksfontsize, fontweight=xticksfontweight)
        # y_max = np.ceil(y_max)
        # print(y_max)
        # ax.set_yticklabels(np.linspace(0.0, y_max, num=2*y_max+1), fontsize=yticksfontsize, fontweight=yticksfontweight)

        ax.legend(prop={'size': legendfontsize, 'weight': legendfontweight})

        fig.tight_layout()

        plt.show()
