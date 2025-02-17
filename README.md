# Hypertension_Prediction
🩺 Hypertension_Prediction - A Streamlit API for predicting hypertension risk using machine learning. 🚀🔬

<img src="">

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

---

## 🏗️ Installation
Clone the repository and install dependencies:
```bash
# Clone the repo
git clone https://github.com/yourusername/hypertension_prediction.git
cd hypertension_prediction

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # For MacOS/Linux
venv\Scripts\activate  # For Windows

# Install required packages
pip install -r requirements.txt
```

---

## ⚙️ Usage
Run the **Streamlit** app:
```bash
streamlit run app.py
```

📌 Open your browser and go to: **`http://localhost:8501`**

---

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

### 🔹 Example API Call (Using cURL)
```bash
curl -X POST "http://localhost:8501/predict" -H "Content-Type: application/json" -d '{
    "Age": 45,
    "BMI": 27.8,
    "Cholesterol": 200,
    "Systolic_BP": 130,
    "Diastolic_BP": 85,
    "Smoking_Status": "Never",
    "Alcohol_Intake": 10.5,
    "Physical_Activity_Level": "Moderate",
    "Family_History": "Yes",
    "Diabetes": "No",
    "Stress_Level": 3,
    "Salt_Intake": 2.5,
    "Sleep_Duration": 7,
    "Heart_Rate": 72,
    "LDL": 120,
    "HDL": 60,
    "Triglycerides": 150,
    "Glucose": 110,
    "Gender": "Male",
    "Education_Level": "Secondary",
    "Employment_Status": "Employed"
}'
```
---

## 📸 Screenshots
### 🔹 **Home Page** 🏠
![Home Page](screenshots/home.png)

### 🔹 **Prediction Page** 🩺
![Prediction Page](screenshots/predict.png)


