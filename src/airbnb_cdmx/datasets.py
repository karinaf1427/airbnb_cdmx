"""
Datasets registry for crimedatasets.
"""

DATASETS = {
    "airbnb_cdmx": {
        "filename": "airbnb_cdmx_2024.csv",
        "source": "Kaggle",
        "url": "https://www.kaggle.com/datasets/riverae/airbnb-prices-in-cdmx-2024", 
        "license": "CC0: Public Domain",
        "description": "Airbnb Prices in Mexico from 1924 to 2022."
    },
}

__all__ = ["DATASETS"]