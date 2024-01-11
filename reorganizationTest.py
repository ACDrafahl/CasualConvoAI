import os
import subprocess
import tkinter as tk

import keyboard
import sounddevice as sd
import soundfile as sf

from whisper_mic import WhisperMic
from gpt4all import GPT4All

class SpeechSynthesizer:
    def __init__(self, piper_exe_path, onnx_path, json_path, speech_output):
        self.base_command = f'{piper_exe_path} -m {onnx_path} -c {json_path} -f {speech_output}'
        self.speech_output = speech_output

    def generate_speech_command(self, text):
        return f'echo "{text}" | {self.base_command}'

    def speak(self, text):
        speak_command = self.generate_speech_command(text)

        try:
            subprocess.run(speak_command, check=True, shell=True)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")

        data, fs = sf.read(self.speech_output, dtype='float32')
        sd.play(data, fs)

    def purge_old_output(self):
        if os.path.exists(self.speech_output):
            os.remove(self.speech_output)

class SpeechController:
    def __init__(self, model, mic, speech_synthesizer):
        self.model = model
        self.mic = mic
        self.speech_synthesizer = speech_synthesizer
        self.space_pressed = False
        self.output = ""

    def on_spacebar_press(self):
        if not self.space_pressed:
            print("press")
            self.space_pressed = True
            while keyboard.is_pressed('space'):
                self.output += self.mic.listen()
                print(self.output)
            return self.output

    def on_spacebar_release(self):
        if self.space_pressed:
            print("release")
            self.space_pressed = False
            prompt = self.output
            print("Prompt: " + prompt)
            response = self.model.generate(prompt=prompt, max_tokens=25, temp=0.7)
            self.speech_synthesizer.speak(response)
            print(response)
            self.output = ""

def main():
    # Define the complete path to the piper.exe executable
    PIPER_EXE_PATH = 'C:\\Users\\acdga\\.cache\\piper\\piper.exe'
    # define the complete path to the onnx model file
    ONNX_PATH = 'C:\\Users\\acdga\\.cache\\piper\\en_US-kusal-medium.onnx'
    # define the complete path to the json config file
    JSON_PATH = 'C:\\Users\\acdga\\.cache\\piper\\en_en_US_kusal_medium_en_US-kusal-medium.onnx.json'
    # define the output file name
    SPEECH_OUTPUT = 'speechOutput.wav'

    speech_synthesizer = SpeechSynthesizer(PIPER_EXE_PATH, ONNX_PATH, JSON_PATH, SPEECH_OUTPUT)
    speech_synthesizer.purge_old_output()
    model = GPT4All("mistral-7b-openorca.Q4_0.gguf")
    mic = WhisperMic("base", "cpu", True, False, 300, 2, False, True, "~/.cache/whisper", 1)

    speech_controller = SpeechController(model, mic, speech_synthesizer)

    with model.chat_session():
        keyboard.on_press_key('space', lambda event: speech_controller.on_spacebar_press())
        keyboard.on_release_key('space', lambda event: speech_controller.on_spacebar_release())

        keyboard.wait('esc')

if __name__ == "__main__":
    main()
