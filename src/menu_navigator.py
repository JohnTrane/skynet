import time
import pyautogui


def move_to_teleport():
  pyautogui.keyDown('d')
  time.sleep(0.35)
  pyautogui.keyUp('d')
  pyautogui.hotkey('f')


def select_level():
  move_to_teleport()
  pyautogui.keyDown('w')
  pyautogui.keyUp('w')
  pyautogui.keyDown('w')
  pyautogui.keyUp('w')
  pyautogui.keyDown('d')
  pyautogui.keyUp('d')
  pyautogui.keyDown('enter')
  pyautogui.keyUp('enter')


def vote_reset():
  pyautogui.hotkey('escape')
  pyautogui.hotkey('down')
  pyautogui.hotkey('down')
  pyautogui.hotkey('enter')
  time.sleep(3.3)


vote_reset()
select_level()