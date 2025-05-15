import os
from pathlib import Path

# Root
ROOT_DIR = Path(__file__).parent.absolute()

# Data
DATA_DIR = ROOT_DIR / "datasets"
TEXT_DATA_DIR = DATA_DIR
LIKELIHOOD_DATA_DIR = DATA_DIR / "likelihood"

# logging
LOG_DIR = ROOT_DIR / "codes" / "log"
LOG_LIKELIHOOD_DIR = LOG_DIR / "likelihood"

# makesure directories exist
os.makedirs(TEXT_DATA_DIR, exist_ok=True)
os.makedirs(LIKELIHOOD_DATA_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(LOG_LIKELIHOOD_DIR, exist_ok=True)


def get_texts_path(dataset_name):
    return TEXT_DATA_DIR / f"{dataset_name}.jsonl"

def get_likelihood_dir(dataset_name):
    path = LIKELIHOOD_DATA_DIR / dataset_name
    os.makedirs(path, exist_ok=True)
    return path

def get_log_likelihood_dir():
    return LOG_LIKELIHOOD_DIR