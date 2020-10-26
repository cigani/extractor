import pytest
from aiextractor.extract import Pipero
from pandas import DataFrame
import numpy as np
import os

@pytest.fixture(name='mdata', scope='module')
def generate_csv(tmpdir_factory ):
    directory = tmpdir_factory .mktemp("csv")
    dd = {}
    for x in ['f1', 'f2', 'f3']:
        columns = ['a', 'b', 'c']
        data = np.reshape(np.arange(0, len(columns)*1000), [-1, len(columns)])
        df = DataFrame(columns=columns, data=data)

        for delim in [('comma',','), ('semi',';'), ('space', ' ')]:
            out = os.path.join(directory, f'{x}_{delim[0]}')
            if dd.get(delim[0]):
                dd[delim[0]].append(out)
            else:
                dd[delim[0]] = [out]
            df.to_csv(out, index=False, sep=delim[1])
    return dd



