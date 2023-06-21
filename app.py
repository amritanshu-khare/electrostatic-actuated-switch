from flask import Flask, render_template, request
import pickle
import numpy as np

#model = pickle.load(open('model.pkl', 'rb'))
from tensorflow.keras.models import load_model

model = load_model('model.h5')

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['a']
    data2 = request.form['b']
    arr = np.array([[int(data1), int(data2)]])
    pred = model.predict(arr)
    return render_template('after_1.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)















