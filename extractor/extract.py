import pandas as pd
import os
from datetime import datetime


class Extract:
    TODAY = datetime.today().date()

    def __init__(self, file_list):
        self.file_list = file_list
        self.frame = pd.DataFrame()
        self.frames = []
        self.extract_frames = []
        self.path = []

    def extract_headers(self):
        for file in self.file_list:
            self.frame = pd.read_csv(file, delimiter=r"\s+")
            self.frames.append(self.frame)
        return self.frame.columns

    def extract_data(self, headers: list):
        for frame in self.frames:
            self.frame = frame.get(headers)
            self.extract_frames.append(self.frame)

    def save_data(self):
        out = pd.concat(self.extract_frames)
        out.to_csv(
            os.path.join(
                os.path.dirname(self.file_list[0].name),
                f"extracted_output_{self.TODAY}.csv",
            )
        )
