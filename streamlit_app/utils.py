import streamlit as st
from pathlib import Path
import pandas as pd

# Définir le répertoire de sortie
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"

#Fonction cache pour charger les fichiers parquet
@st.cache_data
def load_parquet_data(file_name):
    file_path = OUTPUT_DIR / file_name
    return pd.read_parquet(file_path)

