import pyautogui
from PIL import Image, ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def collide(data):
    for i in range(600,650):
        for j in range(420,480):
            if data[i,j]<170:
                hit("up")
                return
                
    for i in range(600,650):
        for j in range(300,400):
            if data[i,j]<170:
                hit("down")
                return
    return



if __name__=="__main__":
    print("start")
    time.sleep(5)
    print("now")
    hit("up")
    while True:
        image=ImageGrab.grab().convert('L')
        data=image.load()
        collide(data)
        
    
    
    
    # for i in range(500,550):
    #     for j in range(420,480):
    #         data[i,j]=0
                
    # for i in range(500,550):
    #     for j in range(300,400):
    #         data[i,j]=70

    # image.show()