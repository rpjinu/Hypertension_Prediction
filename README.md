# Hypertension_Prediction
🩺 Hypertension_Prediction - A Streamlit API for predicting hypertension risk using machine learning. 🚀🔬

<img src="https://github.com/rpjinu/Hypertension_Prediction/blob/main/project_image.png">

# 🩺 Hypertension Prediction API 🚀

## 📌 Project Overview
Hypertension (high blood pressure) is a major risk factor for heart disease and stroke. This **Machine Learning-powered API** predicts the likelihood of hypertension based on health and lifestyle factors. Built using **Streamlit**, it provides an easy-to-use web interface for predictions.

---

## 📊 Dataset
The dataset consists of **174,982** records with **23** features related to demographics, health indicators, and lifestyle habits.

### 🔹 Key Features:
- **Demographics**: `Country`, `Age`, `Gender`, `Education_Level`, `Employment_Status`
- **Health Metrics**: `BMI`, `Cholesterol`, `Systolic_BP`, `Diastolic_BP`, `Heart_Rate`, `LDL`, `HDL`, `Triglycerides`, `Glucose`
- **Lifestyle Factors**: `Smoking_Status`, `Alcohol_Intake`, `Physical_Activity_Level`, `Sleep_Duration`, `Salt_Intake`
- **Medical History**: `Family_History`, `Diabetes`, `Stress_Level`
- **Target Variable**: `Hypertension` (High/Low)

---

## 🚀 Tech Stack
- **📌 Python** 🐍
- **📌 Pandas & NumPy** 📊
- **📌 Scikit-Learn** 🤖
- **📌 Streamlit** 🎨
- **📌 Matplotlib & Seaborn** 📈

## 🏆 Model Training
1. **Preprocessing**:
   - Handling missing values 🔍
   - Encoding categorical variables 🔠
   - Feature scaling 📏
2. **Model Selection**:
   - Logistic Regression 🤖
   - Random Forest 🌳
   - XGBoost 🚀
3. **Evaluation**:
   - Accuracy, Precision, Recall 📊
   - Confusion Matrix 🔄

---

## 📡 API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/predict` | `POST` | Predicts hypertension risk based on input features |
| `/train` | `GET` | Retrains the model with new data |


## 📸 Screenshots
### 🔹 **Home Page** 🏠
![Home Page]<img src="https://github.com/rpjinu/Hypertension_Prediction/blob/main/deploy_image%20(2).png">

### 🔹 **Prediction Page** 🩺
![Prediction Page]<img src="https://github.com/rpjinu/Hypertension_Prediction/blob/main/Predict_image.png">


