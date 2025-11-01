import pickle
import streamlit as st



model1=pickle.load(open("areaprice.pkl","rb"))

def mydeploy():
    st.title("Area Price Prediction")
    area=st.number_input("Enter the Value of Area")
    pred=st.button("Predict")

    if pred:
        x=model1.predict([[area]])
        st.write("Price of given area is :",x[0])




mydeploy()