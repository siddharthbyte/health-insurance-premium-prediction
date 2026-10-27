
import streamlit as st
import pandas as pd
import joblib

# Load trained model pipeline
model = joblib.load("insurance_premium_model.pkl")

st.set_page_config(
    page_title="Insurance Premium Predictor",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ Insurance Premium Predictor")
st.write(
    "Enter the customer details below to estimate their annual insurance premium."
)

# Customer inputs
age = st.number_input("Age", min_value=18, max_value=100, value=30)

gender = st.selectbox("Gender", ["Male", "Female"])

region = st.selectbox(
    "Region",
    ["Southeast", "Southwest", "Northwest", "Northeast"]
)

marital_status = st.selectbox(
    "Marital Status",
    ["Unmarried", "Married"]
)

number_of_dependants = st.selectbox(
    "Number of Dependants",
    [0, 1, 2, 3, 4, 5]
)

bmi_category = st.selectbox(
    "BMI Category",
    ["Normal", "Overweight", "Underweight", "Obesity"]
)

smoking_status = st.selectbox(
    "Smoking Status",
    ["No Smoking", "Occasional", "Regular"]
)

employment_status = st.selectbox(
    "Employment Status",
    ["Salaried", "Freelancer", "Self-Employed"]
)

income_lakhs = st.number_input(
    "Annual Income (in lakhs)",
    min_value=1,
    max_value=100,
    value=10
)

medical_history = st.selectbox(
    "Medical History",
    [
        "No Disease",
        "Diabetes",
        "High blood pressure",
        "Thyroid",
        "Heart disease",
        "Diabetes & High blood pressure",
        "High blood pressure & Heart disease",
        "Diabetes & Thyroid",
        "Diabetes & Heart disease"
    ]
)

insurance_plan = st.selectbox(
    "Insurance Plan",
    ["Bronze", "Silver", "Gold"]
)

if st.button("Predict Annual Premium", type="primary"):
    input_data = pd.DataFrame([{
        "age": age,
        "gender": gender,
        "region": region,
        "marital_status": marital_status,
        "number_of_dependants": number_of_dependants,
        "bmi_category": bmi_category,
        "smoking_status": smoking_status,
        "employment_status": employment_status,
        "income_lakhs": income_lakhs,
        "medical_history": medical_history,
        "insurance_plan": insurance_plan
    }])

    prediction = model.predict(input_data)[0]

    st.success(f"Estimated Annual Premium: {prediction:,.2f}")
    st.caption(
        "This is an experimental ML estimate, not an actual insurance quote."
    )
