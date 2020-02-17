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
            #print("Even number of items per xtick")

            d = 2
            for i in range(0, num_of_data_types):
                xtick_positions.append(num_of_data_types - d * i)

        else:
            #print("Odd number of items per tick")
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
             title=None, xlabelfontsize=26, xlabelfontweight='medium',
             ylabelfontsize=26, ylabelfontweight='medium',
             yticksfontsize=26, yticksfontweight='medium',
             xticksfontsize=26, xticksfontweight='medium',
             titlefontsize=28,
             titlefontweight='bold',
             xtick_positions=None,
             legendfontweight='medium', legendfontsize=22,
             y_max=None,
             fig_size=(24, 14),
             width=0.25,
             alpha=0.5,
             save=False,
             save_file='',
             show=True):

        plt.rc('xtick', labelsize=xticksfontsize)
        plt.rc('ytick', labelsize=yticksfontsize)
        plt.rc('axes', labelsize=xlabelfontsize)  # , labelweight='bold')
        plt.rc('legend', fontsize=legendfontsize)
        x = np.arange(len(xticks))
        fig, ax = plt.subplots(figsize=fig_size)
        # ax.set_yscale('log')
        count = 0

        for dataset, label, hatch, color, xtick_pos in zip(datasets, labels, hatches, colors,
                                                           xtick_positions):
            y = dataset
            count = count + 1
            rects1 = ax.bar(x + width / 2 * xtick_pos, y, width=width,
                            label=label, alpha=alpha, color=color, hatch=hatch)


        ax.set_ylabel(ylabel, fontsize=ylabelfontsize, fontweight=ylabelfontweight)
        ax.set_xlabel(xlabel, fontsize=xlabelfontsize, fontweight=xlabelfontweight)
        ax.set_title(title, fontsize=titlefontsize, fontweight=titlefontweight)
        ax.set_xticks(x)
        ax.set_xticklabels(xticks, fontsize=xticksfontsize, fontweight=xticksfontweight)

        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.07),
                  fancybox=True, shadow=True, ncol=5, prop={'size': legendfontsize, 'weight': legendfontweight})
        #ax.legend()

        fig.tight_layout()
        if save:
            plt.savefig(save_file)
        if show:
            plt.show()
        plt.close()
