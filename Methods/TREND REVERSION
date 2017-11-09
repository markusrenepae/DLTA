import pyautogui
import numpy as np
import datetime
import time

''' MOUSE FUNCTIONS '''
def move_cursor():
    pyautogui.moveTo(1309, 686)


def open_IQ():
    pyautogui.click(222, 750)
    move_cursor()


def put():
    pyautogui.click(1301, 561)
    move_cursor()


def call():
    pyautogui.click(1301, 444)
    move_cursor()


def new_position():
    pyautogui.click(1285, 462)
    move_cursor()


''' SCREEN ANALYSIS FUNCTIONS '''
def get_price_data(screen):
    price_data = np.array([])
    for x in range(350, 950):
        for y in range(145, 625):
            pixel_color = screen.getpixel((x, y))
            if pixel_color == (43, 171, 63):
                price_data = np.append(price_data, -y)
                return price_data
            elif pixel_color == (255, 167, 77):
                price_data = np.append(price_data, -y)
                break


def decide_bet(screen):
    ''' poly model '''
    price_data = get_price_data(screen)
    if price_data is not None:
        price_data_x = np.array(range(price_data.size))
        fit_func = np.polyfit(price_data_x, price_data, 1)
        fit = np.polyval(fit_func, price_data_x)
        error = price_data - fit
        std = np.std(error)
        dot_y = price_data[-1]
        last_fit = fit[-1]
        m = 0.0
        quarter_price_data_x = np.array_split(price_data_x, 2)
        quarter_price_data = np.array_split(price_data, 2)
        half_fit_func_0 = np.polyfit(quarter_price_data_x[0], quarter_price_data[0], 1)
        half_fit_func_1 = np.polyfit(quarter_price_data_x[1], quarter_price_data[1], 1)


        if last_fit + 2*std < dot_y and fit_func[0] < -m and half_fit_func_0[0] < -m and half_fit_func_1[0] < -m:
            put()
            print('put',std,abs((last_fit - dot_y)/std),fit_func[0],half_fit_func_0[0],half_fit_func_1[0])
            return True
        elif dot_y < last_fit - 2*std and fit_func[0] > m and half_fit_func_0[0] > m and half_fit_func_1[0] > m:
            call()
            print('call',std,abs((last_fit - dot_y)/std),fit_func[0],half_fit_func_0[0],half_fit_func_1[0])
            return True
        else:
            return False
    else:
        return False


open_IQ()
bet_done = False
while True:
    screen = pyautogui.screenshot()
    seconds = datetime.datetime.now().second
    if not bet_done and 19 < seconds < 28:
        bet_done = decide_bet(screen)
    elif bet_done and 10 < seconds < 15:
        time.sleep(60)
        new_position()
        bet_done = False
    else:
        pass
