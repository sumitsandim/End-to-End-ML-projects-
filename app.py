import streamlit as st
import pandas as pd
import pickle
Medications=['Anticonvulsant', 'No medication', 'Glucocorticoids']
gender=['F', 'M']
Pipe = pickle.load(open('pipe.pkl', 'rb'))
st.title('Fracture risk Detection System')
col1,col2=st.columns(2)
with col1:
    Medication=st.selectbox("select medication if  your taking ",sorted(Medications))
with col2:
    Sex=st.selectbox("select gender",sorted(gender))    
 

Age = st.number_input('age')
#Sex = st.number_input('sex')
Weight = st.number_input('weight_kg')
Height_cm = st.number_input('height_cm')
#Medication = st.number_input('medication')
BMD = st.number_input('bmd')

submitted = st.button('Submit')
if submitted:
    df = pd.DataFrame({
        'age': [Age],
        'sex': [Sex],
        'weight_kg': [Weight],
        'height_cm': [Height_cm],
        'medication': [Medication],
        'bmd': [BMD]})
    x = pd.DataFrame(df)
    prediction =Pipe.predict_proba(x)
    if prediction[0][0] > 0.5:
        st.write('YoU Have less risk of fracture')
    else:
        st.write('You have high risk of fracture')


        


