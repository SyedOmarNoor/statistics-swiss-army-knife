import tkinter as tk
import tkinter.ttk as ttk
from stat_defs import *

class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.clicksum = 0

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
            "maj_out",
            "summary"
            ]
        labellist = [
            "Sorted list/set",
            "Number count",
            "Sum of numbers",
            "Mean",
            "Range",
            "Median",
            "Mode(s)",
            "Maximum (Q4)",
            "Minimum (Q0)",
            "Quartile 1",
            "Quartile 2",
            "Quartile 3",
            "IQR",
            "Stand. deviation (Σ)",
            "Stand. deviation (σ)",
            "Minor outlier",
            "Major outlier",
            "5-point summary"
            ]

        for labels in self.labelvarlist:
            exec(f"self.{labels}label = tk.Label(self, text = '{labellist[self.labelvarlist.index(labels)]}: ').grid(row = {self.labelvarlist.index(labels)+2}, column = 0, sticky = 'e')")

        for labels in self.labelvarlist:
            exec(f"self.{labels}result = tk.Label(self, text = '0')\nself.{labels}result.grid(row={self.labelvarlist.index(labels) + 2}, column = 1, sticky = 'w')")

        tickboxframe = tk.Frame(self)
        
        tk.Label(tickboxframe, text = "Options:").grid(row=0, column=0)
        
        self.entrylabel = tk.Label(self, text = "Enter list of numbers (separate with commas or spaces):").grid(row = 0, column = 0)

        checkboxlabels = [
            "List info",
            "Common 4",
            "Max/Min",
            "Quartile",
            "Deviation",
            "Outliers",
            "Summary"
            ]
        for label in range(1, len(checkboxlabels)+1):
            exec(f"self.var{label} = tk.IntVar(value=1)\ntk.Checkbutton(tickboxframe, text='{checkboxlabels[label-1]}', variable=self.var{label}).grid(row=0, column = {label}, sticky='w')")
        
        self.listentry = tk.Entry(self, width = 46)
        self.listentry.grid(row = 0, column = 1, sticky = 'w')
        
        tickboxframe.grid(row=1, columnspan = 2, column = 0, sticky = 'w')
        

        self.listentry.bind('<Key>', self.calculate)
        self.listentry.bind('<KeyRelease>', self.calculate)


    def calculate(self, event=0):
        try:
            alldict = allfunctions(self.listentry.get())
            for labels in self.labelvarlist:
                exec(f"self.{labels}result['text'] = alldict['{labels}']")
        except ZeroDivisionError:
            return
root = tk.Tk()
app = Application(master=root)
app.mainloop()
