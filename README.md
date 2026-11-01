# 🦜 Parakeet AI — Desktop Assistant Prototype

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform: Cross-Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-emerald.svg)](https://github.com/Classyvaibhav06/parakeet-ai-desktop-prototype)
[![Architecture: Local STT + LLM](https://img.shields.io/badge/AI-Ollama%20%2B%20Local%20STT-violet.svg)](https://ollama.ai)

A lightweight, high-performance desktop application inspired by **Parakeet AI**. Built to run **100% locally on-device**, keeping your voice audio, transcription, and generative intelligence private without transmitting raw voice data over the public internet.

Developed by **Vaibhav Ghoshi** ([Portfolio](https://vaibhav-ghoshi.in) | [GitHub](https://github.com/Classyvaibhav06)) for the **Lacritz.ai** Full Stack Engineering Assessment.

---

## 🌟 Key Features

1. **Native Desktop Window & Intuitive Controls:**
   - Responsive desktop window with dedicated **Start Listening** and **Stop Listening** controls.
   - Live visual audio level meter tracking microphone input.
2. **Real-Time Speech-to-Text (STT) Capture:**
   - Real-time transcription display reflecting live speech.
   - Live editable transcription pane allowing manual review, corrections, or direct input.
3. **Progressive AI Answer Streaming ("Suggest Answer"):**
   - Click **"Suggest Answer"** to generate an AI answer grounded in the transcribed query.
   - **Progressive streaming output:** Tokens are rendered dynamically token-by-token (real-time stream pacing) rather than waiting for full completion.
4. **Local Runtime Execution (Ollama & Embedded Fallback):**
   - Integrates natively with local LLM runtimes such as **Ollama** (`http://127.0.0.1:11434`) supporting models like `llama3.2`, `mistral`, `qwen2.5-coder`, and `phi3`.
   - Built-in embedded fallback inference engine so the application runs seamlessly out-of-the-box even before models are pulled.

---

## 🏗️ Architecture & Component Flow

```
[ Microphone Audio Stream ]
            │
            ▼
[ Local Speech-to-Text Engine ]  ──► Live Real-Time Transcription UI
            │
      (User Clicks "Suggest Answer")
            │
            ▼
[ Local Inference Controller ] ──► Ollama Daemon (`/api/generate` with stream: true)
            │
            ▼
[ Progressive Streaming Pipeline ] ──► SSE / IPC Token Channel ──► Progressive Answer Display
```

---

## 🚀 Quick Start Guide

### Prerequisites
- **Node.js** (v18+) & **npm**
- *(Optional for full model weights)*: [Ollama](https://ollama.ai) installed locally

```bash
# Pull a local lightweight model (optional)
ollama run llama3.2
```

---

### Installation & Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Classyvaibhav06/parakeet-ai-desktop-prototype.git
   cd parakeet-ai-desktop-prototype
   ```

2. **Option A: Run via Desktop Electron Runtime:**
   ```bash
   npm install
   npm start
   ```

3. **Option B: Run via High-Performance Local Server Mode (Any OS/Browser):**
   ```bash
   python3 parakeet_server.py
   # Open http://localhost:8765 in your browser
   ```

---

## 🧪 Automated Testing & Verification

The project includes an automated end-to-end test suite (`test_e2e.py`) validating the desktop UI, STT endpoint, and progressive streaming token chunking:

```bash
python3 test_e2e.py
```

**Test Output:**
```text
✅ Test 1 Passed: Desktop UI served correctly.
✅ Test 2 Passed: Speech-to-Text inference endpoint working.
✅ Test 3 Passed: Progressive LLM stream verified (18 chunks received).
```

---

## 📁 Repository Structure

```
├── main.js                  # Electron desktop application main process & IPC handlers
├── preload.js               # Secure context-bridge IPC layer
├── parakeet_server.py       # Standalone local server with SSE progressive stream pipeline
├── test_e2e.py              # Automated verification test script
├── package.json             # Application dependencies & metadata
└── src/
    ├── index.html           # Desktop interface layout & structure
    ├── styles.css           # Premium dark obsidian linear-grade styling
    └── renderer.js          # Audio recording, live meter, and token streaming logic
```

---

## 📜 License

MIT License. Designed and engineered by **Vaibhav Ghoshi**.
