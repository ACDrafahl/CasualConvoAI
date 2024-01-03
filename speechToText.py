import json
from vosk import Model, KaldiRecognizer
import pyaudio
import keyboard
# model = Model(r"C:\Program Files (x86)\Vosk\vosk-model-en-us-0.22") # Advanced model, slowest
model = Model(r"C:\Program Files (x86)\Vosk\vosk-model-en-us-0.22-lgraph") # Graph model, fast
recognizer = KaldiRecognizer(model, 16000)
mic = pyaudio.PyAudio()
stream = mic.open(format = pyaudio.paInt16, channels = 1, rate = 16000, input = True, frames_per_buffer = 8192)
stream.start_stream()

def UserInput(): 
    text = ""
    while True:
        keyboard.wait('space')
        print("Mic is hot!")
        while keyboard.is_pressed('space'):
            input = stream.read(4096, exception_on_overflow=False)
            if len(input) == 0:
                break
            if recognizer.AcceptWaveform(input):
                text += json.loads(recognizer.Result())["text"]
        print("Heard: " + text)
    # return text
        
if __name__ == '__main__':
    UserInput()