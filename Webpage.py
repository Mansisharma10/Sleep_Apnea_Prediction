import numpy as np
import pickle 
import streamlit as st
import time


decision_load = pickle.load(open("decision_tree_model.pkl","rb"))

def sleep(input_data):

    input_data_as_numpy_array = np.asarray(input_data)

    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = decision_load.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return'The person is suffering from sleep apnea disorder, please concern doctor :-( '
    else:
        return 'You are healthy :-) '
    

def main():
    st.title('Sleep Apnea Prediction')



    Gender = st.text_input('Gender (0 = Female, 1 = Male)')
    Age = st.text_input('Age')
    Occupation = st.text_input('occupation (Accountant=0, Doctor=1, Engineer=2, Lawyer=3, Manager=4, Nurse=5, Sales Representative=6, Sales-person=7, Scientist=8, Software Engineer=9, Teacher=10 )')
    Sleep_Duration = st.text_input('sleep duration (In hours)')
    Quality_of_Sleep = st.text_input('Quality of Sleep')
    Physical_Activity_Level = st.text_input('Physical Activity Level')
    Stress_Level = st.text_input('Stress Level')
    BMI_Category = st.text_input('BMI Category (Normal=0, Normal Weight=1, Obese=2, Overweight=3)')
    Heart_Rate = st.text_input('Heart Rate')
    Daily_Steps = st.text_input('Daily Steps')
    SYSTOLIC = st.text_input('SYSTOLIC ,<120')
    Diastolic = st.text_input('Diastolic <80 ')


    disorder =''

    # button

    if st.button('prediction'):
            disorder = sleep([Gender ,Age, Occupation, Sleep_Duration, Quality_of_Sleep, Physical_Activity_Level, Stress_Level, BMI_Category, Heart_Rate, Daily_Steps, SYSTOLIC, Diastolic ])

    
    st.success(disorder)


if __name__ == '__main__':
    main()