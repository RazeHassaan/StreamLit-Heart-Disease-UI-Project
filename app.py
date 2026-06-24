import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("❤️ Heart Disease Prediction App")

st.write("Enter patient information below:")

# Input fields
age = st.number_input("Age", min_value=1, max_value=120, value=40)
sex = st.selectbox("Sex", ["Female", "Male"])
cp = st.number_input("Chest Pain Type", value=0)
trestbps = st.number_input("Resting Blood Pressure", value=120)
chol = st.number_input("Cholesterol", value=200)
fbs = st.number_input("Fasting Blood Sugar", value=0)
restecg = st.number_input("Resting ECG", value=0)
thalach = st.number_input("Maximum Heart Rate", value=150)
exang = st.number_input("Exercise Induced Angina", value=0)
oldpeak = st.number_input("Oldpeak", value=1.0)
slope = st.number_input("Slope", value=0)
ca = st.number_input("Number of Major Vessels", value=0)
thal = st.number_input("Thal", value=1)

# Convert sex to numeric
sex = 1 if sex == "Male" else 0

if st.button("Predict"):

    features = np.array([
        age, sex, cp, trestbps, chol,
        fbs, restecg, thalach, exang,
        oldpeak, slope, ca, thal
    ]).reshape(1, -1)

    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("⚠️ Heart Disease Detected")
    else:
        st.success("✅ No Heart Disease Detected")
