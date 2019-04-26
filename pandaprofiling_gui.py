# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 11:14:05 2019

@author: aj-nok

RUN THIS CODE IN IPYTHON CONSOLE ONLY. PANDAS PROFILING DOESN'T WORK IN SPYDER.

"""

import tkinter as tk
from tkinter.filedialog import askopenfilename
import pandas as pd
import pandas_profiling

def import_csv_data():
    global v
    csv_file_path = askopenfilename()
    #print(csv_file_path)
    v.set(csv_file_path)
    df = pd.read_csv(csv_file_path)
    st_pat=csv_file_path.rsplit('/', 1)[0]
    st_pat+='/profilingoutput.html'
    profile(df,st_pat)
    

def profile(df,st_pat):
    profile = pandas_profiling.ProfileReport(df)
    profile.to_file(outputfile=st_pat)
    print("YOUR PANDAS_PROFILING OUTPUT IS CREATED IN THE SAME PATH AS YOUR CSV..")
    
    
root = tk.Tk()
root.title("import csv file gui")
root.geometry("500x200")
root.configure(background="cyan")
tk.Label(root, text='IMPORT CSV FILE: ').grid(row=0, column=0 )
tk.Label(root, text='Type File Path').grid(row=2, column=1)
v = tk.StringVar()
entry = tk.Entry(root, textvariable=v,width=40).grid(row=2, column=2)
tk.Button(root, text='Browse Data Set',command=import_csv_data,bg="orange").grid(row=4, column=1)
tk.Button(root, text='Close',command=root.destroy,bg="orange").grid(row=4, column=2)
root.mainloop()
