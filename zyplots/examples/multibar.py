import numpy as np

from zyplots.data.DataLoader import DataLoader
from zyplots.core.GraphProcessor import GraphProcessor

data_dir = "/home/vibhatha/github/TimelineGraphTool/data/resnet/resnet_split60_timeline_withheader.csv"

data_loader = DataLoader(file_path=data_dir)

pdf = data_loader.read_as_pandas()

npy = data_loader.read_as_numpy()

print(pdf.columns)
print(npy.shape)

dtype = {"split_id": int, "seq1_time": float, "c0_c1_copy_time": float, "seq2_time": float, "seq_fc_time": float}
usecols = ['split_id', 'seq1_time', 'c0_c1_copy_time', 'seq2_time', 'seq_fc_time']
datacols = ['seq1_time', 'c0_c1_copy_time', 'seq2_time', 'seq_fc_time']
index_col = False

dataframe = data_loader.read_as_pandas_from_columns(columns=usecols, data_types=dtype)

gp = GraphProcessor(dataframe=dataframe, cols=datacols)

# print(dataframe.head())

# local_data_java_datasets = [avg_times_ijcnn1_local_blas, avg_times_ijcnn1_local_no_blas,
#                             avg_times_webspam_local_blas, avg_times_webspam_local_no_blas,
#                             avg_times_epsilon_local_blas, avg_times_epsilon_local_no_blas]
# local_error_java_datasets = [error_times_ijcnn1_local_blas, error_times_ijcnn1_local_no_blas,
#                              error_times_webspam_local_blas, error_times_webspam_local_no_blas,
#                              error_times_epsilon_local_blas, error_times_ijcnn1_local_no_blas]
labels = ['Seq1', 'Copy', 'Seq2', 'FC']
colors = ['green', 'blue', 'orange', 'cyan']
hatches = ['xx', '###', '---', '+']
ecolors = ['red', 'red', 'red', 'red']
xlabel = 'Split Sub Id'
ylabel = 'Time(s)'
title = ''
default_font_size = 44
xlabelfontsize = default_font_size
xlabelfontweight = 'bold'
ylabelfontsize = default_font_size
ylabelfontweight = 'bold'
yticksfontsize = default_font_size
yticksfontweight = 'bold'
xticksfontsize = default_font_size
xticksfontweight = 'bold'
titlefontsize = default_font_size
titlefontweight = 'bold'
legendfontsize = 28
legendfontweight = 'bold'

width = 1

data_list = gp.get_data_list()

num_of_data_types = len(data_list)
print(len(data_list))

xtick_positions = gp.get_xtick_positions(num_of_data_types=num_of_data_types)
print(xtick_positions, len(data_list), len(data_list[0]))
y_max = gp.get_y_max()
y_min = gp.get_y_min()
# y_max = 1000000
# y_min = 0.001
# print("Ymax,Ymin", y_max, y_min)

print(y_min, y_max)

gp.plot(datasets=data_list, labels=labels, hatches=hatches, colors=colors,
                                                  xlabel=xlabel, ylabel=ylabel, xticks=np.arange(60).tolist(),
                                                  title=title, xlabelfontsize=xlabelfontsize,
                                                  xlabelfontweight=xlabelfontweight,
                                                  ylabelfontsize=ylabelfontsize, ylabelfontweight=ylabelfontweight,
                                                  yticksfontsize=yticksfontsize, yticksfontweight=yticksfontweight,
                                                  xticksfontsize=xticksfontsize, xticksfontweight=xticksfontweight,
                                                  titlefontsize=titlefontsize,
                                                  titlefontweight=titlefontweight, xtick_positions=xtick_positions,
                                                  legendfontweight=legendfontweight,
                                                  legendfontsize=legendfontsize, y_max=y_max)
