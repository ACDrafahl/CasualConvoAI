import keyboard
from whisper_mic import WhisperMic
space_pressed = False

def on_spacebar_press(self):
    global space_pressed
    global output
    if not space_pressed:
        print("press")
        space_pressed = True
        while keyboard.is_pressed('space'):
            output += mic.listen()
            print(output)

def on_spacebar_release(self):
    global space_pressed
    global output
    if space_pressed:
        print("release")
        space_pressed = False
        print("Final: " + output)
        output = ""

def main():
    running = True
    global mic, output
    mic = WhisperMic("base", "cpu", True, False, 300, 2, False, True, "~/.cache/whisper", 1)
    output = ""
    keyboard.on_press_key('space', on_spacebar_press)
    keyboard.on_release_key('space', on_spacebar_release)

    keyboard.wait('esc')

if __name__ == "__main__":
    main()

