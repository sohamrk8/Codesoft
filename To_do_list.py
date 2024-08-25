from tkinter import *
from tkinter import messagebox
def newTask():
    task = my_entry.get()
    if task != " ":
        lb.insert(END, task)
        my_entry.delete(0, 'end')
    else:
        messagebox.showwarning('warning', 'Enter some task.')

def deleteTask():
    lb.delete(ANCHOR)


window = Tk()
window.geometry("400x400")
window.title("To do list")
window.config(bg='seagreen')


frame = Frame(window)
frame.pack(pady=10)


lb = Listbox(frame, width=30, height=8, font=('Montserrat', 18), bd =0, fg='red', highlightthickness=1, selectbackground='#a6a6a6', activestyle="none")
lb.pack(side=LEFT, fill=BOTH)

task_list = ["tablets", "write hw", "painting"]


for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=LEFT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    window,
    font=('Montserrat', 24)
    )

my_entry.pack(pady=20)

button_frame = Frame(window)
button_frame.pack(pady=10)

addTask_btn = Button(
    button_frame,
    text="Add Task",
    font='times 14',
    bg='cyan',
    padx=20,
    pady=20,
    command= newTask
)

addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

deleteTask_btn = Button(button_frame, text='Delete Task', font='times 14', bg='tomato', padx=20, pady=10, command= deleteTask)
deleteTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


window.mainloop()