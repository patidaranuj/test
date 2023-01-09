import pyautogui
pyautogui.moveTo(410, 622, duration = 1)
i=0
while(i<300):
	pyautogui.click(410, 622)
	pyautogui.typewrite(["down"])
	i=i+1
