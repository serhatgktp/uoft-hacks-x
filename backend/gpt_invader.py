import pyautogui as pag
import win32clipboard
import time

# Before anything, the user must
# log into their openAI account manually

def init_open():
    # Open browser
    pag.moveTo(80, 1045, duration = 1)
    pag.click()
    time.sleep(1)

    # Open new tab
    # pag.hotkey('ctrl', 't')

    # Select address bar
    pag.moveTo(400, 60, duration = 0.2)
    pag.click()

    # Type in chatGPT url and hit enter
    pag.write('https://chat.openai.com')
    pag.press('enter')
    time.sleep(2)

def get_gpt_response(topic, mode='rw',):
    assert topic

    # Refresh page
    pag.moveTo(940, 960, duration = 0.6)
    pag.click()
    pag.press('f5')
    time.sleep(2)

    # Click chat box
    pag.moveTo(940, 960, duration = 0.6)
    pag.click()

    # Format user input
    if mode == 'rw':
        in_prompt = f"Generate a right-wing opinion on \"{topic}\""
        x1, y1 = 760, 220
    elif mode == 'disagree':
        in_prompt = f"Generate an opinion on whether abortion should be legal that disagrees with the following text: \"{topic}\""
        x1, y1 = 1000, 450
    elif mode == 'neutral':
        in_prompt = f"Generate a neutral opinion on \"{topic}\""
        x1, y1 = 760, 220
    
    # Enter prompt
    pag.write(in_prompt)
    pag.press('enter')    
    time.sleep(20)

    # Select entire response via triple-click
    pag.moveTo(x1, y1, duration = 0.6)
    for i in range(3):
        pag.click()

    # Copy response to clipboard
    pag.hotkey('ctrl', 'c')

    # Fetch clipboard data
    win32clipboard.OpenClipboard()
    gpt_response = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return gpt_response