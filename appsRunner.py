import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

canvas = tk.Canvas(root, height=800, width=800)
canvas.pack()

frame = tk.Frame(root, bg="green")
frame.place(relwidth=1, relheight=1)


def addLabel(app):
    label = tk.Label(frame, text=app, bg="white")
    label.pack()

def addApp():
    fileName = filedialog.askopenfilename(initialdir="/", title="Select File", 
                                          filetypes=(("Executables", "*.exe"), ("All Files", "*.*")))
    apps.append(fileName)
    addLabel(fileName)
    
def runApps():
    for app in apps:
        os.startfile(app)


if os.path.isfile('apps.txt'):
    with open('apps.txt', 'r') as inputFile:
        tempApps = inputFile.read()
        apps = tempApps.split('\n')
        for app in apps:
            addLabel(app)

openFileButton = tk.Button(root, text="Open File", padx=10, pady=5, fg="green", 
                           bg="white", command=addApp)
openFileButton.pack()

runAppsButton = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="green", 
                          bg="white", command=runApps)
runAppsButton.pack()

root.mainloop()

with open('apps.txt', 'w') as outputFile:
    for app in apps[:-1]:
        outputFile.write(app + "\n")
    outputFile.write(apps[-1])