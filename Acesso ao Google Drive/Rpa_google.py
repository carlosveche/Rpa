import pyautogui
import time

pyautogui.alert('Aguarde o código completar suas etapas')
pyautogui.PAUSE = 0.5

pyautogui.press('winleft') #Tela do Windows
pyautogui.write('chrome') 
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('https://app.powerbi.com/groups/4c787d14-ccc6-4d8f-adf7-e53e2d5c2357/reports/7ae6898e-4c55-4eaa-9fc3-4d426456f5fb/ReportSectionea69dffe7a068e585865')
time.sleep(1)
pyautogui.press('enter')
pyautogui.moveTo(901, 47)
time.sleep(1)
pyautogui.mouseDown()
pyautogui.mouseUp()
time.sleep(2)
pyautogui.moveTo(150,196)
pyautogui.mouseDown()
pyautogui.mouseUp()


time.sleep(2)


print(pyautogui.position())