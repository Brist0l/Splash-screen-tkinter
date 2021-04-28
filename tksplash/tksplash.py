from tkinter import *
import tkinter.font as font


def add_splash_text(window, text, width, height, font_size, font_style="Lucida Grande",
                    text_colour='#FF002D', time_after_which_it_should_destroy=3000):
    # To destroy the label after a given time

    def destroy():
        splash_screen_label.destroy()

    fontStyle = font.Font(family=font_style, size=font_size)  # Setting the font style and the font size
    splash_screen_label = Label(window, text=str(text), font=fontStyle,
                                fg=text_colour)  # Making a label and setting the  appropriate attributes
    x_pos = width / 2  # finding the middle of the screen
    y_pos = height / 2  # finding the middle of the screen
    splash_screen_label.place(x=x_pos, y=y_pos, anchor=CENTER)  # Place the label at the given coordinates
    window.after(time_after_which_it_should_destroy, destroy)  # Destroying the label after the given time period
    window.wait_window(splash_screen_label)  # Pause everything until this has loaded


def add_image(window, img, img_x, img_y, place_x, place_y, time_after_which_it_should_destroy=3000):
    def destroy():
        canvas.destroy()

    canvas = Canvas(window, width=img_x, height=img_y)
    canvas.place(x=place_x, y=place_y, anchor=CENTER)
    image = PhotoImage(file=img)
    canvas.create_image(place_x, place_y, anchor=NW, image=image)
    window.after(time_after_which_it_should_destroy, destroy)  # Destroying the label after the given time period
    window.wait_window(canvas)  # Pause everything until this has loaded


def add_image_text(window, text, width, height, font_size, img, img_x, img_y, place_x, place_y,
                   font_style="Lucida Grande", text_colour='#FF002D',
                   time_after_which_it_should_destroy=3000):
    def destroy():
        splash_screen_label.destroy()
        canvas.destroy()

    canvas = Canvas(window, width=img_x, height=img_y)
    canvas.place(x=place_x, y=place_y, anchor=CENTER)
    image = PhotoImage(file=img)
    canvas.create_image(place_x, place_y, anchor=NW, image=image)
    window.after(time_after_which_it_should_destroy, destroy)  # Destroying the label after the given time period
    fontStyle = font.Font(family=font_style, size=font_size)  # Setting the font style and the font size
    splash_screen_label = Label(window, text=str(text), font=fontStyle,
                                fg=text_colour)  # Making a label and setting the  appropriate attributes
    x_pos = width / 2  # finding the middle of the screen
    y_pos = height / 2  # finding the middle of the screen
    splash_screen_label.place(x=x_pos, y=y_pos, anchor=CENTER)  # Place the label at the given coordinates
    window.after(time_after_which_it_should_destroy, destroy)  # Destroying the label after the given time period
    window.wait_window(splash_screen_label)  # Pause everything until this has loaded
    window.wait_window(canvas)  # Pause everything until this has loaded

