import numpy as np
import pandas as pd

from zyplots.data.DataLoader import DataLoader
from zyplots.core.GraphProcessor import GraphProcessor
from zyplots.util.DataUtil import DataUtil

dtype = {"split_id": int, "seq1_time": float, "c0_c1_copy_time": float, "seq2_time": float, "seq_fc_time": float}
usecols = ['split_id', 'seq1_time', 'c0_c1_copy_time', 'seq2_time', 'seq_fc_time']
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

def atomic_analytics():
    for data_dir, record, filter in zip(data_dir_list, record_list, filter_list):
        data_loader = DataLoader(file_path=data_dir)

        pdf = data_loader.read_as_pandas()

        seq1 = pdf[usecols[1]]
        cp = pdf[usecols[2]]
        seq2 = pdf[usecols[3]]
        fc = pdf[usecols[4]]
        new_pdf = pdf.sum()
        print(seq1.sum() + cp.sum() + seq2.sum() + fc.sum())


def summary_analytics():
    dtype = {"split_id": int, "forward_time": float, "copy_time": float, "backward_time": float,
             "optimization_time": float}
    usecols = ['split_id', 'forward_time', 'copy_time', 'backward_time', 'optimization_time']
    data_file = "/home/vibhatha/github/TimelineGraphTool/data/summary/resnet/summary_v1.csv"
    pdf = pd.read_csv(data_file, usecols=usecols, dtype=dtype)
    #print(pdf.columns)
    #print(pdf.head())
    group_pdf = pdf.groupby(['split_id'])
    mean_pdf = group_pdf.mean()

    sum_pdf = mean_pdf.sum(axis=1)
    print(mean_pdf)
    print(sum_pdf)
    mean_pdf['total_time'] = sum_pdf

    print(mean_pdf)


summary_analytics()
