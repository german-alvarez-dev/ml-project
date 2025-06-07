# MoMA Acquisition Bias Classifier

This project analyzes the acquisition patterns of the Museum of Modern Art (MoMA) using machine learning. The goal is to predict whether an artwork would be acquired based on its metadata, and to investigate possible institutional biases, especially regarding gender, country, and material.

## Project Structure

````
ml-project/
├── notebooks/
│ ├── 01_EDA_artists.ipynb
│ ├── 02_cleaning_artists.ipynb
│ ├── 03_enrichment_artists.ipynb
│ ├── 04_EDA_artworks.ipynb
│ ├── 05_cleaning_artworks.ipynb
│ ├── 06_enrichment_artworks.ipynb
│ ├── 07_classification_model.ipynb
│ ├── 08_model_analysis.ipynb
│ ├── 09_high_value_not_acquired.ipynb
│ └── 10_summary.ipynb
├── outputs/
│ └── (models, predictions, charts, CSVs, etc.)
├── src/
│ └── data_loader.py
├── data/
│ └── (raw MoMA CSV files)
└── README.md
````


## Goals

- Predict artwork acquisitions based on their metadata.
- Detect false negatives (acquired works predicted as not acquired).
- Investigate bias patterns in acquisition decisions.
- Lay the foundation for a critical or curatorial artistic piece.

## Dataset

- Public data from the MoMA GitHub repository: https://github.com/MuseumofModernArt/collection
- Over 260,000 artwork entries and 15,000 artists
- Metadata includes medium, nationality, gender, date, classification, etc.

## Machine Learning Pipeline

- Data cleaning and standardization
- Feature engineering (categorical, boolean, year, country, era, etc.)
- Target: `is_acquired` (1 if the artwork has a `dateAcquired`)
- Model: Random Forest Classifier inside a preprocessing pipeline
- Evaluation and error analysis with a focus on false negatives

## Results

- Accuracy: 98.7% (heavily imbalanced dataset)
- False Negatives: 161
- No high-confidence false negatives (p > 0.80), but many medium-confidence ones
- Most influential features: `year`, `material`, `department`, `classification`

## Bias & Error Analysis

- Gender and country bias were explored by comparing error rates
- USA and photography-related works were among the most common FNs
- Many FNs were part of the Mies van der Rohe Archive, highlighting possible data artifacts or curatorial anomalies

## Outputs

- classifier_pipeline.pkl – Trained model
- X_test.pkl, y_test.pkl, y_pred.pkl – Evaluation data
- false_negatives_all.csv – All FNs with predicted probabilities
- feature_importances.csv – Top features ranked by importance

## Requirements

See `requirements.txt` for dependencies.

Install with:


`pip install -r requirements.txt`



## How to Run

1. Download and place MoMA CSV files into `data/`
2. Run the notebooks sequentially from `01_EDA_artists.ipynb` to `10_summary.ipynb`
3. Outputs will be saved into the `outputs/` folder

## Possible Extensions

- Refine features like `artist_age_at_acquisition`
- Address class imbalance with techniques like SMOTE or undersampling
- Transform results into curatorial or artistic visualizations
- Build a dashboard for public exploration

## Author

Germán Álvarez