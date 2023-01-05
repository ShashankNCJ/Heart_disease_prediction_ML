# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 00:20:36 2022

@author: user
"""

import numpy as np
import pickle
import streamlit as st
import sklearn

#loading the saved model
loaded_model=pickle.load(open('C:/Users/user/Downloads/trained_model.sav','rb'))

#creating a function for prediction

def heart_prdiction(input_data):
   
    # change the input data to a numpy array
    input_data_as_numpy_array= np.asarray(input_data)

    # reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return'The Person does not have a Heart Disease'
    else:
      return'The Person has Heart Disease'
      
      
      
def main():
    #giving a title
    st.title('Heart Disease prediction Web App')
    
    st.image("heart.jpg")
    
    #getting the input data from the user
    age=st.slider('Age', min_value=20, max_value=80, value=40)
    sex_list=['','0','1']
    sex=st.selectbox('Enter the gender [0-Female,1-Male]',sex_list)
    cp_list=['','0','1','2','3']
    cp=st.selectbox('Range of chest pain [0-3]',cp_list)
    trestbps=st.text_input('Enter the Blood pressure')
    chol=st.text_input('Enter the cholestoral level')
    fbs_list=['','0','1']
    fbs=st.selectbox("Enter the value of Fasting blood sugar", fbs_list)
    restecg_list=['','0','1']
    restecg=st.selectbox('Enter the Resting Electrocardiographic results',restecg_list)
    thalach=st.text_input('Enter the Thalach value')
    exang_list=['','0','1']
    exang=st.selectbox('Enter Exercise induced angina(exang)',exang_list)
    oldpeak=st.text_input('enter the old peak value')
    slope_list=['','0','1']
    slope=st.selectbox('Enter the Slope value',slope_list)
    ca_list=['','0','1','2','3']
    ca=st.selectbox('Enter the ca value',ca_list)
    thal_list=['','1','2','3']
    thal=st.selectbox('Enter the Thal Value',thal_list)
    
    #code for prediction
    predicter = ''
    
    #creating a button for prediction
    
    if st.button('Heart Disease Test Result'):
        predicter=heart_prdiction([age,sex,cp, trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
        
        
    st.success(predicter)
    
    
if __name__ == '__main__':
    main()
        
        
    
    
    
    