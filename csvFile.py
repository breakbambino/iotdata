from tkinter import filedialog
from tkinter import *

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
import csv
with open(root.filename) as csvfile:
    rer=csv.DictReader(csvfile)
    for i in rer:
            print(i)


            
