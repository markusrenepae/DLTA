import pyautogui
import Calvar as var
import numpy as np


def traders_mood(screen):
    red = 0
    green = 0
    blue = 0
    for x in range(var.xmoodstart, var.xmoodend):
        for y in range(var.ymoodstart, var.ymoodend):
            red += screen.getpixel((x, y))[0]
            green += screen.getpixel((x, y))[1]
            blue += screen.getpixel((x, y))[2]
    print("average red: "+str(red/((var.xmoodend-var.xmoodstart)*(var.ymoodend-var.ymoodend))))
    print("average green: "+str(green/((var.xmoodend-var.xmoodstart)*(var.ymoodend-var.ymoodend))))
    print("average blue: "+str(blue/((var.xmoodend-var.xmoodstart)*(var.ymoodend-var.ymoodend))))
    #if-statements for returning values


def mean_splitter(price_data, n):
    means = []
    for i in range(n-1):
        means.append(np.mean(price_data[int(i * len(price_data) / (n-1)):int((i+1) * len(price_data) / (n-1))]))
    means.append(np.mean(price_data[int((n-2) * len(price_data) / (n-1))::]))
    return means
