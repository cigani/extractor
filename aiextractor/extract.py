import pandas as pd
import os
from datetime import datetime


class Pipero:
    TODAY = datetime.today().date()

    def __init__(self, file_list, delimiter=None, start_row=None):
        self.file_list = file_list
        self.frame = pd.DataFrame()
        self.frames = []
        self.extract_frames = []
        self.path = []
        self.delimiter=delimiter
        self.start_row = start_row

    @property
    def delimiter(self):
        return self._delimiter

    @delimiter.setter
    def delimiter(self, value):
        if value:
            value = value.strip()
        if not value:
            value = r"\s+"
        else:
            value = value
        self._delimiter = value

    @property
    def start_row(self):
        return self._start_row

    @start_row.setter
    def start_row(self, value):
        if value:
            value = int(value)
        self._start_row = value


    def extract_headers(self):
        for file in self.file_list:
            self.frame = pd.read_csv(file, delimiter=self.delimiter, skiprows=self.start_row)
            self.frames.append(self.frame)
        return self.frame.columns

    def extract_data(self, headers: list):
        for frame in self.frames:
            self.frame = frame.get(headers)
            self.extract_frames.append(self.frame)

    def save_data(self):
        names = [os.path.splitext(os.path.split(x.name)[-1])[0] for x in self.file_list]
        frames = [x.rename_axis("Index").reset_index() for x in self.extract_frames]
        out = pd.concat(frames, axis=1, keys=names)

        out.to_csv(
            os.path.join(
                os.path.dirname(self.file_list[0].name),
                f"extracted_output_{self.TODAY}.csv",
            ),
            index=False,
        )

