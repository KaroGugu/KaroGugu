import pyautogui
import random

charts = "1234567890"
chart_list = list(charts)
password = pyautogui.password("Enter your test password : ")

guess_password = ""

while guess_password != password:
    guess_password = random.choices(chart_list.k==len(password))
    print(f"DESCRIPING {guess_password} PASSWORD")

    if guess_password == list(password):
        print(f"Your password is : {''.join(guess_password)}")
        break