from aiextractor import __version__
from aiextractor.extract import Pipero


def test_delimiter(mdata):
    comma = Pipero(file_list=mdata['comma'], delimiter=',')
    space = Pipero(file_list=mdata['space'], delimiter=' ')
    none = Pipero(file_list=mdata['space'], delimiter=None)
    semi = Pipero(file_list=mdata['semi'], delimiter=';')
    assert comma.delimiter == ','
    assert space.delimiter == r"\s+"
    assert none.delimiter == r"\s+"
    assert semi.delimiter == ';'

def test_start_row(mdata):
    start = [10, 999, 0, 1]
    for row in start:
        start_10 = Pipero(file_list=mdata['comma'], delimiter=',', start_row=row)
        start_10.extract_headers()
        ten = [len(x.index) for x in start_10.frames]
        assert all([x == 1000-row for x in ten])

def test_extract_headers(mdata):
    assert False


def test_extract_data(mdata):
    assert False


def test_save_data(mdata):
    assert False
