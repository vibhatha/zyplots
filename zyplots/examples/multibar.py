import numpy as np

from zyplots.data.DataLoader import DataLoader
from zyplots.core.GraphProcessor import GraphProcessor
from zyplots.util.DataUtil import DataUtil

labels = ['Seq1(Cuda:0)', 'Copy(Cuda:0 -> Cuda:1)', 'Seq2(Cuda:1)', 'FC(Cuda:1)']
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

dtype = {"split_id": int, "seq1_time": float, "c0_c1_copy_time": float, "seq2_time": float, "seq_fc_time": float}
usecols = ['split_id', 'seq1_time', 'c0_c1_copy_time', 'seq2_time', 'seq_fc_time']
datacols = ['seq1_time', 'c0_c1_copy_time', 'seq2_time', 'seq_fc_time']
index_col = False

data_dir_120 = "/home/vibhatha/github/TimelineGraphTool/data/resnet/resnet_split120_timeline_withheaders.csv"
records_120 = 120
filter_120 = [0, 1, 2, 5, 40, 41, 42, 57, 58, 59, 87, 88, 89, 117, 118, 119]

data_dir_60 = "/home/vibhatha/github/TimelineGraphTool/data/resnet/resnet_split60_timeline_withheader.csv"
records_60 = 60
filter_60 = [0, 1, 2, 5, 27, 28, 29, 57, 58, 59]

data_dir_40 = "/home/vibhatha/github/TimelineGraphTool/data/resnet/resnet_split40_timeline_withheaders.csv"
records_40 = 40
filter_40 = [0, 1, 2, 5, 15, 16, 17, 37, 38, 39]

data_dir_30 = "/home/vibhatha/github/TimelineGraphTool/data/resnet/resnet_split30_timeline_withheaders.csv"
records_30 = 30
filter_30 = [0, 1, 2, 5, 15, 16, 17, 27, 28, 29]

data_dir_24 = "/home/vibhatha/github/TimelineGraphTool/data/resnet/resnet_split24_timeline_withheaders.csv"
records_24 = 24
filter_24 = [0, 1, 2, 5, 12, 13, 14, 22, 23]

data_dir_20 = "/home/vibhatha/github/TimelineGraphTool/data/resnet/resnet_split20_timeline_withheaders.csv"
records_20 = 20
filter_20 = [0, 1, 2, 7, 8, 9, 17, 18, 19]

data_dir_15 = "/home/vibhatha/github/TimelineGraphTool/data/resnet/resnet_split15_timeline_withheaders.csv"
records_15 = 15
filter_15 = [0, 1, 2, 6, 7, 8, 12, 13, 14]

data_dir_12 = "/home/vibhatha/github/TimelineGraphTool/data/resnet/resnet_split12_timeline_withheaders.csv"
records_12 = 12
filter_12 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

data_dir_10 = "/home/vibhatha/github/TimelineGraphTool/data/resnet/resnet_split10_timeline_withheaders.csv"
records_10 = 10
filter_10 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

data_dir_8 = "/home/vibhatha/github/TimelineGraphTool/data/resnet/resnet_split8_timeline_withheaders.csv"
records_8 = 8
filter_8 = [0, 1, 2, 3, 4, 5, 6, 7]

data_dir_6 = "/home/vibhatha/github/TimelineGraphTool/data/resnet/resnet_split6_timeline_withheaders.csv"
records_6 = 6
filter_6 = [0, 1, 2, 3, 4, 5]

data_dir_list = [data_dir_120, data_dir_60, data_dir_40, data_dir_30, data_dir_24, data_dir_20, data_dir_15,
                 data_dir_12, data_dir_10, data_dir_8, data_dir_6]
record_list = [records_120, records_60, records_40, records_30, records_24, records_20, records_15, records_12,
               records_10, records_8, records_6]
filter_list = [filter_120, filter_60, filter_40, filter_30, filter_24, filter_20, filter_15, filter_12, filter_10,
               filter_8, filter_6]

# id = 0
# data_dir_list = [data_dir_list[id]]
# record_list = [record_list[id]]
# filter_list = [filter_list[id]]

for data_dir, record, filter in zip(data_dir_list, record_list, filter_list):
    data_loader = DataLoader(file_path=data_dir)

    pdf = data_loader.read_as_pandas()

    npy = data_loader.read_as_numpy()

    skiprows = DataUtil.get_skiprows(filter=filter, records=record)

    dataframe = data_loader.read_as_pandas_from_columns(columns=usecols, data_types=dtype, filter=skiprows)

    gp = GraphProcessor(dataframe=dataframe, cols=datacols)

    data_list = gp.get_data_list()

    num_of_data_types = len(data_list)

    xtick_positions = gp.get_xtick_positions(num_of_data_types=num_of_data_types)
    y_max = gp.get_y_max()
    y_min = gp.get_y_min()

    gp.plot(datasets=data_list, labels=labels, hatches=hatches, colors=colors,
            xlabel=xlabel, ylabel=ylabel, xticks=filter,
            title="Resnet50 Split "+str(record), xtick_positions=xtick_positions, width=0.20,
            y_max=y_max, save=True, show=False, save_file="resnet50_split_"+str(record)+".png")

    seq1 = pdf[usecols[1]]
    cp = pdf[usecols[2]]
    seq2 = pdf[usecols[3]]
    fc = pdf[usecols[4]]
    new_pdf = pdf.sum()
    print(seq1.sum() + cp.sum() + seq2.sum() + fc.sum())
