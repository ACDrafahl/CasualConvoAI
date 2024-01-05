import keyboard
from whisper_mic import WhisperMic
from gpt4all import GPT4All
space_pressed = False

def on_spacebar_press(mic):
    global space_pressed
    global output
    if not space_pressed:
        print("press")
        space_pressed = True
        while keyboard.is_pressed('space'):
            output += mic.listen()
            print(output)
        return output

def on_spacebar_release(model):
    global space_pressed
    global output
    if space_pressed:
        print("release")
        space_pressed = False
        prompt = output
        print("Prompt: " + prompt)
        response = model.generate(prompt=prompt, max_tokens=25, temp=0.7)
        print(response)
        output = ""

def main():
    running = True
    model = GPT4All("mistral-7b-openorca.Q4_0.gguf")
    mic = WhisperMic("base", "cpu", True, False, 300, 2, False, True, "~/.cache/whisper", 1)
    global output
    output = ""
    with model.chat_session():
        keyboard.on_press_key('space', lambda event: on_spacebar_press(mic))
        keyboard.on_release_key('space', lambda event: on_spacebar_release(model))

        keyboard.wait('esc')

if __name__ == "__main__":
    main()

