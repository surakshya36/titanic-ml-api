# titanic-ml-api

# Titanic Survival Prediction API 🚢

An end-to-end Machine Learning project that predicts whether a passenger survived the Titanic disaster based on socio-economic status, age, gender, and ticket fare. Built with Python, Scikit-Learn, and FastAPI.

---

## 📊 Data Source
The dataset used for this project is sourced from the famous **Kaggle Competition**: 
- [Kaggle - Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic/data)
- Files used: `train.csv` (training data) and `test.csv` (evaluation data).

---

## 🚀 Features
- **Data Cleaning & Preprocessing:** Handled missing values (median imputation for age) and encoded categorical data using Pandas.
- **Machine Learning Models:** Trained classification models (**Logistic Regression** & **Random Forest**) to predict survival.
- **Backend API:** Deployed the trained model using **FastAPI** with automatic interactive documentation (Swagger UI).

---

## 🛠️ Tech Stack
- **Python** (Pandas, Scikit-Learn, Joblib)
- **FastAPI** (for API deployment)
- **Uvicorn** (ASGI server)
- **Git & GitHub** (Version control)

---

## 📂 Project Structure
```text
titanic/
│
├── train.csv                # Raw Titanic training dataset
├── test.csv                 # Test dataset
├── gender_submission.csv    # Sample submission file
├── survival.ipynb           # Jupyter Notebook (EDA & Model Training)
├── titanic_rf_model.pkl     # Saved Random Forest model
├── app.py                   # FastAPI backend application
└── README.md                # Project documentation
```

## ⚙️ How to Set Up and Run Locally

Follow these steps to run the project on your local machine (tested on Ubuntu/Linux):

### 1. Clone the repository
```bash
git clone https://github.com/YOUR-USERNAME/titanic-ml-api.git
cd titanic-ml-api
```
### 2.  Create and activate a virtual environment
```bash
python3 -m venv titanic_env
source titanic_env/bin/activate
```
### 3.  Install dependencies
```bash
pip install fastapi uvicorn scikit-learn pandas joblib
```
### 4. Run the FastAPI server
```bash
uvicorn app:app --reload
```
### 5. Test the API
Open your browser and navigate to the interactive Swagger UI:
```bash
http://127.0.0.1:8000/docs
```


