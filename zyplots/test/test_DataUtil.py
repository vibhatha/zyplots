from unittest import TestCase
from zyplots.util.DataUtil import DataUtil


class TestDataUtil(TestCase):

    def test_get_skiprows(self):
        records = 10
        record_list = range(records)
        filter = [0, 5, 7]
        skiprows = DataUtil.get_skiprows(filter=filter, records=records)
        self.assertEqual(skiprows, [1,2,3,4,6,8,9])
