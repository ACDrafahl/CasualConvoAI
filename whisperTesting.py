import keyboard
import subprocess
import sounddevice as sd
import soundfile as sf
from whisper_mic import WhisperMic
from gpt4all import GPT4All

space_pressed = False

# Define the complete path to the piper.exe executable
piper_exe_path = 'C:\\Users\\acdga\\.cache\\piper\\piper.exe'
# Define the complete path to the onnx model file
onnx_path = 'C:\\Users\\acdga\\.cache\\piper\\en_US-kusal-medium.onnx'
# Define the complete path to the json config file
json_path = 'C:\\Users\\acdga\\.cache\\piper\\en_en_US_kusal_medium_en_US-kusal-medium.onnx.json'
# Define the output file name
speechOutput = 'speechOutput.wav'
# Define the rest of the command without the text
base_command = f'{piper_exe_path} -m {onnx_path} -c {json_path} -f {speechOutput}'

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
        speech(response)
        print(response)
        output = ""

def speech(text):
    # Combine the base command and the dynamically changing text
    speak = f'echo "{text}" | {base_command}'

    # Run the speech synthesis command in the console
    try:
        subprocess.run(speak, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    
    # Extract data and sampling rate from file 
    data, fs = sf.read(speechOutput, dtype='float32')  
    sd.play(data, fs)
    # status = sd.wait()  # Wait until file is done playing

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