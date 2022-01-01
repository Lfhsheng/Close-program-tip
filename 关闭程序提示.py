from tkinter import *
import tkinter.messagebox as messagebox
def closeWindow():
    askback = messagebox.askyesno('提示', '真的要关闭这个程序吗？')
    if askback == True:
        window.destroy()
window = Tk()
window.title('关闭程序提示 By 泠风寒声')
window.protocol('WM_DELETE_WINDOW', closeWindow)
window.mainloop()