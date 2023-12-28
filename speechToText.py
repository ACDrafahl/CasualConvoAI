import json
from vosk import Model, KaldiRecognizer
import pyaudio
model = Model(r"C:\Program Files (x86)\Vosk\vosk-model-en-us-0.22")
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format = pyaudio.paInt16, channels = 1, rate = 16000, input = True, frames_per_buffer = 8192)
stream.start_stream()

print("Running!")
while True:
    input = stream.read(4096)
    if recognizer.AcceptWaveform(input):
        text = json.loads(recognizer.Result())["text"]
        print(text)