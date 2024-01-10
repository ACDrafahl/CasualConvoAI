import keyboard
import os
import subprocess
import sounddevice as sd
import soundfile as sf
import tkinter as tk
from whisper_mic import WhisperMic
from gpt4all import GPT4All

space_pressed = False

# define the complete path to the piper.exe executable
piper_exe_path = 'C:\\Users\\acdga\\.cache\\piper\\piper.exe'
# define the complete path to the onnx model file
onnx_path = 'C:\\Users\\acdga\\.cache\\piper\\en_US-kusal-medium.onnx'
# define the complete path to the json config file
json_path = 'C:\\Users\\acdga\\.cache\\piper\\en_en_US_kusal_medium_en_US-kusal-medium.onnx.json'
# define the output file name
speechOutput = 'speechOutput.wav'
# define the rest of the command without the text
base_command = f'{piper_exe_path} -m {onnx_path} -c {json_path} -f {speechOutput}' # There may be a way to use this without loading in the voice every time

def on_spacebar_press(root, mic):
    global space_pressed
    global output
    if not space_pressed:
        print("press")
        space_pressed = True
        while keyboard.is_pressed('space'):
            output += mic.listen()
            print(output)
            text_window(root, "Testing, testing, 1-2-3")
        return output

def on_spacebar_release(model):
    global space_pressed
    global output
    if space_pressed:
        print("release")
        space_pressed = False
        prompt = output
        print("Prompt: " + prompt)
        response = model.generate(prompt=prompt, max_tokens=100, temp=0.7)
        speech(response)
        print(response)
        output = ""

def speech(text):
    # combine the base command and the dynamically changing text
    speak = f'echo "{text}" | {base_command}'

    # run the speech synthesis command in the console
    try:
        subprocess.run(speak, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    
    # extract data and sampling rate from file 
    data, fs = sf.read(speechOutput, dtype='float32')  
    sd.play(data, fs)
    # status = sd.wait()  # Wait until file is done playing

def main():
    # purging old output, might be causing problems. 
    if os.path.exists("output.wav"):
        os.remove("output.wav")
    model = GPT4All("mistral-7b-openorca.Q4_0.gguf")
    mic = WhisperMic("base", "cpu", True, False, 300, 2, False, True, "~/.cache/whisper", 1)
    global output
    output = ""
    with model.chat_session():
        keyboard.on_press_key('space', lambda event: on_spacebar_press(root, mic))
        keyboard.on_release_key('space', lambda event: on_spacebar_release(model))

        keyboard.wait('esc')

if __name__ == "__main__":
    main()