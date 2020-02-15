import numpy as np

from zyplots.data.DataLoader import DataLoader
from zyplots.core.GraphProcessor import GraphProcessor
from zyplots.util.DataUtil import DataUtil

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

records = 60
skiprows = DataUtil.get_skiprows(filter=[0, 1, 2, 5, 15, 16, 17, 43, 44, 45, 57, 58, 59], records=records)

print(skiprows)

dataframe = data_loader.read_as_pandas_from_columns(columns=usecols, data_types=dtype, filter=skiprows)

print(dataframe.shape)

gp = GraphProcessor(dataframe=dataframe, cols=datacols)

labels = ['Seq1', 'Copy', 'Seq2', 'FC']
colors = ['green', 'blue', 'orange', 'cyan']
hatches = ['xx', '###', '---', '+']
ecolors = ['red', 'red', 'red', 'red']
xlabel = 'Split Sub Id'
ylabel = 'Time(s)'
title = ''
default_font_size = 14
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
legendfontsize = 14
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

# print(y_min, y_max)

gp.plot(datasets=data_list, labels=labels, hatches=hatches, colors=colors,
        xlabel=xlabel, ylabel=ylabel, xticks=np.arange(13).tolist(),
        title=title, xtick_positions=xtick_positions,
        y_max=y_max)

seq1 = pdf[usecols[1]]
cp = pdf[usecols[2]]
seq2 = pdf[usecols[3]]
fc = pdf[usecols[4]]
new_pdf = pdf.sum()

print(seq1.sum() + cp.sum() + seq2.sum() + fc.sum())
