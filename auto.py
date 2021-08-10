# Automoçao Com Python, fazendo udate pra o google drive 
import pyautogui
import time

pyautogui.alert("codigo rodando, nao usar o computador")

pyautogui.PAUSE = 0.5
# abrindo google dive no pc, precionando a tecla windows
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

time.sleep(1)

pyautogui.write("https://drive.google.com/drive/u/0/my-drive")
pyautogui.press('enter')

# entrar na area de trabalho e pegar arquivo
pyautogui.hotkey('win', 'd')

# clicar no arquivo e arrastar ele
pyautogui.moveTo(3704, 98)
pyautogui.mouseDown()

# arratar arquivo e jogar dentro do googledrive
pyautogui.moveTo(2318, 1413)
pyautogui.hotkey('alt', 'tab')
pyautogui.mouseUp()

