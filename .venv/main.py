import tkinter as tk
import ttkbootstrap as ttk
import datetime as dt
import app


def main():
    # window
    root = tk.Tk()
    root.geometry("600x400")
    root.title("To-Do")

    # app GUI object
    task_app = app.App(root)
    task_app.pack(side="top", fill="both", expand=True)

    # run GUI
    root.mainloop()

if __name__ == '__main__':
    main()