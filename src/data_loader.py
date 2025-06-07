import pandas as pd
from pathlib import Path

def load_artworks(path=None):
    if path is None:
        path = Path(__file__).parents[1] / "data" / "Artworks.csv"
    return pd.read_csv(path)

def load_artists(path=None):
    if path is None:
        path = Path(__file__).parents[1] / "data" / "Artists.csv"
    return pd.read_csv(path)


def load_artworks_enriched(path=None):
    if path is None:
        path = Path(__file__).parents[1] / "outputs" / "artworks_enriched.csv"
    return pd.read_csv(path)