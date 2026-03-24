# Voice-Pro for Pinokio

[Voice-Pro](https://github.com/abus-aikorea/voice-pro) repacked for [Pinokio](https://pinokio.computer) — 1-click install, no conda required.

This is a repackaged version of ABUS's Voice-Pro AI voice app, modified to run cleanly through Pinokio's launcher system. The original project's conda-based installer has been replaced with Pinokio scripts that handle virtual environments, dependency installation, and GPU setup automatically.

## What changed from the original

- Removed conda-based 1-click installer (`one_click.py`, `start.bat`, `configure.bat`, etc.)
- Created Pinokio launcher scripts (`install.js`, `start.js`, `reset.js`, `update.js`, `pinokio.js`)
- Custom `requirements.txt` with cleaned dependencies (PyTorch handled separately via `torch.js`, cuDNN 8 via conda)
- Removed `modelscope` dependency from CosyVoice (model downloads handled by the app's own HF downloader)
- Made `WeTextProcessing`/`pynini` optional in CosyVoice frontend (not needed when using `text_frontend=False`)
- Stripped Matcha-TTS `utils/__init__.py` to avoid pulling in training-only deps (hydra, lightning, gdown, omegaconf)
- Fixed TTS audio pipeline across all engines (Kokoro, Edge, F5, Azure, CosyVoice) — intermediate wav + pydub trim/convert instead of broken ffmpeg/soundfile chain
- Fixed emoji characters in filenames crashing `os.system()`/`cmd.exe`
- Fixed ffmpeg mp3 encoding (conda's ffmpeg uses `mp3_mf`, not `libmp3lame`)
- Various `logger.error` → `logger.warning` to prevent Pinokio shell auto-kill

## Install

Download through Pinokio or clone this repo into your Pinokio `api` folder and run the install script.

## Credits

All credit for Voice-Pro goes to [ABUS / abus-aikorea](https://github.com/abus-aikorea/voice-pro). This is a repackaging for Pinokio compatibility, licensed under GPL-3.0 per the original project.

---

<details>
<summary>📄 Original Voice-Pro README</summary>

<!-- 
 title: Voice-Pro: Ultimate AI Voice Conversion and Multilingual Translation Tool
 description: Powerful AI-powered web application for YouTube video processing, speech recognition, translation, and text-to-speech with multilingual support
 keywords: AI voice conversion, YouTube translation, subtitle generation, speech-to-text, text-to-speech, voice cloning, multilingual translation, ElevenLabs Alternative 
 author: ABUS
 version: 2.0.0
 last-updated: 2025-02-23
 product-type: AI Multimedia Processing Software
 platforms: Windows
 technology-stack: Whisper, Edge-TTS, Gradio, CUDA, Faster-Whisper, Whisper-Timestamped, WhisperX, E2-TTS, F5-TTS, YouTube Downloader, Demucs, MDX-Net, RVC, CosyVoice, kokoro
 license: LGPL
-->



<h1 align="center">
Voice-Pro
</h1>

<p align="center">
  <i align="center">The best AI speech recognition, translation, and multilingual dubbing solution 🚀</i>
</p>

<h4 align="center">
  <a href="https://deepwiki.com/abus-aikorea/voice-pro">
    <img alt="Ask DeepWiki.com" src="https://deepwiki.com/badge.svg" style="height: 20px;">
  </a>
  <a href="https://www.youtube.com/channel/UCbCBWXuVbk-OBp9T4H5JjAA">
    <img src="https://img.shields.io/badge/youtube-d95652.svg?style=flat-square&logo=youtube" alt="youtube" style="height: 20px;">
  </a>
  <a href="https://www.buymeacoffee.com/abus">
    <img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me a Coffee" style="height: 20px;">
  </a>
  <a href="https://github.com/abus-aikorea/voice-pro/releases">
    <img src="https://img.shields.io/github/v/release/abus-aikorea/voice-pro" alt="release" style="height: 20px;">
  </a>
  <a href="https://github.com/abus-aikorea/voice-pro/stargazers">
    <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/abus-aikorea/voice-pro">
  </a>  
</h4>

<p align="center">
    <img src="docs/images/main_page_crop.eng.jpg?raw=true" alt="Dubbing Studio"/>
</p>
<br />



## 🎙️ An AI-powered web application for speech recognition, translation, and dubbing


<p>  
  <a href="docs/README.kor.md">
    <img src="https://flagcdn.com/16x12/kr.png" alt="South Korea Flag" style="vertical-align: middle;"> 한국어
  </a> ∙ 
  <a href="docs/README.eng.md">
    <img src="https://flagcdn.com/16x12/us.png" alt="United Kingdom Flag" style="vertical-align: middle;"> English
  </a> ∙ 
  <a href="docs/README.zh.md">
    <img src="https://flagcdn.com/16x12/cn.png" alt="China Flag" style="vertical-align: middle;"> 中文简体
  </a> ∙ 
  <a href="docs/README.tw.md">
    <img src="https://flagcdn.com/16x12/tw.png" alt="Taiwan Flag" style="vertical-align: middle;"> 中文繁體
  </a> ∙ 
  <a href="docs/README.jpn.md">
    <img src="https://flagcdn.com/16x12/jp.png" alt="Japan Flag" style="vertical-align: middle;"> 日本語
  </a> ∙ 
  <a href="docs/README.deu.md">
    <img src="https://flagcdn.com/16x12/de.png" alt="Germany Flag" style="vertical-align: middle;"> Deutsch
  </a> ∙ 
  <a href="docs/README.spa.md">
    <img src="https://flagcdn.com/16x12/es.png" alt="Spain Flag" style="vertical-align: middle;"> Español
  </a> ∙ 
  <a href="docs/README.por.md">
    <img src="https://flagcdn.com/16x12/pt.png" alt="Portugal Flag" style="vertical-align: middle;"> Português
  </a>
</p>

Voice-Pro is a state-of-the-art web app that transforms multimedia content creation. It integrates YouTube video downloading, voice separation, speech recognition, translation, and text-to-speech into a single, powerful tool for creators, researchers, and multilingual professionals.
- 🔊 Top-tier speech recognition: **Whisper**, **Faster-Whisper**, **Whisper-Timestamped**, **WhisperX**
- 🎤 Zero-shot voice cloning: **F5-TTS**, **E2-TTS**, **CosyVoice**
- 📢 Multilingual text-to-speech: **Edge-TTS**, **kokoro** (Paid version includes **Azure TTS**)
- 🎥 YouTube processing & audio extraction: **yt-dlp**
- 🌍 Instant translation for 100+ languages: **Deep-Translator** (Paid version includes **Azure Translator**)


A robust alternative to **ElevenLabs**, Voice-Pro empowers podcasters, developers, and creators with advanced voice solutions.

## ⚠️ Please Note
- Due to [WeConnect](https://www.wctokyoseoul.com) development work, Voice-Pro development and updates are not possible for the time being.
- We have made all Voice-Pro code open source and completely free. Voice-Pro can now be freely distributed and modified by anyone.
- It works well on Windows with NVIDIA GPU. Operation on Mac and Linux has not been verified.
- Please leave your requests on the [![GitHub Issues](https://img.shields.io/github/issues/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/issues)  or  [![GitHub Discussions](https://img.shields.io/github/discussions/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/discussions) pages.


## 📰 News & History

<details open>
<summary>version 3.2</summary>

- We have been focusing on [WeConnect](https://www.wctokyoseoul.com) development for the past few months and have not been able to manage Voice-Pro at all. 
- We have decided to open source all Voice-Pro code.
- Voice-Pro is completely free and supports Windows, Mac, Linux.
- [WeConnect](https://www.wctokyoseoul.com) is an application for global cultural exchange.
- Connect with people from all over the world for meaningful cultural exchanges, language learning, and international friendships.

<p align="center">
    <img src="docs/images/Hotpot 0.png?raw=true" alt="ScreenShot 0" width="18%"/>
    <img src="docs/images/Hotpot 1.png?raw=true" alt="ScreenShot 1" width="18%"/>
    <img src="docs/images/Hotpot 2.png?raw=true" alt="ScreenShot 2" width="18%"/>
    <img src="docs/images/Hotpot 3.png?raw=true" alt="ScreenShot 3" width="18%"/>
    <img src="docs/images/Hotpot 4.png?raw=true" alt="ScreenShot 4" width="18%"/>
</p>

</details>


<details>
<summary>version 3.1</summary>

- 🪄 Support for fine-tuned models of **F5-TTS**
- 🌍 Supported languages
  - <img src="https://flagcdn.com/16x12/us.png" alt="United Kingdom Flag" style="vertical-align: middle;"> English & <img src="https://flagcdn.com/16x12/cn.png" alt="China Flag" style="vertical-align: middle;"> Chinese: <a href="https://huggingface.co/SWivid/F5-TTS/tree/main/F5TTS_v1_Base"> SWivid/F5-TTS_v1 </a> 
  - <img src="https://flagcdn.com/16x12/fi.png" alt="Spain Flag" style="vertical-align: middle;"> Finnish: <a href="https://huggingface.co/AsmoKoskinen/F5-TTS_Finnish_Model"> AsmoKoskinen/F5-TTS_Finnish_Model </a> 
  - <img src="https://flagcdn.com/16x12/fr.png" alt="Spain Flag" style="vertical-align: middle;"> French: <a href="https://huggingface.co/RASPIAUDIO/F5-French-MixedSpeakers-reduced"> RASPIAUDIO/F5-French-MixedSpeakers-reduced </a> 
  - <img src="https://flagcdn.com/16x12/in.png" alt="Spain Flag" style="vertical-align: middle;"> Hindi: <a href="https://huggingface.co/SPRINGLab/F5-Hindi-24KHz"> SPRINGLab/F5-Hindi-24KHz </a>  
  - <img src="https://flagcdn.com/16x12/it.png" alt="Spain Flag" style="vertical-align: middle;"> Italian: <a href="https://huggingface.co/alien79/F5-TTS-italian"> alien79/F5-TTS-italian </a>  
  - <img src="https://flagcdn.com/16x12/jp.png" alt="Spain Flag" style="vertical-align: middle;"> Japanese: <a href="https://huggingface.co/Jmica/F5TTS/tree/main/JA_21999120"> Jmica/F5TTS/JA_21999120 </a>  
  - <img src="https://flagcdn.com/16x12/ru.png" alt="Spain Flag" style="vertical-align: middle;"> Russian: <a href="https://huggingface.co/hotstone228/F5-TTS-Russian"> hotstone228/F5-TTS-Russian </a> 
  - <img src="https://flagcdn.com/16x12/es.png" alt="Spain Flag" style="vertical-align: middle;"> Spanish: <a href="https://huggingface.co/jpgallegoar/F5-Spanish"> jpgallegoar/F5-Spanish </a> 
  
</details>

<details>
<summary>version 3.0</summary>

- 🔥 Removed the **AI Cover** feature.  
- 🚀 Added support for **m-bain/whisperX**.
  
</details>

<details>
<summary>version 2.0</summary>

- 🐍 Built with Python 3.10.15, Torch 2.5.1+cu124, and Gradio 5.14.0.  
- 🆓 Free trial supports media up to **60 seconds** in length.  
- 🔥 Added the **AI Cover** feature.  
- 🎤 Introduced support for **CosyVoice** and **kokoro**.  
- ⏳ Initial run downloads **CozyVoice2-0.5B (9GB)**, which may take over an hour depending on network speed.  
- 🎧 Voice samples for cloning will be continuously updated.  
- 📝 Added **spaCy** for natural sentence-by-sentence translation and TTS.  
- ☁️ Subscription version includes **Microsoft Azure** Translator and TTS.  
- 🏪 Subscription offers **unlimited usage** (no 60-second limit) during the subscription period, available via [![Shopify](https://img.shields.io/badge/Shopify-7ab55c.svg?style=flat-square&logo=shopify&logoColor=white)](https://r17wvy-t2.myshopify.com).
  
</details>

## 🎥 YouTube Showcase

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <td style="padding: 10px; border: none;" align="center">
      <a href="https://youtu.be/scC5CicZ6G0" style="text-decoration: none; color: inherit;">
        <img src="https://img.youtube.com/vi/scC5CicZ6G0/hqdefault.jpg" alt="Demo Video 1" width="240" height="135" style="border-radius: 4px;">
        <br>
        <span style="font-size: 16px; font-weight: 600; color: #0f0f0f; line-height: 1.2;">Demo for Voice-Pro (v2.0)</span>
      </a>
    </td>
    <td style="padding: 10px; border: none;" align="center">
      <a href="https://youtu.be/Wfo7vQCD4no" style="text-decoration: none; color: inherit;">
        <img src="https://img.youtube.com/vi/Wfo7vQCD4no/hqdefault.jpg" alt="Demo Video 2" width="240" height="135" style="border-radius: 4px;">
        <br>
        <span style="font-size: 16px; font-weight: 600; color: #0f0f0f; line-height: 1.2;">F5-TTS: Voice Cloning</span>
      </a>
    </td>
    <td style="padding: 10px; border: none;" align="center">
      <a href="https://youtu.be/GOzCDj4MCpo" style="text-decoration: none; color: inherit;">
        <img src="https://img.youtube.com/vi/GOzCDj4MCpo/hqdefault.jpg" alt="Demo Video 3" width="240" height="135" style="border-radius: 4px;">
        <br>
        <span style="font-size: 16px; font-weight: 600; color: #0f0f0f; line-height: 1.2;">Live Transcription & Translation</span>
      </a>
    </td>
    <td style="padding: 10px; border: none;" align="center">
      <a href="https://youtu.be/YdAq80wjtuQ" style="text-decoration: none; color: inherit;">
        <img src="https://img.youtube.com/vi/YdAq80wjtuQ/hqdefault.jpg" alt="Demo Video 4" width="240" height="135" style="border-radius: 4px;">
        <br>
        <span style="font-size: 16px; font-weight: 600; color: #0f0f0f; line-height: 1.2;">Multi-Lingual Voice Cloning: Korean - German</span>
      </a>
    </td>
  </tr>
  <tr>
    <td style="padding: 10px; border: none;" align="center">
      <a href="https://youtu.be/Tu2okoHY174" style="text-decoration: none; color: inherit;">
        <img src="https://img.youtube.com/vi/Tu2okoHY174/hqdefault.jpg" alt="Demo Video 5" width="240" height="135" style="border-radius: 4px;">
        <br>
        <span style="font-size: 16px; font-weight: 600; color: #0f0f0f; line-height: 1.2;">Multi-Lingual Voice Cloning: English - Korean</span>
      </a>
    </td>
    <td style="padding: 10px; border: none;" align="center">
      <a href="https://youtu.be/dWCEwO56_7Y" style="text-decoration: none; color: inherit;">
        <img src="https://img.youtube.com/vi/dWCEwO56_7Y/hqdefault.jpg" alt="Demo Video 6" width="240" height="135" style="border-radius: 4px;">
        <br>
        <span style="font-size: 16px; font-weight: 600; color: #0f0f0f; line-height: 1.2;">Multi-Lingual Voice Cloning: Korean - Japanese</span>
      </a>
    </td>
    <td style="padding: 10px; border: none;" align="center">
      <a href="https://youtu.be/HXomwoKS3V4" style="text-decoration: none; color: inherit;">
        <img src="https://img.youtube.com/vi/HXomwoKS3V4/hqdefault.jpg" alt="Demo Video 7" width="240" height="135" style="border-radius: 4px;">
        <br>
        <span style="font-size: 16px; font-weight: 600; color: #0f0f0f; line-height: 1.2;">NVIDIA RTX Video Super-Resolution</span>
      </a>
    </td>
    <td style="padding: 10px; border: none;" align="center">
      <a href="https://youtu.be/lZK7pLJBHb4" style="text-decoration: none; color: inherit;">
        <img src="https://img.youtube.com/vi/lZK7pLJBHb4/hqdefault.jpg" alt="Demo Video 8" width="240" height="135" style="border-radius: 4px;">
        <br>
        <span style="font-size: 16px; font-weight: 600; color: #0f0f0f; line-height: 1.2;">AI Karaoke</span>
      </a>
    </td>
  </tr>
  <tr>
    <td style="padding: 10px; border: none;" align="center">
      <a href="https://youtu.be/Co70lh95EsQ" style="text-decoration: none; color: inherit;">
        <img src="https://img.youtube.com/vi/Co70lh95EsQ/hqdefault.jpg" alt="Demo Video 5" width="240" height="135" style="border-radius: 4px;">
        <br>
        <span style="font-size: 16px; font-weight: 600; color: #0f0f0f; line-height: 1.2;">Multi-Lingual Voice Cloning: English - Korean</span>
      </a>
    </td>
  </tr>    
</table>


## ⭐ Key Features

### 1. Dubbing Studio
- YouTube video downloads & audio extraction
- Voice separation with **Demucs**
- Supports 100+ languages for speech recognition & translation

### 2. Speech Technologies
- **Speech-to-Text:** **Whisper**, **Faster-Whisper**, **Whisper-Timestamped**, **WhisperX**
- **Text-to-Speech:** 
  - **Edge-TTS**: 100+ languages, 400+ voices
  - **E2-TTS**, **F5-TTS**, **CosyVoice**: Zero-shot cloning
  - **kokoro**: Ranked #2 in HuggingFace TTS Arena

### 3. Real-Time Translation
- Instant speech recognition
- Multilingual translation on the fly
- Customizable audio inputs


## 🤖 WebUI

### `Dubbing Studio` Tab
- All-in-one hub: YouTube downloads, noise removal, subtitles, translation, & TTS
- Supports all ffmpeg-compatible formats
- Output options: WAV, FLAC, MP3
- Subtitles & recognition for 100+ languages
- TTS with speed, volume, & pitch controls
  
<p align="center">
  <img style="width: 90%; height: 90%" src="docs/images/main_page.eng.jpg?raw=true" alt="Multilingual Voice Conversion and Subtitle Generation Web UI Interface"/>
</p>  


### `Whisper Caption` Tab
- Subtitle-focused: 90+ languages
- Video-integrated subtitle display
- Word-level highlighting & denoise options

### `Translate` Tab
- Translation for 100+ languages
- Supports subtitle files (ASS, SSA, SRT, etc.)
- Real-time voice recognition & translation

<p align="center">
  <img style="width: 90%; height: 90%" src="docs/images/live_translation_bbc.jpg?raw=true" alt="WebUI for Real-Time Speech Recognition and Translation"/>
</p>  

### `Speech Generation` Tab
- Options: **Edge-TTS**, **F5-TTS**, **CosyVoice**, **kokoro**
- Celeb voice podcasts & multilingual support

<p align="center">
  <img style="width: 90%; height: 90%" src="docs/images/tts_f5_multi.jpg?raw=true" alt="Podcast Production WebUI Using Voice-Cloning Technology"/>
</p>  


## 💻 System Requirements
- **OS:** Windows 10/11 (64-bit)
- **GPU:** NVIDIA with CUDA 12.4 (recommended)
- **VRAM:** 4GB+ (8GB+ preferred)
- **RAM:** 4GB+
- **Storage:** 20GB+ free space
- **Internet:** Required


## 🙏 Credits
* Voice-Pro: <https://github.com/abus-aikorea/voice-pro>
* Demucs: <https://github.com/facebookresearch/demucs>
* yt-dlp: <https://github.com/yt-dlp/yt-dlp>
* gradio: <https://github.com/gradio-app/gradio>
* edge-TTS: <https://github.com/rany2/edge-tts>
* F5-TTS: <https://github.com/SWivid/F5-TTS.git>
* openai-whisper: <https://github.com/openai/whisper>
* faster-whisper: <https://github.com/SYSTRAN/faster-whisper>
* whisper-timestamped: <https://github.com/linto-ai/whisper-timestamped>
* whisperX: <https://github.com/m-bain/whisperX>
* CosyVoice: <https://github.com/FunAudioLLM/CosyVoice>
* kokoro: <https://github.com/hexgrad/kokoro>
* Deep-Translator: <https://github.com/nidhaloff/deep-translator>
* spaCy: <https://github.com/explosion/spaCy>


## ©️ Copyright
  <img src="docs/images/ABUS-logo.jpg" width="100" height="100"> by [ABUS](https://www.wctokyoseoul.com)

</details>
