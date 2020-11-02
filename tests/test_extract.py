from aiextractor.extract import Pipero
import os
import os

from pandas import read_csv, Index

from aiextractor.extract import Pipero


def test_delimiter(mdata):
    k = list(mdata.keys())[0]
    test = Pipero(file_list=mdata[k], delimiter=k)
    if k == ' ':
        k = r"\s+"
    assert test.delimiter == k


def test_start_row(mdata):
    k = list(mdata.keys())[0]

    start = [10, 999, 0, 1, '15', 10.5]
    for row in start:
        test = Pipero(file_list=mdata[k], delimiter=k, start_row=row)
        test.load_data()
        ten = [len(x.index) for x in test.frames]
        assert all([x == 1000 - int(row) for x in ten])


def test_extract_headers(mdata):
    k = list(mdata.keys())[0]
    test = Pipero(file_list=mdata[k], delimiter=k)
    assert (all(test.get_headers() == ['a', 'b', 'c']))
    assert (all(test.get_headers() == ['a', 'b', 'c']))


def test_extract_data(mdata):
    k = list(mdata.keys())[0]
    test = Pipero(file_list=mdata[k], delimiter=k)
    test.load_data()
    columns = [df.columns for df in test.extract_frames]
    rows = [len(df.index) for df in test.extract_frames]
    assert all([x == 1000 for x in rows])
    assert all([all(y == ['a', 'b', 'c']) for y in columns])
    test.extract_data(['a'])
    columns = [df.columns for df in test.extract_frames]
    rows = [len(df.index) for df in test.extract_frames]
    assert all([x == 1000 for x in rows])
    assert all([y == ['a'] for y in columns])



def test_save_data(mdata, tmpdir):
    k = list(mdata.keys())[0]
    buffered_read = [open(x, mode='rb') for x in mdata[k]]
    for data in [mdata[k], buffered_read]:
        test = Pipero(file_list=data, delimiter=k)
        test.save_data()
        new = list(set(os.listdir(os.path.dirname(mdata[k][0]))) - set(map(lambda x: os.path.split(x)[-1], mdata[k])))[0]
        path_to_extracted = os.path.join(os.path.dirname(mdata[k][0]), new)
        df = read_csv(path_to_extracted, sep=',')
        base_columns = list(map(lambda x: os.path.splitext(os.path.split(x)[-1])[0], mdata[k]))
        assert all(df.columns.intersection(base_columns) == Index(base_columns))
        os.remove(os.path.join(os.path.dirname(mdata[k][0]), new))
