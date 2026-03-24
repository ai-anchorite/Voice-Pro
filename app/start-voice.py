import argparse
import os
import sys
import time
from pathlib import Path

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


from src.config import UserConfig
from app.abus_hf import AbusHuggingFace
from app.abus_genuine import genuine_init
from app.abus_app_voice import create_ui
from app.abus_path import path_workspace_folder, path_gradio_folder


def download_with_retry(file_type, level=0, max_retries=3):
    for attempt in range(1, max_retries + 1):
        try:
            AbusHuggingFace.hf_download_models(file_type=file_type, level=level)
            return
        except Exception as e:
            if attempt < max_retries:
                wait = 5 * attempt
                print(f"Download '{file_type}' failed (attempt {attempt}/{max_retries}): {e}", flush=True)
                print(f"Retrying in {wait}s...", flush=True)
                time.sleep(wait)
            else:
                print(f"Download '{file_type}' failed after {max_retries} attempts: {e}", flush=True)
                print(f"Skipping '{file_type}' - it will be downloaded on next start.", flush=True)


# ABUS - start voice
genuine_init()
AbusHuggingFace.initialize(app_name="voice")

download_with_retry('demucs')
download_with_retry('edge-tts')
download_with_retry('kokoro')
download_with_retry('cosyvoice')

path_workspace_folder()
path_gradio_folder()


user_config_path = os.path.join(Path(__file__).resolve().parent, "app", "config-user.json5")
user_config = UserConfig(user_config_path)

import traceback

try:
    create_ui(user_config=user_config)
except Exception as e:
    print(f"\n\nFATAL ERROR: {e}", flush=True)
    traceback.print_exc()
    sys.exit(1)