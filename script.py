import pyautogui as pag

pag.PAUSE = 0.5
pag.FAILSAFE = True # failsafe

#move cursor
pag.moveTo(120, 1055) # coordinates of lower search box

#click
pag.click()

#search
pag.typewrite("command prompt")
pag.typewrite(['enter'])

#type something in the terminal
pag.typewrite("cd C:\\Users\\simon\\Desktop\\FALL2020\\")
pag.typewrite(['enter'])
