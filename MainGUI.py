from tkinter import *

rect_width = 100
rect_height = 40

window = Tk()

bottomFrame = Frame(window, bg="red", height=180)
bottomFrame.pack(side=BOTTOM, fill=BOTH)

rightFrame = Frame(window, bg="yellow", width=200)
rightFrame.pack(side=RIGHT, fill=BOTH)

middleFrame = Frame(window, bg="pink")
middleFrame.pack(expand=1, fill=BOTH)

# Bottom Frame
timelineCanvas = Canvas(bottomFrame, bg="white", height=180, borderwidth=0, highlightthickness=0)
timelineCanvas.pack(fill=BOTH, expand=YES)

timeline_scroll = Scrollbar(bottomFrame, orient=HORIZONTAL, background="white", command=timelineCanvas.xview)
timeline_scroll.pack(side=BOTTOM, fill=X)
timelineCanvas.config(xscrollcommand=timeline_scroll.set)
timelineCanvas.xview_moveto(0)

def update():
    for i in range(5):
        y1 = i * rect_height
        y2 = y1 + rect_height
        timelineCanvas.create_rectangle(0, y1, 60, y2, fill="#04244B", outline="white",
                                         tags="clip_type")

    for i in range(5):
        y1 = i * rect_height
        y2 = y1 + rect_height
        timelineCanvas.create_rectangle(60, y1, timelineCanvas.winfo_width(), y2, fill="#0e0629", outline="white",
                                         tags="background")

    timelineCanvas.create_rectangle(10, 10, rect_width, rect_height, fill="#0071DB")
    timelineCanvas.create_text(rect_width / 2, rect_height/2+5, text="Click at")

    rect_x = 1500
    timelineCanvas.create_rectangle(rect_x, 10, rect_x + rect_width, rect_height, fill="#0071DB")
    timelineCanvas.create_text(rect_x + rect_width / 2, rect_height/2+5, text="Click at")

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
helpmenu.add_command(label="About", command=lambda: ...)

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Edit", menu=editmenu)
menubar.add_cascade(label="Help", menu=helpmenu)

window.mainloop()
