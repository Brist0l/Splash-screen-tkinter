import tksplash
import tkinter

win = tkinter.Tk()
win.geometry("500x500")
splash = tksplash.Tksplash(win)
splash.add_gif_text("hello", 500, 500, "test.gif", 100, 100)
tkinter.Button(win, text="hello").pack()
win.mainloop()
