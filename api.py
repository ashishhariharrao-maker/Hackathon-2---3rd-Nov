from fastapi import FastAPI
import pickle

app = FastAPI()

# Load the model once when the application starts
with open('model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)

@app.post("/predict")
async def predict(data: dict):
# Process input data and make predictions using loaded_model
        prediction = loaded_model.predict([list(data.values())])
        return {"prediction": prediction.tolist()}