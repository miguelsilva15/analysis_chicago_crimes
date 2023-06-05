import joblib
import pandas as pd

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    Domestic: int
    Beat: int
    Ward: int
    Community_Area: int
    Year: int
    dow: int
    month: int
    day: int
    season: int
    # TODO:
    # - Include the preprocessing label encoder, to be more user-friendly.
    Location_Description_encoded: int	

app = FastAPI()

# TODO:
# - Include logs


# Load your trained model
model = joblib.load("/home/msf/Downloads/model.joblib")

@app.post('/predict')
async def predict(item: Item):
    to_predict = pd.DataFrame([item.dict()])
    print(to_predict)
    print(to_predict.shape)
    to_predict = to_predict.rename(columns={'Community_Area': 'Community Area'})
    prediction = model.predict(to_predict)
    # chage the prediction to strings to be more user-friendly.. if thats the case
    return {"prediction": prediction.tolist()}