from tkinter import Label, Tk
import time

app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("410x150")
app_window.resizable(1,1)

text = ("Boulder", 70, "bold")
background = "white"
foreground = "blue"
borderWidth = 20

label = Label(app_window, font=text, bg=background, fg=foreground, bd=borderWidth)
label.grid(row=0, column=1)

def clock():
    liveTime = time.strftime("%H:%M:%S")
    label.config(text=liveTime)
    label.after(200, clock)

clock()
app_window.mainloop()