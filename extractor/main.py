from tkinter import filedialog, simpledialog, Listbox
from tkinter import *
from extractor.extract import Extract

root = Tk()
root.filename = filedialog.askopenfiles(initialdir="/", title="Select files")
data = Extract(root.filename)
headers = data.extract_headers()
listbox = Listbox(selectmode=MULTIPLE)
listbox.pack()
for i in headers:
    listbox.insert(END, "Option " + str(i))
listbox.bind("<Double-Button-1>", True)


def close():
    global listbox, root, headers
    items = items = listbox.curselection()
    items = [headers[int(item)] for item in items]
    data.extract_data(items)
    data.save_data()
    root.destroy()


b = Button(root, text="OK", command=close).pack()

root.mainloop()
