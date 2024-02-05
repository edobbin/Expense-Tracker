import tkinter as tk
from tkinter import ttk

class mainWindow():
    def __init__(self, ):
        super().__init__()
        self.title("Expense Tracker")
        self.geometry("400x300")
        label = tk.Label(self, text="Hello world")
        label.pack()

mainWindow(tk.Tk)