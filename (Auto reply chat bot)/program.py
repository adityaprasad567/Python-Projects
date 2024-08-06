import pyautogui
import pyperclip
import time

# Define the coordinates
icon_x, icon_y = 1328, 1044
drag_start_x, drag_start_y = 606, 255
drag_end_x, drag_end_y = 1226, 902 

# Pause to give you time to switch to the appropriate window
time.sleep(5)  # Adjust the sleep time as needed

# Click on the icon
pyautogui.click(icon_x, icon_y)

# Drag to select text
pyautogui.moveTo(drag_start_x, drag_start_y)
pyautogui.mouseDown()
pyautogui.moveTo(drag_end_x, drag_end_y)
pyautogui.mouseUp()

# Copy the selected text
pyautogui.hotkey('ctrl', 'c')

# Wait a moment to ensure the text is copied
time.sleep(1)  # Adjust as needed

# Retrieve the copied text from the clipboard
copied_text = pyperclip.paste()

# Output the copied text
print("Copied text:", copied_text)
