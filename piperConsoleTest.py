import subprocess

# Define the complete path to the piper.exe executable
piper_exe_path = 'C:\\Users\\acdga\\.cache\\piper\\piper.exe'

# Define the complete path to the onnx model file
onnx_path = 'C:\\Users\\acdga\\.cache\\piper\\en_US-kusal-medium.onnx'

# Define the complete path to the json config file
json_path = 'C:\\Users\\acdga\\.cache\\piper\\en_en_US_kusal_medium_en_US-kusal-medium.onnx.json'

# Define the output file name
output = 'output.wav'

# Define the rest of the command without the text
base_command = f'{piper_exe_path} -m {onnx_path} -c {json_path} -f {output}'

# Replace this with the text you want to use dynamically
custom_text = "Hi there. I'm Bradley. I love you!"

# Combine the base command and the dynamically changing text
speak = f'echo "{custom_text}" | {base_command}'

try:
    subprocess.run(speak, check=True, shell=True)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")

# Working commands:
# echo "This is a test"  | .\piper.exe -m .\en_US-kusal-medium.onnx -c en_en_US_kusal_medium_en_US-kusal-medium.onnx.json -f test.wav          

# echo "This is an additional test!"  | C:\Users\acdga\.cache\piper\piper.exe -m C:\Users\acdga\.cache\piper\en_US-kusal-medium.onnx -c C:\Users\acdga\.cache\piper\en_en_US_kusal_medium_en_US-kusal-medium.onnx.json -f test.wav                