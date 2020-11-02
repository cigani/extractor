from tkinter import *

from aihelper import Browse, OkButton, EntryBar, Popup, CheckBar

from aiextractor import Pipero





class Aiex:
    def __init__(self):
        self.data = None
        self.headers = None
        self.root = Tk()
        self.files = None
        self.listbox = Listbox
        self.button = None
        self.checkbox = None
        self.index = IntVar

    def looper(self):
        self.files = Browse(self.root, type="file", title="Select your files")
        self.entrybar = EntryBar(self.root, picks=['Delimiter', 'Start Row'])
        self.button = OkButton(parent=self.root, function=self.listboxer)
        self.checkbox = CheckBar(self.root, picks=['Remove The Index?'])
        self.checkbox.pack()
        self.root.mainloop()

    def load_data(self, delimiter, start_row):
        self.data = Pipero(self.files.get(), delimiter=delimiter, start_row=start_row, index=list(self.checkbox.state()))
        self.headers = self.data.get_headers()

    def listboxer(self):
        try:
            delimiter = list(self.entrybar.get('Delimiter'))[0]
        except IndexError:
            delimiter = None
        try:
            start_row = list(self.entrybar.get('Start Row'))[0]
        except IndexError:
            start_row = None

        self.load_data(delimiter, start_row)
        new_window = Toplevel(self.root)
        new_window.grab_set()
        self.listbox = Listbox(
            master=new_window,
            selectmode=MULTIPLE,
            width=max(map(lambda x: len(x), self.headers)) + 5,
            height=len(self.headers),
        )
        self.listbox.pack(expand=TRUE, fill=BOTH)
        for i in self.headers:
            self.listbox.insert(END, str(i))
        self.listbox.bind("<Double-Button-1>", True)
        OkButton(new_window, function=lambda: self.close(new_window))

    def close(self, window):
        items = [self.headers[int(item)] for item in self.listbox.curselection()]
        self.data.extract_data(items)
        self.data.save_data()
        if self.data.errors:
            for error in self.data.errors:
                Popup(self.root, error)
        window.destroy()


if __name__ == "__main__":
    Aiex().looper()
