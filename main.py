import pyautogui as pt
import time as time
import tkinter as tk
import json

timeline = {}

timeline["1"] = {"moveTo": {"x": 0, "y": 0}}
timeline["2"] = {"moveTo": {"x": 100, "y": 0}}

print(timeline)


class AddAction:
    def __init__(self):
        super().__init__()
        self.timeline = {}
        self.x, self.y = 0, 0

    def clickAt(self):
        print('positionnez vous pour cliquer')
        for i in range(4):
            time.sleep(1)
            print(i)
        repx, repy = pt.position()
        self.x = repx
        self.y = repy
        print("Coordonnées enregistrées :", self.x, self.y)
        self.timeline[len(self.timeline) + 1] = {"clickAt": {"x": self.x, "y": self.y}}
        print(timeline)

    def getMousePosition(self):
        time.sleep(3)
        return pt.position()

    def moveTo(self, x, y):
        try:
            print("coordonné enregistrées : ", x, y)
            self.timeline[len(self.timeline) + 1] = {"moveTo": {"x": x, "y": y}}
        except (SyntaxError, NameError) as e:
            return e

    def slideFromTo(self, pos1: tuple, pos2: tuple):
        self.timeline[len(self.timeline) + 1] = {"slideFormTo": [pos1, pos2]}

    def detectImage(self):
        path = str(input("Enter the path of the image => "))
        self.timeline[len(self.timeline) + 1] = {"detectImage": {"path": path}}

    def getColorOfPixel(self, x, y):
        return pt.pixel(x, y)

    def waitSince(self, time: int | float):
        if time > 0:
            self.timeline[len(self.timeline) + 1] = {"waitSince": time}
        else:
            return 0

    def writeThis(self, text: str | int):
        self.timeline[len(self.timeline) + 1] = {"writeThis": text}

    def shortcut(self, type):
        if type == "copy":
            self.timeline[len(self.timeline) + 1] = {"shortcut": "copy"}
        elif type == "paste":
            self.timeline[len(self.timeline) + 1] = {"shortcut": "paste"}
        elif type == "cut":
            self.timeline[len(self.timeline) + 1] = {"shortcut": "cut"}
        else:
            return "TypeError: shortcut isn't exist"

    def clear(self):
        self.timeline.clear()

    def saveTimeline(self, filename: str):
        with open(f"{filename}.json", 'w') as f:
            json.dump(self.timeline, f, indent=2)


test = AddAction()
test.moveTo(0, 0)
test.getMousePosition()
test.waitSince(2)
test.shortcut("copy")
test.slideFromTo((100, 100), (500, 854))
test.writeThis("This is a macro !")
test.detectImage()
test.saveTimeline("savefile")
