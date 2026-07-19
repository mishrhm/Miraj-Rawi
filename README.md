# MIRAJ RAWI 🗣️

> **Local • Open Source • Privacy-First • Zero-Shot Voice Cloning**

MIRAJ RAWI is a **fully local**, **free**, and **open-source** instant voice cloning and speech synthesis engine.

As the third project in the **MIRAJ Passion Stack** (alongside **MIRAJ-IMS** and **MIRAJ-Lisaan**), RAWI is designed to bring modern AI voice synthesis capabilities to consumer hardware without relying on cloud services or external APIs.

Using state-of-the-art **zero-shot Text-to-Speech (TTS)** models, RAWI can clone a voice from a clean reference sample as short as **3–10 seconds**, generating natural and expressive speech completely offline.

---

# ✨ Features

- 🎙️ **Zero-Shot Voice Cloning**
  - Clone a voice instantly using a short reference recording.
  - No model training or fine-tuning required.

- 🔒 **100% Local Execution**
  - No cloud APIs.
  - No internet required after model download.
  - Your audio never leaves your machine.

- ⚡ **Hardware Accelerated**
  - Automatic detection of:
    - NVIDIA CUDA GPUs
    - Apple Silicon (MPS)
    - CPU fallback

- 🌍 **Cross-Lingual Speech Synthesis**
  - Generate speech in multiple languages while preserving the cloned voice identity.

- 🛠️ **Open Source**
  - Built entirely with open-source technologies.
  - Designed for experimentation, research, and local AI workflows.

---

# 🏗️ Project Architecture

```
miraj-rawi/
│
├── core/
│   ├── clone_engine.py
│   ├── models/
│   ├── inputs/
│   └── outputs/
│
├── README.md
└── .gitignore
```

---

# 🚀 Roadmap

## ✅ Phase 1 — Local Core Engine

- Zero-shot voice cloning
- Local inference
- Hardware acceleration
- Offline speech synthesis

---

## ⏳ Phase 2 — API Layer

- FastAPI backend
- Async inference
- Audio streaming
- REST endpoints
- WebSocket support

---

## ⏳ Phase 3 — Desktop Workspace

- Voice Lab
- Reference voice manager
- Prompt editor
- Audio preview
- Export tools

---

## ⏳ Phase 4 — Advanced Audio Toolkit

- Voice embedding mixer
- Speech-to-speech conversion
- Timeline editor
- Long-form narration
- Voice design tools

---

# 📋 Requirements

## Software

- Python 3.10+
- Git

## Recommended Hardware

### NVIDIA

- CUDA-compatible GPU
- 8 GB VRAM or higher

### Apple Silicon

- M1
- M2
- M3
- M4

with sufficient unified memory.

CPU-only execution is supported but will be significantly slower.

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/mishrhm/Miraj-Rawi.git

cd miraj-rawi
```

---

## 2. Create the Directory Structure

```bash
mkdir -p core/models
mkdir -p core/inputs
mkdir -p core/outputs
```

---

## 3. Create a Virtual Environment

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

### Windows

```powershell
python -m venv venv

venv\Scripts\activate
```

---

## 4. Install Dependencies

Upgrade pip:

```bash
pip install --upgrade pip
```

Install PyTorch:

```bash
pip install torch torchaudio
```

Install Coqui TTS:

```bash
pip install TTS
```

---

# ▶️ Running the Engine

## Step 1

Place a clean WAV recording inside:

```
core/inputs/
```

Example:

```
core/
└── inputs/
    └── sample_voice.wav
```

Recommended recording:

- WAV format
- 3–10 seconds
- Minimal background noise
- One speaker
- Normal speaking voice

---

## Step 2

Run the engine:

```bash
python core/clone_engine.py
```

---

## Step 3

The generated audio will be saved to:

```
core/outputs/rawi_output.wav
```

---

# 📁 Project Directories

| Directory              | Purpose                  |
| ---------------------- | ------------------------ |
| `core/models/`         | Downloaded model weights |
| `core/inputs/`         | Reference audio samples  |
| `core/outputs/`        | Generated speech         |
| `core/clone_engine.py` | Main inference engine    |

---

# ⚠️ Responsible Use

MIRAJ RAWI is intended for research, education, accessibility, and legitimate creative applications.

Users are solely responsible for how the software is used.

## Voice Consent

Do **not** clone another person's voice without their explicit permission.

Unauthorized voice cloning may violate laws, platform policies, or personal rights depending on your jurisdiction.

## Deepfake Misuse

This software must not be used for:

- Fraud
- Identity theft
- Impersonation
- Social engineering
- Harassment
- Misinformation
- Non-consensual voice replication

## Local Resource Usage

Deep learning inference can consume significant CPU, GPU, VRAM, and system memory.

Ensure your hardware has adequate cooling and available resources during extended generation sessions.

## Third-Party Models

RAWI may use third-party open-source model weights (such as Coqui XTTS). Those models remain subject to their respective licenses and terms of use.

---

# 🤝 Contributing

Contributions are welcome.

Possible areas include:

- Performance optimization
- New TTS backends
- UI improvements
- Documentation
- Bug fixes
- Testing
- Cross-platform support

Feel free to open an issue or submit a pull request.

---

# 📜 License

This project is licensed under the **MIT License**.

```text
MIT License

Copyright (c) 2026 Mishaal Rahman Jannah (MIRAJ)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

# ❤️ MIRAJ Passion Stack

- **MIRAJ-IMS** — Intelligent Memory System
- **MIRAJ-Lisaan** — Local Lightweight Dubbing Intelligence System
- **MIRAJ RAWI** — Local Voice Cloning & Speech Synthesis

Together, these projects aim to build a fully local, privacy-first AI ecosystem powered entirely on consumer hardware.
