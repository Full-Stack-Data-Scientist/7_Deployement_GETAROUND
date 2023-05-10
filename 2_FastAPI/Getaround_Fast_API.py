from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import uvicorn
from joblib import load
import numpy as np

description = """
The 'Getaround API' have been created to help you suggest optimum prices to car owners using Machine Learning. 

Check out the documentation below to learn more on how to use the endpoint.

## ✔️ MACHINE LEARNING
* `/predict` the optimal price for a given set of parameters

Check out documentation for more information on each endpoint. 
"""

tags_metadata = [
    {
        "name": "MACHINE LEARNING",
        "description": "Endpoints that uses our Machine Learning model to suggest the optimal prices"
    }, 
    
]

app = FastAPI(
    title =" 🚖 GETAROUND API - 📊 PRICING OPTIMIZATION MACHINE LEARNING",
    description = description,
    version = "0.1",
    openapi_tags=tags_metadata
)

class PredictionFeatures(BaseModel):
    model_key : str = "Citroën"
    mileage : int = 141512
    engine_power : int = 100
    fuel : str = "diesel"
    paint_color : str = "black"
    car_type : str = "estate"
    private_parking_available : bool = True
    has_gps : bool = True
    has_air_conditioning : bool  = True
    automatic_car : bool = True
    has_getaround_connect : bool = True
    has_speed_regulator : bool = True
    winter_tires : bool = True


@app.get("/", tags = ["ENDPOINT INFORMATION"])
async def index():
    information = "Dear user, In order to use our API, please make sure to check the documentation page located at '/docs' or use the following link: https://getaround-fastapi-ml.herokuapp.com/docs Thank you!"
    return information

@app.post("/predict", tags=["MACHINE LEARNING"])
async def predict(predictionFeatures: PredictionFeatures):
    """
    Please make sure to give this endpoint all columns values as a dictionnary.
    """

    df = pd.DataFrame(dict(predictionFeatures), index = [0])
    preprocessing = load('preprocessor.joblib')
    model = load('LinearRegressionModel.joblib')

    X = preprocessing.transform(df)
    prediction = model.predict(X)

   
    # Format response
    response = {"The suggested optimum price for this rental is": round(prediction.tolist()[0], 2)}
    return response


if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=4000, debug=True, reload=True)