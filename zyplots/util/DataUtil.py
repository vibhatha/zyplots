class DataUtil:

    @staticmethod
    def get_skiprows(filter=[], records=0):
        if records <= 0:
            raise Exception("Total records must be greater than 1")

        ids = range(records)
        skiprows = [e for e in ids if e not in filter]
        return skiprows
