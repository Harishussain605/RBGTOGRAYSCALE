import tkinter as tk # this is the preferred import for tkinter
from tkinter import filedialog

root = tk.Tk()
x = filedialog.askopenfilename()
print(x)
root.mainloop()