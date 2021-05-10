import tkinter.font as font
from tkinter import *
import time
from PIL import Image


def add_splash_text(window, text, width, height, font_size, font_style="Lucida Grande",
                    text_colour='#FF002D', time_after_which_it_should_destroy=3000):
    # To destroy the label after a given time
    def destroy():
        splash_screen_label.destroy()

    # Setting the font style and the font size
    fontStyle = font.Font(family=font_style, size=font_size)
    splash_screen_label = Label(window, text=str(text), font=fontStyle,
                                fg=text_colour)  # Making a label and setting the  appropriate attributes
    x_pos = width / 2  # finding the middle of the screen
    y_pos = height / 2  # finding the middle of the screen
    # Place the label at the given coordinates
    splash_screen_label.place(x=x_pos, y=y_pos, anchor=CENTER)
    # Pause everything until this has loaded
    window.wait_window(splash_screen_label)
    window.after(time_after_which_it_should_destroy,
                 destroy)  # Destroying the label after the given time period


def add_image(window, img, img_x, img_y, place_x, place_y, time_after_which_it_should_destroy=3000):
    def destroy(thing): return thing.destroy()

    canvas = Canvas(window, width=img_x, height=img_y)
    canvas.place(x=place_x, y=place_y, anchor=CENTER)
    image = PhotoImage(file=img)
    canvas.create_image(place_x, place_y, anchor=NW, image=image)
    window.after(time_after_which_it_should_destroy,
                 destroy(canvas))  # Destroying the label after the given time period
    window.wait_window(canvas)  # Pause everything until this has loaded


def add_image_text(window, text, width, height, font_size, img, img_x, img_y, place_x, place_y,
                   font_style="Lucida Grande", text_colour='#FF002D',
                   time_after_which_it_should_destroy=3000):
    def destroy(thing): return thing.destroy()

    canvas = Canvas(window, width=img_x, height=img_y)
    canvas.place(x=place_x, y=place_y, anchor=CENTER)
    image = PhotoImage(file=img)
    canvas.create_image(place_x, place_y, anchor=NW, image=image)
    window.after(time_after_which_it_should_destroy,
                 destroy(canvas))  # Destroying the label after the given time period
    # Setting the font style and the font size
    fontStyle = font.Font(family=font_style, size=font_size)
    splash_screen_label = Label(window, text=str(text), font=fontStyle,
                                fg=text_colour)  # Making a label and setting the  appropriate attributes
    x_pos = width / 2  # finding the middle of the screen
    y_pos = height / 2  # finding the middle of the screen
    # Place the label at the given coordinates
    splash_screen_label.place(x=x_pos, y=y_pos, anchor=CENTER)
    window.after(time_after_which_it_should_destroy,
                 destroy(splash_screen_label))  # Destroying the label after the given time period
    # Pause everything until this has loaded
    window.wait_window(splash_screen_label)
    window.wait_window(canvas)  # Pause everything until this has loaded


def add_gif(window, gif, place_x, place_y, time_after_which_it_should_destroy=3000):
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
            if int(time1) == int(time_after_which_it_should_destroy) / 1000:
                label.destroy()
            window.after(100, update, ind)
        else:
            return

    # print("running..")
    label = Label(window)
    # print("label made")
    label.place(x=place_x, y=place_y)
    # print("placed")
    update(0)
    window.wait_window(label)


def add_gif_text(window, text, width, height, font_size, gif, place_x, place_y,
                 font_style="Lucida Grande", text_colour='#FF002D', time_after_which_it_should_destroy=3000):
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
            if int(time1) == time_after_which_it_should_destroy:
                label.destroy()
            window.after(100, update, ind)
        else:
            return

    label = Label(window)
    x_pos = width / 2
    y_pos = height / 2
    label.place(x=place_x, y=place_y)
    fontStyle = font.Font(family=font_style, size=font_size)
    splash_screen_label = Label(window, text=str(text), font=fontStyle,
                                fg=text_colour)
    splash_screen_label.place(x=x_pos, y=y_pos, anchor=CENTER)
    # print("placed")
    update(0)
    window.wait_window(label)
    # window.wait_window(splash_screen_label)
    window.after(1,
                 destroy)  # Destroying the label after
