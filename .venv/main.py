import tkinter as tk
import ttkbootstrap as ttk
import datetime as dt
import app
import platform


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

def check_mac_os() -> bool:
    os = platform.platform(terse=True)
    if os.find("macOS") == -1:
        return False
    else:
        return True

def main():
    # handle close event
    root.protocol("WM_DELETE_WINDOW", on_closing)

    # check if app is running on macOS system
    if check_mac_os():
        root.createcommand("::tk::mac::Quit", on_closing)

    # run GUI
    root.mainloop()

if __name__ == '__main__':
    main()