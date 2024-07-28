import tkinter
import tkinter.font as tkFont
import ttkbootstrap as ttk


class Task:
    def __init__(self, master, text="", font="", status= False) -> None:
        self.font : str = font
        self.task_frame = ttk.Frame(master=master)
        self.task_label = ttk.Label(master=self.task_frame, text=text, font=font)
        self.task_check_box = ttk.Checkbutton(master=self.task_frame, command=self.check_task)
        self.task_check_box.configure(bootstyle="light")
        # unchecking button by default
        self.task_check_box.state(['!alternate'])
        self.task_status : bool = status

        if self.task_status:
            self.set_task_label_checked()
            self.task_check_box.state(['selected'])

        self.task_title : str = text

    def pack(self, padx=0, pady=0) -> None:
        self.task_check_box.pack(side="left")
        self.task_label.pack(side="left")
        self.task_frame.pack(side="top", fill="both")


    def check_task(self) -> None:
        self.task_status = not self.task_status
        if(self.task_status):
            self.set_task_label_checked()
        else:
            normal_font = tkFont.Font(family="Calibri", size=18, overstrike=0)
            self.task_label.configure(font=normal_font)

    def set_task_label_checked(self):
        strikethrough_font = tkFont.Font(family="Calibri", size=18, overstrike=1)
        self.task_label.configure(font=strikethrough_font)