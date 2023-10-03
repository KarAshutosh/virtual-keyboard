import tkinter as tk
import pyautogui
import time

def delay(seconds):
    time.sleep(seconds)

def type_character(character):
    # Get the current cursor position
    x, y = pyautogui.position()
    
    # Simulate typing the character at the cursor position
    pyautogui.click(x, y)
    pyautogui.typewrite(character)

def backspace():
    # Simulate pressing the backspace key
    delay(2)
    pyautogui.press('backspace')

def enter():
    # Simulate pressing the enter key
    delay(2)
    pyautogui.press('enter')

def exit_keyboard(root):
    # Close the virtual keyboard
    root.destroy()

def create_virtual_keyboard():
    def switch_to_special_keyboard():
        # Destroy the current keyboard and create a special keyboard
        root.destroy()
        create_special_keyboard()

    root = tk.Tk()
    root.title("Virtual Keyboard")
    
    # Make the virtual keyboard window always on top
    root.wm_attributes('-topmost', 1)

    # Define a grid of buttons for the virtual keyboard
    keyboard_layout = [
        ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
        ['Z', 'X', 'C', 'V', 'B', 'N', 'M'],
        ['Backspace', 'Enter', 'Show special', 'Exit']
    ]

    for row in keyboard_layout:
        key_frame = tk.Frame(root)
        key_frame.pack()
        for key in row:
            if key == 'Backspace':
                tk.Button(key_frame, text=key, width=7, height=2, command=backspace).pack(side=tk.LEFT)
            elif key == 'Enter':
                tk.Button(key_frame, text=key, width=7, height=2, command=enter).pack(side=tk.LEFT)
            elif key == 'Show special':
                tk.Button(key_frame, text=key, width=12, height=2, command=switch_to_special_keyboard).pack(side=tk.LEFT)
            elif key == 'Exit':
                tk.Button(key_frame, text=key, width=7, height=2, command=lambda r=root: exit_keyboard(r)).pack(side=tk.LEFT)
            else:
                tk.Button(key_frame, text=key, width=3, height=2, command=lambda k=key: type_character(k)).pack(side=tk.LEFT)

    root.mainloop()

def create_special_keyboard():
    def switch_to_standard_keyboard():
        # Destroy the special keyboard and create the standard keyboard
        root.destroy()
        create_virtual_keyboard()

    root = tk.Tk()
    root.title("Special Keyboard")
    
    # Make the special keyboard window always on top
    root.wm_attributes('-topmost', 1)

    # Define a grid of buttons for the special keyboard
    special_layout = [
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
        ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')'],
        ['-', '_', '+', '=', '{', '}', '[', ']', '/', '\\'],
        ['Close Screen', 'Switch to Standard']
    ]

    for row in special_layout:
        key_frame = tk.Frame(root)
        key_frame.pack()
        for key in row:
            if key == 'Close Screen':
                tk.Button(key_frame, text=key, width=12, height=2, command=lambda r=root: exit_keyboard(r)).pack(side=tk.LEFT)
            elif key == 'Switch to Standard':
                tk.Button(key_frame, text=key, width=12, height=2, command=switch_to_standard_keyboard).pack(side=tk.LEFT)
            else:
                tk.Button(key_frame, text=key, width=3, height=2, command=lambda k=key: type_character(k)).pack(side=tk.LEFT)

    root.mainloop()

if __name__ == "__main__":
    create_virtual_keyboard()
