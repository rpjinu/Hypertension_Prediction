import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load(r'D:\Dawnloads\hypertension_model.pkl')

# Streamlit UI
st.title("🩺 Hypertension Prediction API")
st.write("Enter your details below to predict the risk of hypertension.")

# User Inputs
age = st.number_input("Age", min_value=1, max_value=120, value=30)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
cholesterol = st.number_input("Cholesterol Level", min_value=100, max_value=400, value=200)
systolic_bp = st.number_input("Systolic BP", min_value=80, max_value=200, value=120)
diastolic_bp = st.number_input("Diastolic BP", min_value=50, max_value=130, value=80)
alcohol_intake = st.number_input("Alcohol Intake (drinks per week)", min_value=0.0, max_value=50.0, value=5.0)
diabetes = st.selectbox("Diabetes", ["Yes", "No"])
stress_level = st.slider("Stress Level (1-10)", min_value=1, max_value=10, value=5)
salt_intake = st.number_input("Salt Intake (grams per day)", min_value=0.0, max_value=20.0, value=5.0)
sleep_duration = st.number_input("Sleep Duration (hours per night)", min_value=0.0, max_value=12.0, value=7.0)
heart_rate = st.number_input("Heart Rate (bpm)", min_value=40, max_value=150, value=75)
ldl = st.number_input("LDL Cholesterol", min_value=50, max_value=300, value=100)
hdl = st.number_input("HDL Cholesterol", min_value=20, max_value=100, value=50)
triglycerides = st.number_input("Triglycerides", min_value=50, max_value=500, value=150)
glucose = st.number_input("Glucose Level", min_value=50, max_value=300, value=100)

# Encoding categorical values
encoding_map = {"Diabetes": {"No": 0, "Yes": 1}}
encoded_diabetes = encoding_map["Diabetes"][diabetes]

# Prediction Button
if st.button("Predict Hypertension"):
    input_data = np.array([[age, bmi, cholesterol, systolic_bp, diastolic_bp, alcohol_intake,
                             encoded_diabetes, stress_level, salt_intake, sleep_duration, heart_rate,
                             ldl, hdl, triglycerides, glucose]])
    
    prediction = model.predict(input_data)
    result = "High Hypertension Risk" if prediction[0] == 0 else "Low Hypertension Risk"
    
    st.subheader("🩸 Prediction Result: ")
    st.success(result)
