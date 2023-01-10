import streamlit as st
import pickle

st.title('Iris Recognition')

model = pickle.load(open('SVM.pickle','rb'))

sl = st.number_input('Enter Sepal Length')
sw = st.number_input('Enter Sepal Width')
pl = st.number_input('Enter Petal Length')
pw = st.number_input('Enter Petal Width')

if st.button('Predict'):
    data=[[sl,sw,pl,pw]]
    result=model.predict(data)
    st.success(result[0])