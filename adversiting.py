import streamlit as st
import pandas as pd
import pickle

st.write("""
# Sales Prediction App

This app predicts the **Number of Sales!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    Number_of_TV = st.sidebar.slider('Number_of_TV', 0.7, 296.4, 5.4)
    Number_of_Radio = st.sidebar.slider('Number_of_Radio', 0.0, 49.6, 3.4)
    Number_of_Newspaper = st.sidebar.slider('Number_of_Newspaper', 0.3, 114.0, 1.3)
    data = {'TV': Number_of_TV,
            'Radio': Number_of_Radio,
            'Newspaper': Number_of_Newspaper}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

loaded_model = pickle.load(open("projecthema.h5", "rb"))

prediction = loaded_model.predict(df)

st.subheader('Sales Prediction')
st.write(prediction)
