import tkinter as tk
#from tkinter import *
import cv2
import numpy as np
from PIL import Image
from imutils.video import VideoStream
import subprocess
from subprocess import Popen, PIPE


parent = tk.Tk()
parent.geometry("800x500")
var = tk.StringVar()

rotation =  tk.Label(parent, textvariable=var, font=('Times', 24)).place(x = 500, y = 45)
def cam_start():
    capStream = VideoStream('rtsp://admin:csircmeri@192.168.18.188:554/streaming/channels/401').start()
    print("camera open")
    while(True):
        cap = capStream.read()
        cv2.imshow('front view',cap)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    capStream.release()
    cv2.destroyAllWindows()

def stt_start():
	pass



def stp_stop():
	pass



var.set("Hey! How are you doing?" '\n'  "This is The ip_camera Interface" '\n')

btn1 = tk.Button(parent, text = "Camera_start", activebackground = "green", activeforeground = "blue", command = cam_start, state= "normal")
btn1.place(x = 70, y = 100)

sbmitbtn2 = tk.Button(parent, text = "Start_Recording", activebackground = "green", activeforeground = "blue", command = stt_start, state= "normal")
sbmitbtn2.place(x = 70, y = 200)

sbmitbtn3 = tk.Button(parent, text = "Stop_Recording", activebackground = "green", activeforeground = "blue", command = stp_stop, state= "normal")
sbmitbtn3.place(x = 70, y = 240)









if __name__ == "__main__":
    parent.mainloop()
