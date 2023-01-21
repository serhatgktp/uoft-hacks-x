import pyautogui as pag
import win32clipboard
import time

MAX_PROMPT_LEN = 180

def get_gpt_response(max_prompt_len):
    
    ### SKIP THIS PORTION IF YOU MANUALLY AUTHENTICATED TO CHATGPT
    # # Open firefox
    # pag.moveTo(80, 1045, duration = 1)
    # pag.click()
    # time.sleep(1)

    # # Select address bar
    # pag.moveTo(400, 60, duration = 0.2)
    # pag.click()

    # # Type in chatGPT url and hit enter
    # pag.write('https://chat.openai.com')
    # pag.press('enter')
    # time.sleep(2)


    # After logging in:

    # Open browser
    pag.moveTo(80, 1045, duration = 1)
    pag.click()

    # Refresh page
    pag.moveTo(940, 960, duration = 0.6)
    pag.click()
    pag.press('f5')
    time.sleep(2)

    # Click chat box
    pag.moveTo(940, 960, duration = 0.6)
    pag.click()

    # Get user input
    # prompt = input("How are you today?")
    # while len(prompt) >= MAX_PROMPT_LEN:
    #     prompt = input(f"Sorry! Please give me a prompt that is less than {MAX_PROMPT_LEN} characters in length.")

    # Format user input
    # prompt = f"Give consolation to someone who says the following: \"{prompt}\""
    prompt = "Give consolation to someone who says the following: \"I feel lonely and I feel like nobody cares about me.\"" # Manual input
    pag.write(prompt)
    pag.press('enter')

    time.sleep(20)

    pag.moveTo(760, 220, duration = 0.6)
    pag.mouseDown(button='left')
    pag.moveTo(1700, 900, duration = 0.6)
    pag.mouseUp(button='left')

    pag.hotkey('ctrl', 'c')

    # get clipboard data
    win32clipboard.OpenClipboard()
    gpt_response = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    print(gpt_response)