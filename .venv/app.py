import task
import tkinter as tk
import ttkbootstrap as ttk

# style
HEADER_BG_COLOR : str = "#343a40"
HEADER_FG_COLOR : str = "#ffffff"

class App(ttk.Frame):

    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # app GUI
        # header frame
        self.header_frame = ttk.Frame(master=self)
        self.header_frame.configure(bootstyle="dark")
        self.header_frame.pack(side="top", fill="both")

        # welcome message (title)
        self.welcome_message = ttk.Label(master=self.header_frame, text="Hello User!", font="Calibri 24 bold", background=HEADER_BG_COLOR)
        self.welcome_message.configure(foreground=HEADER_FG_COLOR)
        self.welcome_message.pack(side="left", padx=10, pady=10)

        # body frame
        self.body_frame = ttk.Frame(master=self)
        self.body_frame.configure(bootstyle="secondary")
        self.body_frame.pack(side="top", fill="both", expand=True)

        # task button frame
        add_task_frame = ttk.Frame(master=self.body_frame)
        add_task_frame.configure(bootstyle="secondary")
        add_task_frame.pack(side="top", fill="both")

        # add task button
        self.add_task_button = ttk.Button(master=add_task_frame, text="Add task", command=self.add_task, state="disabled")
        self.add_task_button.pack(side="left", padx=20, pady=10)

        # task text input
        self.text_input = ttk.StringVar()
        self.text_input.trace_add('write', self.on_entry_changed)
        self.task_text_input = ttk.Entry(master=add_task_frame, textvariable=self.text_input)
        self.task_text_input.pack(side="top", pady=10)

        # tasks frame
        self.tasks_frame = ttk.Frame(master=self.body_frame)
        self.tasks_frame.configure(bootstyle="light")
        self.tasks_frame.pack(side="top", fill="both")

        # tasks list
        self.tasks_list : List[task.Task] = []

    def add_task(self) -> None:
        task_title = self.text_input.get()
        new_task = task.Task(master=self.tasks_frame, text=task_title)
        new_task.pack()
        self.tasks_list.append(new_task)
        self.reset_entry()


    def on_entry_changed(self, var, index, mode) -> None:
        if len(self.text_input.get()) == 0:
            self.add_task_button.configure(state="disabled")
        else:
            self.add_task_button.configure(state="active")

    def reset_entry(self) -> None:
        self.task_text_input.delete(0, "end")