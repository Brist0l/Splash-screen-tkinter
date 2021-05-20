import tkinter.font as font
from tkinter import *
import time
from PIL import Image


class Tksplash:
    def __init__(self, window, destroy_time=3000, font_style="Lucida Grande",text_colour='#FF002D',font_size=100):
        self.win = window
        self.time = destroy_time
        self.text = font_style
        self.colour = text_colour
        self.size = font_size

    def add_splash_text(self, text, width, height):
        # To destroy the label after a given time
        def destroy(thing): return thing.destroy()

        # Setting the font style and the font size
        fontStyle = font.Font(family=self.text, size=self.size)
        splash_screen_label = Label(self.win, text=str(text), font=fontStyle,
                                    fg=self.colour)  # Making a label and setting the  appropriate attributes
        x_pos = width / 2  # finding the middle of the screen
        y_pos = height / 2  # finding the middle of the screen
        # Place the label at the given coordinates
        splash_screen_label.place(x=x_pos, y=y_pos, anchor=CENTER)
        # Pause everything until this has loaded
        self.win.wait_window(splash_screen_label)
        self.win.after(self.time,
                       destroy(thing=splash_screen_label))  # Destroying the label after the given time period

    def add_image(self, img, img_x, img_y, place_x, place_y):
        def destroy(thing): return thing.destroy()

        canvas = Canvas(self.win, width=img_x, height=img_y)
        canvas.place(x=place_x, y=place_y, anchor=CENTER)
        image = PhotoImage(file=img)
        canvas.create_image(place_x, place_y, anchor=NW, image=image)
        self.win.after(self.time,
                       destroy(canvas))  # Destroying the label after the given time period
        self.win.wait_window(canvas)  # Pause everything until this has loaded

    def add_image_text(self, text, width, height, img, img_x, img_y, place_x, place_y,):
        def destroy(thing): return thing.destroy()

        canvas = Canvas(self.win, width=img_x, height=img_y)
        canvas.place(x=place_x, y=place_y, anchor=CENTER)
        image = PhotoImage(file=img)
        canvas.create_image(place_x, place_y, anchor=NW, image=image)
        self.win.after(self.time,
                       destroy(canvas))  # Destroying the label after the given time period
        # Setting the font style and the font size
        fontStyle = font.Font(family=self.text, size=self.size)
        splash_screen_label = Label(self.win, text=str(text), font=fontStyle,
                                    fg=self.colour)  # Making a label and setting the  appropriate attributes
        x_pos = width / 2  # finding the middle of the screen
        y_pos = height / 2  # finding the middle of the screen
        # Place the label at the given coordinates
        splash_screen_label.place(x=x_pos, y=y_pos, anchor=CENTER)
        self.win.after(self.time,
                       destroy(splash_screen_label))  # Destroying the label after the given time period
        # Pause everything until this has loaded
        self.win.wait_window(splash_screen_label)
        self.win.wait_window(canvas)  # Pause everything until this has loaded

    def add_gif(self, gif, place_x, place_y):
        def count(main_gif):
            # print("counting..")
            file = Image.open(main_gif)
            # print("done")
            return file.n_frames

        frameCount = count(gif)
        frames = [PhotoImage(file=gif, format='gif -index %i' % i) for i in
                  range(frameCount)]  # iterating over the given number of frames

        start = time.perf_counter()

        def update(ind):
            info = label.winfo_exists()
            if info:
                # print(f"updating..{ind}")
                frame = frames[ind]
                ind += 1
                if ind == frameCount:
                    ind = 0
                label.configure(image=frame)
                end = time.perf_counter()
                time1 = end - start
                if int(time1) == int(self.time) / 1000:
                    label.destroy()
                self.win.after(100, update, ind)
            else:
                return

        # print("running..")
        label = Label(self.win)
        # print("label made")
        label.place(x=place_x, y=place_y)
        # print("placed")
        update(0)
        self.win.wait_window(label)

    def add_gif_text(self, text, width, height, gif, place_x, place_y):
        def count(main_gif):
            # print("counting..")
            file = Image.open(main_gif)
            # print("done")
            return file.n_frames

        def destroy():
            splash_screen_label.destroy()

        frameCount = count(gif)
        frames = [PhotoImage(file=gif, format='gif -index %i' % i) for i in
                  range(frameCount)]  # iterating over the given number of frames

        start = time.perf_counter()

        def update(ind):
            info = label.winfo_exists()
            if info:
                # print(f"updating..{ind}")
                frame = frames[ind]
                ind += 1
                if ind == frameCount:
                    ind = 0
                label.configure(image=frame)
                end = time.perf_counter()
                time1 = end - start
                if int(time1) == self.time:
                    label.destroy()
                self.win.after(100, update, ind)
            else:
                return

        label = Label(self.win)
        x_pos = width / 2
        y_pos = height / 2
        label.place(x=place_x, y=place_y)
        fontStyle = font.Font(family=self.text, size=self.size)
        splash_screen_label = Label(self.win, text=str(text), font=fontStyle,
                                    fg=self.colour)
        splash_screen_label.place(x=x_pos, y=y_pos, anchor=CENTER)
        # print("placed")
        update(0)
        self.win.wait_window(label)
        # window.wait_window(splash_screen_label)
        self.win.after(1,
                       destroy)  # Destroying the label after
