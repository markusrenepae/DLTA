import pyHook
import pythoncom
import pyautogui
import time

def onclick(event):
    print(event.Position)               #prints coordinates of the mouse click
    print(pyautogui.screenshot().getpixel(event.Position))      #prints out RGB of a pixel that was clicked on
    print(str(time.time())+"\n")        #prints out the current system time
    return True

hm = pyHook.HookManager()
hm.SubscribeMouseAllButtonsDown(onclick)
hm.HookMouse()
pythoncom.PumpMessages()
hm.UnhookMouse()
