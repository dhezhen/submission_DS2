import streamlit as st
import joblib
import numpy as np

# Load your trained model
model = joblib.load('model.joblib')

st.title("Prediction App")

# Example: Assume the model expects 3 features as input
st.header("Enter Input Features")
feature1 = st.number_input("Feature 1", value=0.0)
feature2 = st.number_input("Feature 2", value=0.0)
feature3 = st.number_input("Feature 3", value=0.0)

if st.button("Predict"):
    # Prepare input for prediction
    input_data = np.array([[feature1, feature2, feature3]])
    prediction = model.predict(input_data)
    st.success(f"Prediction: {prediction[0]}")