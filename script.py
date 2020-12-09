import pyautogui as pag

pag.PAUSE = 0.5
pag.FAILSAFE = True # failsafe

#move cursor (legacy)
#pag.moveTo(120, 1055) # coordinates of lower search box

#click (legacy)
#pag.click()

# open start menu
pag.hotkey('ctrl', 'esc')

#search
pag.typewrite("command prompt")
pag.typewrite(['enter'])

#set window to the left
pag.keyDown('win')
pag.keyDown('up')
pag.keyUp('up')
pag.keyDown('left')
pag.keyUp('left')
pag.keyUp('win')

#type something in the terminal
pag.typewrite("cd C:\\Users\\simon\\Desktop\\FALL2020\\")
pag.typewrite(['enter'])

