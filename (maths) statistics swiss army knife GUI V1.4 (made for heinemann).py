import tkinter as tk
import tkinter.ttk as ttk
from stat_defs import *

class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.calcbuf = None

    def create_widgets(self):
        self.master.title("Statistics Swiss Army Knife GUI")

        self.labelvarlist = [
            "sorted",
            "count",
            "sum",
            "mean",
            "range",
            "median",
            "mode",
            "max",
            "min",
            "q1",
            "q2",
            "q3",
            "iqr",
            "pop_dev",
            "samp_dev",
            "min_out",
            "summary",
            "expected",
            "exsquared",
            "variance",
            ]
        self.labeldict = {  # function name, label, frame
            'sorted':   ['Sorted list/set',         "List info"], 
            'count':    ['Number count',            "List info"], 
            'sum':      ['Sum of numbers',          "List info"], 
            'mean':     ['Mean',                    "Common 4"], 
            'range':    ['Range',                   "Common 4"], 
            'median':   ['Median',                  "Common 4"], 
            'mode':     ['Mode(s)',                 "Common 4"], 
            'max':      ['Maximum (Q4)',            "Max/Min"], 
            'min':      ['Minimum (Q0)',            "Max/Min"], 
            'q1':       ['Quartile 1',              "Quartile"], 
            'q2':       ['Quartile 2',              "Quartile"], 
            'q3':       ['Quartile 3',              "Quartile"], 
            'iqr':      ['InterQuartile Range',     "Quartile"], 
            'pop_dev':  ['Stand. deviation (σ,pop)',"Deviation"], 
            'samp_dev': ['Stand. deviation (s,smp)',"Deviation"], 
            'min_out':  ['Outlier',           "Outlier"], 
            'summary':  ['5-point summary',         "Summary"], 
            'expected':  ['E(x)',         "Discrete"], 
            'exsquared':  ['E(x^2)',         "Discrete"], 
            'variance':  ['Variance',         "Discrete"], 
        }

        #print(self.labeldict) # list all fields, their label and their category

        tickboxframe = tk.Frame(self)
        
        tk.Label(tickboxframe, text = "Options:").grid(row=0, column=0)
        
        self.checkboxlabels = [
            "List info",
            "Common 4",
            "Max/Min",
            "Quartile",
            "Deviation",
            "Outlier",
            "Summary",
            "Discrete",
            ]
        for label in range(len(self.checkboxlabels)):  # create the checkboxes
            label += 1
            exec(
                f"""
self.varcheck{label} = tk.IntVar(value=1)
tk.Checkbutton(tickboxframe, text='{self.checkboxlabels[label-1]}', variable=self.varcheck{label}, command=self.checkboxupdate).grid(row=0, column = {label}, sticky='w')
"""  # can't indent multi-line strings when exec because it's say "unexpected indent"
                )
        
        tickboxframe.grid(row=1, columnspan = 2, column = 0, sticky = 'w')

        for func, info in self.labeldict.items():  # labels for values
            exec(
                f"""
self.{func}label = tk.Label(self, text = '{info[0]}: ')
self.{func}label.grid(row = {self.labelvarlist.index(func)+2}, column = 0, sticky = 'e')
"""
                )

        for func, info in self.labeldict.items():  # values of statistics of list
            exec(
                f"""
self.{func}result = tk.Label(self, text = '0')
self.{func}result.grid(row={self.labelvarlist.index(func) + 2}, column = 1, sticky = 'w')
"""
                )
        self.entrylabel = tk.Label(self, text = "Enter list of numbers (separate with commas or spaces):").grid(row = 0, column = 0)

        self.listentry = tk.Entry(self, width = 46)  # a decent width, doesn't adjust itself tho
        self.listentry.grid(row = 0, column = 1, sticky = 'w')
        

        self.listentry.bind('<Key>', self.calculate)  # calculate when key pressed
        self.listentry.bind('<KeyRelease>', self.calculate)  # calculate when key released, just in case

    def checkboxupdate(self):
        for index, label in enumerate(self.checkboxlabels):
            index += 1
            if eval(f"self.varcheck{index}.get()"):
                for func, items in self.labeldict.items():
                    if items[1] == label:
                        exec(f"self.{func}label.grid()")
                        exec(f"self.{func}result.grid()")
            else:
                for func, items in self.labeldict.items():
                    if items[1] == label:
                        exec(f"self.{func}label.grid_remove()")
                        exec(f"self.{func}result.grid_remove()")

    def calculate(self, event=0):
        try:
            if self.calcbuf == listify(self.listentry.get()):
                return
            alldict = allfunctions(self.listentry.get())
            for labels in self.labelvarlist:
                exec(f"self.{labels}result['text'] = alldict['{labels}']")
            self.calcbuf = listify(self.listentry.get())
        except (ZeroDivisionError, IndexError):  # except no values i.e. list length is 0, or if only 1 value
            pass
root = tk.Tk()
app = Application(master=root)
app.mainloop()
