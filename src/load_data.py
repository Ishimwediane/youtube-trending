import pandas as pd
import os

def load_data(filepath):
    # read csv if it exists
    if os.path.exists(filepath):
        return pd.read_csv(filepath)
    else:
        print(f"can't find {filepath}")
        return None
