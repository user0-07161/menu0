#!/usr/bin/python
import tkinter as tk
from tkinter import ttk, simpledialog, filedialog
import os 
import json
import subprocess
from functools import partial

def main():
    root = tk.Tk()
    root.geometry("182x499")
    root.title("menu0")
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.pack(fill="both", expand=True)
    homedir = os.getenv("HOME")
    apps = {}
    #root.configure(background='black')

    if not os.path.isfile(f"{homedir}/.menu0.json"):
        with open(f"{homedir}/.menu0.json", 'w') as conf:
            json.dump(apps, conf)
    else:
        with open(f"{homedir}/.menu0.json", 'r') as conf:
            try:
                apps = json.load(conf)
            except:
                apps = {}


    def runApp(appl):
        subprocess.Popen(appl.split(" "))
    def addApp():
        name = simpledialog.askstring("Application name", "What's the application's name?", parent=root)
        dir = filedialog.askopenfilename(parent=root, initialdir="/", title="Please select the program", filetypes=[('All files', '*')])
        print(dir)
        if name:
            apps[name] = dir
            with open(f"{homedir}/.menu0.json", 'w') as conf:
                json.dump(apps, conf)
            root.destroy()
            main()
            
    def remConf():
        with open(f"{homedir}/.menu0.json", 'w') as conf:
            json.dump({}, conf)
        root.destroy()
        main()

    def createButtons():
        for app in apps:
            button = tk.Button(root, text=app, width=20, height=1, command=lambda appl=apps[app]: runApp(appl), padx=10, pady=10)
            button["border"] = 2
            button.pack(fill="both", expand=True) 
            print(apps)

        button = tk.Button(root, text="Add app", width=20, height=1, command=addApp, padx=10, pady=10)
        button["border"] = 2
        button.pack(fill="both", expand=True)
        button2 = tk.Button(root, text="Reset config", width=20, height=1, command=remConf, padx=10, pady=10, border=2)
        button2.pack(fill="both", expand=True)
        
    createButtons()
    root.mainloop()

main()
