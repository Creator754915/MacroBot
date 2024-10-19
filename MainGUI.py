import webbrowser
from tkinter import *
import pyautogui as pt

rect_width = 100
rect_height = 40

window = Tk()

rightFrame = Frame(window, bg="lightgray", width=200)
rightFrame.pack(side=RIGHT, fill=BOTH)

timelineFrame = Frame(window, bg="lightblue", height=240)
timelineFrame.pack(side=BOTTOM, fill=BOTH)

infoFrame = Frame(window, bg="lightgray", width=155)
infoFrame.pack(side=LEFT, fill=BOTH)

middleFrame = Frame(window, bg="white")
middleFrame.pack(expand=1, fill=BOTH)

# Bottom Frame
timelineCanvas = Canvas(timelineFrame, bg="white", height=200, borderwidth=0, highlightthickness=0)
timelineCanvas.pack(fill=BOTH, expand=YES)

timeline_scroll = Scrollbar(timelineFrame, orient=HORIZONTAL, background="white", command=timelineCanvas.xview)
timeline_scroll.pack(side=BOTTOM, fill=X)
timelineCanvas.config(xscrollcommand=timeline_scroll.set)
timelineCanvas.xview_moveto(0)

# Right Frame
Label(rightFrame, text="Actions", bg="lightgray", font=('Arial', 16)).pack(side=TOP, padx=60)
for i in range(1, 10):
    Button(rightFrame, text=f"Action{i}", relief='groove', bg="lightblue").place(x=20, y=i * 65, width=180,
                                                                                 relheight=0.05)

# Left Frame
mousePosLabel = Label(infoFrame, text="", bg="lightgray", font=('Arial', 12))
mousePosLabel.pack()
mousePosLabel.place(x=2)


def update():
    for i in range(5):
        y1 = i * rect_height
        y2 = y1 + rect_height + 5
        timelineCanvas.create_rectangle(0, y1, 60, y2, fill="#04244B", outline="white",
                                         tags="clip_type")

    for i in range(5):
        y1 = i * rect_height
        y2 = y1 + rect_height + 5
        timelineCanvas.create_rectangle(60, y1, timelineCanvas.winfo_width(), y2, fill="#0e0629", outline="white",
                                         tags="background")

    rect_x = 100
    timelineCanvas.create_rectangle(rect_x, 1, rect_x + rect_width, rect_height - 1, fill="#0071DB")
    timelineCanvas.create_text(rect_x + rect_width / 2, rect_height/2, text="Click at")

    rect_x = 250
    timelineCanvas.create_rectangle(rect_x, 1, rect_x + rect_width, rect_height - 1, fill="#0071DB")
    timelineCanvas.create_text(rect_x + rect_width / 2, rect_height/2, text="Click at")


def getMousePos(event):
    x, y = pt.position()
    mousePosLabel.config(text=f'X:{str(x)} - Y:{str(y)}')
    return x, y


menubar = Menu(window)
window.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=update)
filemenu.add_command(label="Open", command=lambda: ...)
filemenu.add_command(label="Save", command=lambda: ...)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help")
helpmenu.add_separator()
helpmenu.add_command(label="About", command=lambda: webbrowser.open("https://macrobot.github.io"))

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Edit", menu=editmenu)
menubar.add_cascade(label="Help", menu=helpmenu)

window.bind("<Motion>", getMousePos)

window.mainloop()
