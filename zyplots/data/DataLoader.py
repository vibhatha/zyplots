import pandas as pd
import os


class DataLoader:

    def __init__(self, file_path):
        self.file_path = file_path

    def read_as_pandas(self, columns=[], data_types=[], filter=[]):
        data = None
        if not os.path.exists(self.file_path):
            raise Exception("{} not found".format(self.file_path))
        if not columns and not data_types:
            data = pd.read_csv(self.file_path, skiprows=filter)
        if columns and data_types:
            data = pd.read_csv(self.file_path, usecols=columns, dtype=data_types, skiprows=filter)
        return data

    def read_as_numpy(self):
        return self.read_as_pandas().to_numpy()

    def read_as_pandas_from_columns(self, columns=[], data_types=[], filter=[]):
        return self.read_as_pandas(columns=columns, data_types=data_types, filter=filter)



