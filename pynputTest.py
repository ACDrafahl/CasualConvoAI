import pynput
import keyboard

def on_press(key):
    if key == pynput.keyboard.Key.space:
        print("The space key is being held down.")

def on_release(key):
    if key == pynput.keyboard.Key.space:
        print("The space key is no longer being held down.")

listener = pynput.keyboard.Listener(
    on_press=on_press,
    on_release=on_release)

listener.start()

keyboard.wait('esc')
