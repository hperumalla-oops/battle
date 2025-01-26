from tkinter import *
from time import sleep
from gpiozero import AngularServo


root = Tk()

def rotate():
	servo = AngularServo(17, min_angle = -90, max_angle = 90)
	angle = V1.get()
	while True:
		servo.angle = angle
		sleep(20)

V1 = DoubleVar()
Title = Label(root,text = "select the angle of rotation using slider")


Slider = Scale(root, variable = V1,from_ = -90, to=90, length=720, tickinterval=15, orient = "horizontal")
Submit = Button(root,text = "Click here to rotate ",command = lambda: rotate()) #, bg= 'Yellow')

Title.pack(anchor = CENTER)
Slider.pack(anchor = CENTER)
Submit.pack(anchor = CENTER)

root.mainloop()
