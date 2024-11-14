import streamlit as st
import pickle
import pandas as pd

with open('gender_classification_model.pkl', 'rb') as file:
    model = pickle.load(file)

def predict_gender(features):
    prediction = model.predict([features])
    return "Male" if prediction[0] == 1 else "Female"

st.title("Gender Classification Model")
st.markdown("### Classify gender based on facial features")
st.write("This model predicts gender based on physical features. Adjust the parameters below and click 'Predict Gender'.")

st.markdown("""
    <style>
        .stRadio > div { flex-direction: row; }
        .stSlider > div { padding: 0.5rem; }
        .section-header { font-size: 1.25em; font-weight: bold; margin-top: 1rem; color: #4A90E2; }
    </style>
    """, unsafe_allow_html=True)


st.markdown('<div class="section-header">Hair and Face</div>', unsafe_allow_html=True)
long_hair = st.radio("Long Hair", ("Yes", "No"), help="Select 'Yes' if the person has long hair.")
long_hair = 1 if long_hair == "Yes" else 0

forehead_width_cm = st.slider("Forehead Width (cm)", min_value=10.0, max_value=20.0, step=0.1, help="Adjust the width of the forehead in centimeters.")
forehead_height_cm = st.slider("Forehead Height (cm)", min_value=5.0, max_value=15.0, step=0.1, help="Adjust the height of the forehead in centimeters.")

st.markdown('<div class="section-header">Nose Features</div>', unsafe_allow_html=True)
nose_wide = st.radio("Wide Nose", ("Yes", "No"), help="Select 'Yes' if the nose is wide.")
nose_wide = 1 if nose_wide == "Yes" else 0

nose_long = st.radio("Long Nose", ("Yes", "No"), help="Select 'Yes' if the nose is long.")
nose_long = 1 if nose_long == "Yes" else 0

st.markdown('<div class="section-header">Lip Features</div>', unsafe_allow_html=True)
lips_thin = st.radio("Thin Lips", ("Yes", "No"), help="Select 'Yes' if the lips are thin.")
lips_thin = 1 if lips_thin == "Yes" else 0

distance_nose_to_lip_long = st.radio("Long Distance from Nose to Lip", ("Yes", "No"), help="Select 'Yes' if the distance between the nose and lip is long.")
distance_nose_to_lip_long = 1 if distance_nose_to_lip_long == "Yes" else 0

# Prediction Button
if st.button("Predict Gender"):
    features = [long_hair, forehead_width_cm, forehead_height_cm, nose_wide, nose_long, lips_thin, distance_nose_to_lip_long]
    prediction = predict_gender(features)
    st.success(f"The Predicted Gender is: **{prediction}**")
