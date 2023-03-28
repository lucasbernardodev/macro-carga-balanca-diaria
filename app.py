import pyautogui
import time
from tkinter import Tk
from tkinter.messagebox import Message 
from _tkinter import TclError


# INFORMATIVO #
aguarda = 10000 # millisegundos
root = Tk() 
root.withdraw()
try:
    root.after(aguarda, root.destroy) 
    Message(title="Carga MGV7", message="Aguarde a carga passar, por favor não mexa. Para cancelar feche a aplicação 'App.py'.", master=root).show()
except TclError:
    pass

# INICIO # 
# 1 - Pressionar tecla WINDOWS.
pyautogui.press('win')
time.sleep(1)
# 2 - Digitar "cargabalanca".
pyautogui.typewrite('cargabalanca', interval=0.2)
# 3 - Pressionar tecla ENTER.
pyautogui.press('enter')
# 4 - Aguardar 5 segundos.
time.sleep(2)
pyautogui.click(960,323,duration=0.1)
time.sleep(2)
# 5 - Pressionar tecla ALT + V.
pyautogui.hotkey('alt', 'v')
# 6 - Pressionar tecla ALT + A.
pyautogui.hotkey('alt', 'a')
# 7 - Clicar na opção "TOLEDO"
pyautogui.click(638,394,duration=0.1)
# 8 - Pressiontar tecla ALT + G.
pyautogui.hotkey('alt', 'g')
# 9 - Aguardar 10 segundos.
time.sleep(10)
# 10 - Pressionar tecla ENTER.
pyautogui.hotkey('enter')
# 11 - Pressionar tecla ENTER.
pyautogui.hotkey('enter')
# 12 - Pressionar tecla ALT + F4.
pyautogui.hotkey('alt', 'f4')
# 13 - Pressionar tecla WINDOWS.
pyautogui.press('win')
# 14 - Digitar "mgv7".
pyautogui.typewrite('mgv7', interval=0.2)
# 15 - Pressionar enter.
pyautogui.press('enter')
# 16 - Aguardar 20 segundos.
time.sleep(20)
pyautogui.click(772,130,duration=0.1)
# 17 - Clicar em "IMPORTAÇÂO"
pyautogui.click(454,113,duration=0.2)
time.sleep(1)
# 18 - Clicar em "IMPORTAR"
pyautogui.click(977,211,duration=0.2)
# 19 - Aguardar 30 segundos.
time.sleep(30)
# 20 - Pressionar tecla ENTER
pyautogui.press('enter')
time.sleep(1)
# 21 - Pressionar tecla TAB
pyautogui.press('tab')
time.sleep(1)
# 22 - Pressionar tecla ENTER
pyautogui.press('enter')
time.sleep(1)
# 22 - Pressionar tecla ENTER
pyautogui.press('enter')
time.sleep(1)
# 21 - Pressionar tecla TAB
pyautogui.press('tab')
time.sleep(1)
# 22 - Pressionar tecla ENTER
pyautogui.press('enter')
time.sleep(1)
# 23 - Pressionar no botão SAIR
pyautogui.click(973,469,duration=0.2)
# 24 - Pressionar no botão CARGA
pyautogui.click(621,116,duration=0.2)
time.sleep(1)
# 25 - Pressionar no botão ENVIAR
pyautogui.click(991,110,duration=0.2)
time.sleep(3)
# 26 - Pressionar tecla ENTER
pyautogui.hotkey('alt','f4')
time.sleep(1)
# 27 - Pressionar no botão SAIR
pyautogui.click(1017,644,duration=0.2)
time.sleep(1)
# 28 - Pressionar tecla ALT + F4
pyautogui.hotkey('alt','f4')
# FIM #

aguarda = 5000 # millisegundos
root = Tk() 
root.withdraw()
try:
    root.after(aguarda, root.destroy) 
    Message(title="Situação carga MGV7", message="Finalizado!", master=root).show()
except TclError:
    pass

exit()