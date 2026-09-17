import joblib
from fastapi import FastAPI
import pandas as pd

# initialise the app
app = FastAPI()

# load the saved model
model = joblib.load('titanic_rf_model.pkl')

@app.get("/")
def home():
    return {"message": "Welcome to the Titanic Survival Prediction API."}

# define a prediction route
@app.get("/predict")
def predict_survival(pclass: int, sex: int, age: float, fare: float):
    
    # create a dataframe with the user inputs
    
    input_data = pd.DataFrame(
        [[pclass, sex, age, fare]], columns= ['Pclass', 'Sex', 'Age', 'Fare']
    )
    
    # make prediction
    prediction = model.predict(input_data)
    results = "Survived" if prediction[0] == 1 else "Did not Survive"
    
    return {"Prediction": results}