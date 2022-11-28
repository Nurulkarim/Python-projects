from django.http import HttpResponseNotAllowed
import pyautogui
import time

n=3
for i in range(n):
    time.sleep(4)
    pyautogui.typewrite('hi,It\'s your day')
    time.sleep(1)
    pyautogui.press('enter')
    
