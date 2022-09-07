from tkinter import *
from tkinter import ttk


def add_item():
    list_box.insert(END, enter_entry.get())
    enter_entry.delete(0, END)


def remove_value(event):
    selection = list_box.curselection()
    list_box.delete(selection)


def del_list():
    select = list(list_box.curselection())
    select.reverse()
    for i in select:
        list_box.delete(i)


root = Tk()
root.title("Графика")
root.geometry('400x400')

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

Label(mainframe, text='Введите слово, которое хотите добавить в trie дерево: ').grid(column=1, row=1, sticky=W)

# поле ввода для слова, которое будем добавлять в это trie_tree
enter = StringVar()
enter_entry = ttk.Entry(mainframe, width=7, textvariable=enter)
enter_entry.grid(column=2, row=1, sticky=(W, E))

button = ttk.Button(mainframe, text="Добавить", command=add_item)
button.grid(column=2, row=2, sticky=W)


list_box = Listbox(mainframe)
list_box.grid(column=1, row=3)

list_box.bind("<Double-Button-1>", remove_value)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()



