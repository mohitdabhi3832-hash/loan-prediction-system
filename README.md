# loan-prediction-system
Machine Learning based Loan Prediction System with Streamlit Frontend


# Loan Prediction System

# Overview
The Loan Prediction System is a Machine Learning-based web application that predicts whether a loan application is likely to be approved or rejected based on applicant details.

This project uses classification algorithms to analyze user inputs and provide accurate loan approval predictions through an interactive frontend built with Streamlit.

# Features
- Predicts loan approval status
- User-friendly Streamlit interface
- Real-time predictions
- Data preprocessing and scaling
- Machine Learning model integration

# Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib


# Machine Learning Models
- K-Nearest Neighbors (KNN)
- Support Vector Classifier (SVC)
- Naive Bayes
- DecisionTreeClassifier

# Project Structure
plaintext
loan-prediction-system/
│── loan_prediction.ipynb
│── loan_prediction_frontend.py
│── loan_model.pkl
│── scaler_loan.pkl
│── README.md


Run the application:

bash
streamlit run loan_prediction_frontend.py


# Input Parameters
- Gender
- Marital Status
- Dependents
- Education
- Self Employment
- Applicant Income
- Coapplicant Income
- Loan Amount
- Loan Term
- Credit History
- Property Area


# Output
- Loan Approved
- Loan Rejected
  

# Future Improvements
- Improve model accuracy
- Add advanced UI features
- Add multiple model comparison

