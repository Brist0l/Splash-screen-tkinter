The tksplash module can be used to make splash screens for all of your GUIs which you make using tkinter 

These are some examples on how to use this module :

```
import tkinter
import tksplash

window = tkinter.Tk() #making a basic window 

width = window.winfo_screenwidth() # getting the screen width
height = window.winfo_screenheight() # getting the screen height
 
window.geometry("%dx%d" % (width, height)) # setting the window with respect to the height and width

tksplash.add_splash_text(window, "Hello World", width, height, 100)

window.mainloop()
````

______________
the `tksplash.add_splash_text()` takes in exactly 8 arguments and out of which only 5 are required the other 3 are
optional 

`window, text, width, height, font_size`

these are the required values 👆👆

`font_style , text_colour , time_after_which_it_should_destroy`

these are the optional values 👆👆
___
`window`--> you have to provide the name of the window 

`text`--> the text you want to display 

`widht`--> the width of the window

`height`--> the height of the window

`font_size`--> the value for the font size 

`font_style`--> which font style do you want ?? 

`text_colour`--> the colour of the fonts 

`time_after_which_it_should_destroy` --> the time that the text is being shown 🕛

_________________________

An example using all the arguments

```
import tkinter
import tksplash

window = tkinter.Tk()
width = window.winfo_screenwidth()
height = window.winfo_screenheight()

window.geometry("%dx%d" % (width, height))

tksplash.add_splash_text(window, "Hello World", width, height, 100, font_style="Lucida Grande", text_colour='white',time_after_which_it_should_destroy=3000)

window.mainloop()
```

⚠⚠⚠⚠

**Note**->the `text_colour` can also be written as `#RRGGBB` 

**Note**->The value of `time_after_which_it_should_destroy` should be entered in millisecond(ms), (1 s = 1000ms) 


------

Adding an image in the splash screen 

`tksplash.add_image(window,"ts.png", 500, 500, 20, 40)`

The `add_image()` function takes in exactly `7` arguments and out of that only 6 are required and 1 is optional 

`window, img, img_x, img_y, place_x, place_y`

these are the required values 👆👆

`time_after_which_it_should_destroy`

these are the optional values 👆👆

___
`window`--> you have to provide the name of the window 

`img`--> the image you want to project on the splash screen 

`img_x`--> the width of the image 

`img_y`--> the height of the image 

`place_x`--> the x value where you want to place the image

`place_y`--> the y value where you want to place the image

`time_after_which_it_should_destroy` --> the time that the text is being shown 

_________________________

Adding  image as well as text use `add_image_text()` function 

It takes in these values 

`window, text, width, height, font_size, img, img_x, img_y, place_x, place_y,font_style="Lucida Grande", text_colour='#FF002D', time_after_which_it_should_destroy=3000`





