import pandas as pd
import os

def ensure_folder(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

def save_to_csv(data, filepath):
    ensure_folder(filepath)
    df = pd.DataFrame(data)
    df.to_csv(filepath, index=False)
