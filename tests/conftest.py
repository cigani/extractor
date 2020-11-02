import os

import numpy as np
import pytest
from pandas import DataFrame

delims = [',', ' ', ';']


@pytest.fixture(name='mdata', scope='module', params=delims)
def generate_csv(tmpdir_factory, request):
    directory = tmpdir_factory.mktemp("csv")
    dd = {}
    columns = ['a', 'b', 'c']
    for x in ['1', '2', '3']:
        data = np.reshape(np.arange(0, len(columns) * 1000), [-1, len(columns)])
        df = DataFrame(columns=columns, data=data)
        out = os.path.join(directory, f'{x}_{request.param}.csv')
        if dd.get(request.param):
            dd[request.param].append(out)
        else:
            dd[request.param] = [out]
        df.to_csv(out, index=False, sep=request.param)
    return dd
