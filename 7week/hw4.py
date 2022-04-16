##2021041047 허정윤

from tkinter import *
from tkinter.filedialog import *

def func_open() :
    global filename
    filename = askopenfilename(parent = window, filetypes = (("GIF 파일", "*gif"), ("모든 파일", "*.*")))
    photo = PhotoImage(file = filename)
    pLabel.configure(image = photo)
    pLabel.image = photo

def func_exit() :
    window.quit()
    window.destroy()

def zoom_in(event) :
    photo = PhotoImage(file = filename)
    photo = photo.zoom(2,2)
    pLabel.configure(image = photo)
    pLabel.image = photo

def zoom_out(event) :
    photo = PhotoImage(file = filename)
    photo = photo.subsample(2, 2)
    pLabel.configure(image = photo)
    pLabel.image = photo

window = Tk()
window.geometry("500x500")
window.title("그림 감상")

photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack(expand = 1, anchor = CENTER)

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일 열기", command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램 종료", command = func_exit)

window.bind("<Up>", zoom_in)
window.bind("<Down>", zoom_out)

window.mainloop()
                               
