import torch
import sys

from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

tts = TTS(model_name="tts_models/en/ek1/tacotron2")
tts.tts_to_file(text="This is a test of the tacotron2 voice, lmao")
