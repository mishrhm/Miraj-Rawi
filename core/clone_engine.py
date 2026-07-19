import os
import sys

# --- PYTORCH 2.6+ COMPATIBILITY PATCH ---
# Coqui TTS uses custom class configurations that PyTorch's new default 
# 'weights_only=True' security filter blocks. We safely bypass this local block.
import torch
from functools import partial
torch.load = partial(torch.load, weights_only=False)
# ----------------------------------------

from TTS.api import TTS

def init_engine():
    print("Initializing MIRAJ RAWI Core Engine...")
    
    # Auto-detect local compute acceleration hardware
    if torch.cuda.is_available():
        device = "cuda"
        print("--> Hardware acceleration found: NVIDIA CUDA Enabled.")
    elif torch.backends.mps.is_available():
        device = "mps"
        print("--> Hardware acceleration found: Apple Silicon MPS Enabled.")
    else:
        device = "cpu"
        print("--> WARNING: No hardware acceleration found. Running on slow CPU mode.")
        
    # Load the multi-lingual zero-shot cloning model
    model_name = "tts_models/multilingual/multi-dataset/xtts_v2"
    
    print(f"Loading {model_name} onto device: {device}...")
    
    # Implicitly bypass any remaining legacy licensing prompts
    os.environ["COQUI_TOS_AGREED"] = "1"
    
    tts = TTS(model_name).to(device)
    return tts

def run_voice_clone(tts_instance, text, reference_audio_path, output_path, language="en"):
    if not os.path.exists(reference_audio_path):
        raise FileNotFoundError(f"Reference voice clip not found at: {reference_audio_path}")
        
    print(f"\nProcessing Speech Synthesis...")
    print(f"Target Text: \"{text}\"")
    print(f"Cloning Profile: {reference_audio_path}")
    
    # Run zero-shot generation matching the reference speaker's embeddings
    tts_instance.tts_to_file(
        text=text,
        speaker_wav=reference_audio_path,
        language=language,
        file_path=output_path
    )
    print(f"✓ Audio successfully synthesized! Saved to: {output_path}")

if __name__ == "__main__":
    REF_AUDIO = "core/inputs/sample_voice.wav" 
    OUT_AUDIO = "core/outputs/rawi_output.wav"
    TEST_TEXT = "Welcome to Miraj Rawi. This is the third entry to my passion stack, running completely locally on open source technology."
    
    try:
        # 1. Initialize and load model to local GPU/MPS
        engine = init_engine()
        
        # 2. Execute a test clone if an input sample exists
        if os.path.exists(REF_AUDIO):
            run_voice_clone(engine, TEST_TEXT, REF_AUDIO, OUT_AUDIO)
        else:
            print(f"\n[Ready] Core engine successfully loaded. To test a clone, drop a 5-10s voice clip at '{REF_AUDIO}' and rerun this script.")
            
    except Exception as e:
        print(f"\n[Execution Error] Engine initialization or synthesis failed: {str(e)}")