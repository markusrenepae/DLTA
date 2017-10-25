import datetime
import time
import matplotlib.pyplot as plt
import numpy as np
import pyautogui
import Calvar as var


def move_cursor():
    pyautogui.moveTo(var.rand)


def open_IQ():
    pyautogui.click(var.chrome)
    move_cursor()
    time.sleep(1)


def put():
    pyautogui.click(var.put)
    move_cursor()


def call():
    pyautogui.click(var.call)
    move_cursor()


def new_position():
    pyautogui.click(var.newpos)
    move_cursor()


def get_price_data(screen):
    price_data = np.array([])
    for x in range(var.xstart, var.xend):
        for y in range(var.ystart, var.yend):
            pixel_color = screen.getpixel((x, y))
            if pixel_color == (43, 171, 63):
                price_data = np.append(price_data, -y)
                return price_data
            elif pixel_color == (255, 167, 77):
                price_data = np.append(price_data, -y)
                break


def plot_state(price_data_x, price_data, fit, std_limit):
    plt.plot(price_data_x, price_data, "orange")
    plt.scatter(price_data_x[-1], price_data[-1], color="green", s=5)
    plt.plot(price_data_x, fit, "red")
    plt.plot(price_data_x, fit + std_limit, "black")
    plt.plot(price_data_x, fit - std_limit, "black")
    plt.show()


def decide_bet(screen):
    price_data = get_price_data(screen)
    if price_data is not None:
        mean1 = np.mean(price_data)
        mean2 = np.mean(price_data[int(6 * len(price_data) / 7):len(price_data)])
        price_data_x = np.array(range(price_data.size))
        fit_func = np.polyfit(price_data_x, price_data, 1)
        fit = np.polyval(fit_func, price_data_x)
        error = price_data - fit
        currentsec = datetime.datetime.now().second
        if var.timeupper - 9 <= currentsec < var.timeupper:
            factor = var.stdfactor
        else:
            factor = var.stdfactor * (1 + 0.75 * (11 - currentsec) / 11)  # dynamic limit
        std_limit = factor * np.std(error)
        dot_y = price_data[-1]
        last_fit = fit[-1]
        if dot_y > last_fit + std_limit and (
                    mean2 - mean1 > 140 or (price_data[-1] - mean2 > 150 and currentsec > var.timelower + 10)):
            put()
            return True
        elif dot_y < last_fit - std_limit and (
                    mean1 - mean2 > 140 or (mean2 - price_data[-1] > 150 and currentsec > var.timelower + 10)):
            call()
            return True
        else:
            return False


open_IQ()
bet_done = False
while True:
    screen = pyautogui.screenshot()
    seconds = datetime.datetime.now().second
    if var.timelower <= seconds < var.timeupper:
        bet_done = decide_bet(screen)
        if bet_done:
            time.sleep(25)
        else:
            pass
        new_position()
    else:
        pass
