import tkinter as tk
import ttkbootstrap as ttk
import datetime as dt
import app


# window
root = tk.Tk()
root.geometry("600x400")
root.title("To-Do")

# app GUI object
task_app = app.App(root)
task_app.pack(side="top", fill="both", expand=True)

def on_closing() -> None:
    task_app.on_close()
    root.destroy()

def main():
    # handle close event
    root.protocol("WM_DELETE_WINDOW", on_closing)

    # run GUI
    root.mainloop()

if __name__ == '__main__':
    main()