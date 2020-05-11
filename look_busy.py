import pyautogui as pag
import random

pag.PAUSE, pag.FAILSAFE = 1, True # Bot configuration (take mouse to 0, 0 to stop)
screen_w, screen_h = pag.size() # Screen info 
mouse_x, mouse_y = pag.position() # Current mouse position 
center_x, center_y = screen_w / 2, screen_h / 2  # Screen center (adjust when needed)
screen_min, screen_max = 0.1, 0.3 
w_min, w_max, h_min, h_max = int(screen_min * screen_w), int(screen_max * screen_w), int(screen_min * screen_h), int(screen_max * screen_h) # Bot is allowed to move mouse from 10 % - 30 % of screen area 

print('----Initiating bot----')
print('Suggestion: Minimize all windows to prevent undesired actions and hide desktop icons')
print('Screen height:', screen_h, 'Screen width:', screen_w)
print('Current mouse position (x, y):', mouse_x, ',', mouse_y)
print('Take mouse to (0, 0) to stop...')
pag.moveTo(center_x, center_y, 5) # Center mouse on screen 

while True: 
    next_x, next_y = random.randint(w_min, w_max), random.randint(h_min, h_max) # Next random x, y mouse position within allowed limits 
    delay_time = random.random() * 10 # Random delay time in seconds to perform action 
    pag.moveTo(next_x, next_y, delay_time) # Move cursor to next random position on random time 
    pag.doubleClick() # Do a double click to prevent idle or sleep 