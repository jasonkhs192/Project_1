import os
from tkinter import *

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("620x480")

#Scroll Bar
scroll = Scrollbar(root)
scroll.pack(side="right", fill = "y")

#Text Field
txt = Text(root, yscrollcommand=scroll.set)
txt.pack(side="left", fill = "both", expand=True)

scroll.config(command=txt.yview)


#Menu
menu = Menu(root)

#파일 메뉴
filename = "note.txt"

def open_file():
    if os.path.isfile(filename):
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0", END)
            txt.insert(END, file.read())

def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0",END))

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New")
menu_file.add_command(label="New Window")
menu_file.add_command(label="Open...", command=open_file)
menu_file.add_command(label="Save", command=save_file)
menu_file.add_command(label="Save As...")
menu_file.add_separator()
menu_file.add_command(label="Page Setup...")
menu_file.add_command(label="Print...")
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

#편집 메뉴
menu_edit = Menu(menu, tearoff=0)
menu_edit.add_command(label="Undo", state="disable")

menu.add_cascade(label="Edit", menu=menu_edit)

#서식 메뉴
menu_format = Menu(menu, tearoff=0)
menu_format.add_command(label="Word wrap")
menu_format.add_command(label="Font...")

menu.add_cascade(label="Format", menu=menu_format)

#보기 메뉴
menu_view = Menu(menu, tearoff=0)
submenu_zoom = Menu(menu_view, tearoff=0)

submenu_zoom.add_command(label="Zoom In")
submenu_zoom.add_command(label="Zoom Out")

menu_view.add_cascade(label="Zoom", menu=submenu_zoom)
menu_view.add_checkbutton(label="Status Bar")

menu.add_cascade(label="View", menu=menu_view)

#도움말 메뉴
menu_help = Menu(menu, tearoff=0)
menu_help.add_command(label="View Help")
menu_help.add_command(label="Send Feedback")
menu_help.add_separator()
menu_help.add_command(label="About Notepad")
menu.add_cascade(label="Help", menu=menu_help)

root.config(menu=menu)
root.mainloop()