import task
import tkinter as tk
import ttkbootstrap as ttk

# style
HEADER_BG_COLOR : str = "#343a40"
HEADER_FG_COLOR : str = "#ffffff"
SAVEFILE : str = "../save.txt"

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
        self.tasks_frame.pack(side="top", fill="both", padx=20, pady=20)

        # tasks list
        self.tasks_list : List[task.Task] = []

        self.load_tasks()

    def add_task(self) -> None:
        task_title = self.text_input.get()
        new_task = task.Task(master=self.tasks_frame, text=task_title)
        new_task.pack()
        self.tasks_list.append(new_task)
        self.reset_entry()

    def add_raw_task(self, text : str, status : bool):
        new_task = task.Task(master=self.tasks_frame, text=text, status=status)
        new_task.pack()
        self.tasks_list.append(new_task)

    def on_entry_changed(self, var, index, mode) -> None:
        if len(self.text_input.get()) == 0:
            self.add_task_button.configure(state="disabled")
        else:
            self.add_task_button.configure(state="active")

    def reset_entry(self) -> None:
        self.task_text_input.delete(0, "end")

    def on_close(self):
        self.save_tasks()
        self.destroy()

    def save_tasks(self):
        file = open(SAVEFILE, "w")
        for t in self.tasks_list:
            save_content = t.task_title + "|" + str(t.task_status) + "\n"
            file.write(save_content)
        file.close()

    def load_tasks(self):
        file = open(SAVEFILE, "r")
        while True:
            content = file.readline()

            if not content:
                break

            content_splitted = content.split("|")

            task_title = content_splitted[0]
            task_status_str = content_splitted[1]

            task_status = False
            if task_status_str == "True\n":
                task_status = True

            self.add_raw_task(task_title, task_status)

        file.close()