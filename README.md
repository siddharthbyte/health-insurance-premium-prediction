# Insurance Premium Prediction

An end-to-end Machine Learning project that predicts annual insurance premiums based on customer demographics, income, medical history, lifestyle, and insurance plan.

## Live Demo

**Try the app:** [Your Streamlit App URL](https://health-insurance-premium-prediction-e9kw77pxjla6msxwfz5fq9.streamlit.app/)

## Project Overview

The goal of this project is to build and deploy a regression model that estimates annual insurance premiums from customer information.

The project covers the complete ML workflow, from exploratory data analysis to model deployment using Streamlit.

## Tech Stack

- Python
- Pandas and NumPy
- Scikit-learn
- XGBoost
- Matplotlib and Seaborn
- Streamlit
- Joblib

## Machine Learning Workflow

1. Data cleaning and exploratory data analysis (EDA)
2. Feature engineering and categorical encoding
3. Train-test split
4. Model training and comparison
5. Cross-validation and evaluation
6. Prediction error analysis
7. Model serialization using Joblib
8. Deployment with Streamlit Community Cloud

## Models Evaluated

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor

XGBoost was selected as the final model based on its performance on the held-out test set.

## Model Performance

Final XGBoost model test-set metrics:

| Metric | Score |
|---|---:|
| MAE | 765.98 |
| RMSE | 1140.36 |
| R² | 0.98154 |

These scores reflect performance on the available test set and do not guarantee the same accuracy on new, real-world insurance data.

## Run Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Basic_ML_project
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv mlenv
.\mlenv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit app

```bash
python -m streamlit run app.py
```

## Disclaimer

This project is for educational and demonstration purposes only. The predicted premium is an experimental ML estimate and is not an official insurance quote or financial advice.