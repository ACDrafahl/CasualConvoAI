import json
from vosk import Model, KaldiRecognizer
import pyaudio
# model = Model(r"C:\Program Files (x86)\Vosk\vosk-model-en-us-0.22")

model = Model(r"C:\Program Files (x86)\Vosk\vosk-model-en-us-0.22-lgraph")
recognizer = KaldiRecognizer(model, 16000)
mic = pyaudio.PyAudio()
stream = mic.open(format = pyaudio.paInt16, channels = 1, rate = 16000, input = True, frames_per_buffer = 8192)
stream.start_stream()


def UserInput(): 
    print("Mic is hot!")
    while True:
        input = stream.read(4096, exception_on_overflow=False)
        if len(input) == 0:
            break
        if recognizer.AcceptWaveform(input):
            text = json.loads(recognizer.Result())["text"]
            print("Heard: " + text)
            return text
        
if __name__ == '__main__':
    UserInput()