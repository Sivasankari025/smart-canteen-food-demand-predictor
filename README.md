# 🍱 Smart Canteen Food Demand Predictor

A Machine Learning web application that predicts food demand using historical meal-ordering and fulfilment-center data. The system helps canteen management estimate expected food demand for better food preparation, inventory planning, and reduction of food wastage.

## 1. 📌 Project Overview

The **Smart Canteen Food Demand Predictor** uses Machine Learning to predict the expected number of meals ordered based on historical demand and operational information.

**Main features:**
- Data preprocessing and feature engineering
- Random Forest regression
- MAE and RMSE evaluation
- Grid Search hyperparameter tuning
- Flask REST API
- Interactive web frontend
- Git/GitHub version control
- Render cloud deployment



## 2. 🎯 Objectives

- Collect and prepare food-demand data.
- Handle missing values and preprocess data.
- Perform feature engineering.
- Train a Machine Learning regression model.
- Evaluate the model using MAE and RMSE.
- Optimize the model using Grid Search.
- Develop a REST API using Flask.
- Create an interactive prediction interface.
- Deploy the application online.
- Test the application for accuracy and usability.

---

## 3. 📊 Dataset & Machine Learning

### Dataset

The project uses the **Food Demand Forecasting** dataset containing historical meal-order information.

Important attributes include:

- Week
- Center ID
- Meal ID
- Checkout Price
- Base Price
- Emailer Promotion
- Homepage Promotion
- City Code
- Region Code
- Center Type
- Operational Area
- Number of Orders

**Dataset:**  
[Food Demand Forecasting Dataset – Kaggle](https://www.kaggle.com/competitions/food-demand-forecasting-iod-week8-ensemblelearning/data?utm_source=chatgpt.com)

### Machine Learning Problem

**Problem Type:** Regression

**Target Variable:** `num_orders`

The model predicts the expected number of meals that may be ordered.

### Model

The project uses **Random Forest Regressor** for demand prediction.

Model performance is evaluated using:

- **MAE (Mean Absolute Error)**
- **RMSE (Root Mean Squared Error)**

---

## 4. 🔄 Project Workflow

```text
Historical Dataset
       ↓
Data Collection
       ↓
Data Cleaning
       ↓
Missing Value Handling
       ↓
Feature Engineering
       ↓
Train / Test Split
       ↓
Random Forest Model
       ↓
MAE & RMSE Evaluation
       ↓
Grid Search Optimization
       ↓
Best Model
       ↓
model.pkl
       ↓
Flask REST API
       ↓
Interactive Web Interface
       ↓
Food Demand Prediction
```

---

## 5. 🧠 Model Optimization

Grid Search is used to find better hyperparameter combinations for the Random Forest model.

Example parameters:

```python
param_grid = {
    "n_estimators": [50, 100],
    "max_depth": [10, 20],
    "min_samples_split": [2, 5]
}
```

The best model is selected using:

```python
grid.best_estimator_
```

The trained model is saved using Joblib:

```python
joblib.dump(model, "model.pkl")
```

---

## 6. 🌐 Application & Frontend

The trained model is integrated with a **Flask REST API**.

The application:

1. Accepts user input.
2. Processes the input.
3. Sends the data to the trained ML model.
4. Generates the predicted demand.
5. Displays the result on the web interface.

### Technologies

- **Backend:** Flask
- **Frontend:** HTML, CSS, JavaScript
- **ML:** Scikit-learn
- **Data Processing:** Pandas, NumPy
- **Model Saving:** Joblib

### Project Structure

```text
smart-canteen-food-demand-predictor/
│
├── data/
│   ├── fulfilment_center_info.csv
│   ├── meal_info.csv
│   └── train.csv
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── app.py
├── train_model.py
├── check_data.py
├── model.pkl
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 7. 💻 Installation & Local Execution

### Clone the Repository

```bash
git clone https://github.com/Sivasankari025/smart-canteen-food-demand-predictor.git
cd smart-canteen-food-demand-predictor
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

**Windows:**

```bash
venv\Scripts\activate
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 8. 🚀 Deployment & Testing

The application can be deployed without Docker using **Render**.

### Deployment Workflow

```text
Local Project
     ↓
Git
     ↓
GitHub
     ↓
Render
     ↓
Flask + Gunicorn
     ↓
Public Web Application
```

### Render Configuration

**Build Command:**

```text
pip install -r requirements.txt
```

**Start Command:**

```text
gunicorn app:app
```

**Render:**  
[Render](https://smart-canteen-food-demand-predictor.onrender.com/)

### Testing

The application is tested for:

- Webpage loading
- Valid user inputs
- Prediction button functionality
- Prediction generation
- Invalid input handling
- Model performance using MAE and RMSE
- Frontend usability
- Responsive interface

---

## 9. 🌟 Benefits, Future Scope & Resources

### Benefits

- Reduces food wastage.
- Helps avoid food shortages.
- Improves inventory planning.
- Estimates meal requirements.
- Supports canteen management decisions.
- Enables data-driven food preparation.

### Future Enhancements

- Daily and weekly demand forecasting
- Weather-based demand prediction
- Holiday and event information
- Real-time sales data
- Stock-level prediction
- Food wastage prediction
- Automated inventory recommendations
- Advanced models such as XGBoost and LightGBM
- Admin dashboard
- Mobile application

### Technologies & Resources

- [Python](https://www.python.org/?utm_source=chatgpt.com)
- [Pandas](https://pandas.pydata.org/?utm_source=chatgpt.com)
- [Scikit-learn](https://scikit-learn.org/?utm_source=chatgpt.com)
- [Flask](https://flask.palletsprojects.com/?utm_source=chatgpt.com)
- [GitHub](https://github.com/?utm_source=chatgpt.com)
- [Render](https://render.com/?utm_source=chatgpt.com)
- [Kaggle Food Demand Forecasting Dataset](https://www.kaggle.com/competitions/food-demand-forecasting-iod-week8-ensemblelearning/data?utm_source=chatgpt.com)

### Project Information

**Project Title:** Smart Canteen Food Demand Predictor  
**Domain:** Machine Learning / Web Application  
**Problem Type:** Regression  
**Backend:** Flask  
**Frontend:** HTML, CSS, JavaScript  
**ML Model:** Random Forest Regressor  
**Deployment:** Render  
**Version Control:** Git & GitHub
