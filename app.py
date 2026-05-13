import streamlit as st
import joblib
import numpy as np

model=joblib.load(open('loan_model.pkl','rb'))
scaler=joblib.load(open('scaler_loan.pkl','rb'))
st.title("Loan Prediction..")

gender=st.selectbox("Gender ",['Male','Female'])
married=st.selectbox("Married ",['Yes','No'])
Dependents= st.selectbox("Dependents ",[0,1,2,3])
Eduction= st.selectbox("Eduction ",['Graduate','Not Graduate'])
self_Employed=st.selectbox("Self_Employed ",['Yes','No'])

Applicant_income= st.slider("Applicant Income ",1000,10000)
Coapplicant_income= st.slider("Coapplicant Income ",0,25000)
loan_amount= st.number_input("Loan Amount ")
loan_amount_term= st.number_input("Loan Amount Term ")

credit_history= st.selectbox("Credit History ",[0,1])
property_area= st.selectbox("Property Area ",['Urban', 'Semiurban', 'Rural'])


gender= 1 if gender=="Male" else 0
married= 1 if married=="Yes" else 0
Eduction= 0 if Eduction=="Graduate" else 1
self_Employed= 1 if self_Employed=="Yes" else 0
if property_area=="Urban":
    property_area=1
elif property_area=="Semiurban":
    property_area=2
else:
    property_area=0


if st.button("Predict"):
    data=np.array([
        [gender,married,Dependents,Eduction,self_Employed,Applicant_income,Coapplicant_income,
         loan_amount,loan_amount_term,credit_history,property_area
         ]

    ])
    data=scaler.transform(data)
    pred=model.predict(data)
    if pred[0]==1:
        st.success("Loan Approved.")
    else:
        st.error("Loan Rejected.")
