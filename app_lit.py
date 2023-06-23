import streamlit as st
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from streamlit.components.v1 import html

# Load the ML model
model = load_model('model.h5')

def main():
    st.title('ML Model App')
    
    # # Load and render the home.html template
    # with open('templates/home.html', 'r') as file:
    #     home_html = file.read()
    # html_temp = f'<div>{home_html}</div>'
    # #html(html_temp, height=300)

    # Get input values from user
    voltage = st.number_input('Voltage')
    force = st.number_input('Force')
    
    # code for Prediction
    result = ''


    if st.button('Predict'):
        # Perform classification
        data = np.array([[force, voltage]])
        pred = model.predict(data)
        result = pred[0]
        
        if result<=0.3:
            #print("Open Circuit")
            outcome =  'Open Circuit'
        if result>0.3:
            #print("Closed Circuit")
            outcome = 'Closed Circuit'
        # else :
        #     print("There is some problem")
        
        st.success(outcome)
        #Load and render the after_1.html template with the prediction result

        # with open('templates/after_1.html', 'r') as file:
        #     after_html = file.read()
        # after_temp = f"<div>{after_html}</div>"
        # rendered_html = after_temp.replace("{%if data <= 0.3%}", "{%if data <= 0.3%}".replace("data", str(result)))
        # html(rendered_html, height=300)
        
if __name__ == "__main__":
    main()
