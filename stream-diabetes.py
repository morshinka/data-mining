import pickle 
import streamlit as st

#membaca model
diabtes_model = pickle.load(open('diabetes_model.sav', 'rb'))

#judul website

st.title('Diabetes Prediction')

#membagi colom

col1, col2 = st.columns(2)

with col1 :
    pregancies = st.text_input('pregnancies')
    
with col2 :
    glucose = st.text_input('Glucose')

with col1 :
    bloodPressure = st.text_input('Blood Pressure')

with col2 :
    skinThickness = st.text_input('Skin Thickness')

with col1 :
    insulin = st.text_input('Insulin')

with col2 :
    bmi = st.text_input('Body Mass Index')

with col1 :
    diabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')

with col2 :
    age = st.text_input('Age')

#code untuk prediksi
diab_diagnosis = ''

#membuat model perediksi
if st.button('Prediksi Diabetes'):
    diab_prediction = diabtes_model.predict([[pregancies, glucose, bloodPressure, skinThickness, insulin, bmi, diabetesPedigreeFunction, age]])
    
    if(diab_prediction[0] == 0):
        diab_diagnosis = 'Pasien terkena diabetes'
    else: 
        diab_diagnosis = 'Pasien tidak terkena diabetes'
    st.success(diab_diagnosis)


