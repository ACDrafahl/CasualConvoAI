# %%
import keyboard
import time
import ipywidgets as widgets
from IPython.display import display
from threading import Thread
from queue import Queue
import json
from vosk import Model, KaldiRecognizer
import pyaudio

p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
    print(p.get_device_info_by_index(i))

p.terminate

CHANNELS = 1
FRAME_RATE = 16000
RECORD_SECONDS = 5
AUDIO_FORMAT = pyaudio.paInt16
SAMPLE_SIZE = 2
INPUT_INDEX = 1

# model = Model(r"C:\Program Files (x86)\Vosk\vosk-model-en-us-0.22") # Advanced model, slowest
model = Model(r"C:\Program Files (x86)\Vosk\vosk-model-en-us-0.22-lgraph") # Graph model, fast
rec = KaldiRecognizer(model, FRAME_RATE)
rec.SetWords(True)

def speech_recognition(output):
    while not messages.empty():
        frames = recordings.get()

        rec.AcceptWaveform(b''.join(frames))
        result = rec.Result()
        text = " " + json.loads(result)["text"]

        output.append_stdout(text + "\n")
        time.sleep(1) #unsure if this is neccessary

def record_microphone(chunk=1024):
    p = pyaudio.PyAudio()

    stream = p.open(format=AUDIO_FORMAT, channels=CHANNELS, rate=FRAME_RATE, input=True, input_device_index=INPUT_INDEX, frames_per_buffer=chunk)

    frames = []

    while not messages.empty():
        data = stream.read(chunk)
        frames.append(data)

        if len(frames) >= (FRAME_RATE * RECORD_SECONDS) / chunk:
            recordings.put(frames.copy())
            frames = []

    stream.stop_stream()
    stream.close()
    p.terminate()

messages = Queue()
recordings = Queue()

output = widgets.Output()

def start_recording(data):
    messages.put(True)

    with output:
        display("Starting...")
        record = Thread(target=record_microphone)
        record.start()

        transcribe = Thread(target=speech_recognition, args=(output,))
        transcribe.start()

def stop_recording(data):
    with output:
        messages.get()
        display("Stopped.")
        print(output)

space_pressed = False

def on_spacebar_press(self):
    global space_pressed
    if not space_pressed:
        start_recording(self)
        space_pressed = True

def on_spacebar_release(self):
    global space_pressed
    if space_pressed:
        stop_recording(self) #this is probably the issue
        space_pressed = False

keyboard.on_press_key('space', on_spacebar_press)
keyboard.on_release_key('space', on_spacebar_release)

# Wait for the 'esc' key to exit the program
keyboard.wait('esc') 

# Unhook the keyboard listener when the program exits
keyboard.unhook_all()


