# Import FastAPI and other modules
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import tensorflow as tf
import numpy as np

# Create an app instance
app = FastAPI()

# Load the ML model
model = tf.keras.models.load_model("model.h5")

# Create a Jinja2 template instance
templates = Jinja2Templates(directory="templates")

# Define the home page route
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    # Render the home page template
    return templates.TemplateResponse("home.html", {"request": request})

# Define the predict route
@app.post("/predict")
async def predict(request: Request):
    # Get the input values from the form
    form_data = await request.form()
    a = float(form_data["a"])
    b = float(form_data["b"])

    # Reshape the input values into a numpy array
    input_data = np.array([[a, b]])

    # Make a prediction using the ML model
    prediction = model.predict(input_data)
    data = prediction

    # Render the result page template with the prediction value
    return templates.TemplateResponse("after_1.html", {"request": request, "data": data})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

