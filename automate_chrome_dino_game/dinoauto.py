import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
# from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)
    # return
def isCollideB(data):
    # Draw the rectangle for birds
    for i  in range(520,580):
        for j in range(160,210):
            if data[i, j] > 100  :
                hit('down')
                time.sleep(0.3)
                pyautogui.keyUp('down')
                return

    for i in range(505, 560):
        for j in range(220, 250):
            if data[i, j] > 100:
                hit("up")
                return
    return


def isCollideW(data):
    # Draw the rectangle for birds
    for i  in range(520,580):
        for j in range(160,210):
            if data[i, j] < 100  :
                hit('down')
                time.sleep(0.3)
                pyautogui.keyUp('down')
                return

    for i in range(505, 560):
        for j in range(220, 250):
            if data[i, j] < 100:
                hit("up")
                return
    return


if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    # hit('up') 

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        if data[210,500] > 200:
            isCollideW(data)
        else:
            isCollideB(data)


        # for i in range(210,250):
        #     for j in range(500,550):
        #         if data[i, j] == 255:
        #             isCollideB(data)
        #         else:
        #             isCollideW(data)
            
        # print(asarray(image))
        '''
        # Draw the rectangle for cactus
        for i in range(275, 325):
            for j in range(563, 650):
                data[i, j] = 0
        
        # Draw the rectangle for birds
        for i in range(250, 300):
            for j in range(410, 563):
                data[i, j] = 171

        image.show()
        break
      '''



