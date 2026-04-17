#1. Import Streamlit
import streamlit as st

# Add a title to your app
st.title("My first streamlit created by Moulya Shivakoti")

#Add some text
st.write("Welcome! This app calculates square of numbers ")

# Create an interactive slider
st.header("Select a Number") 
number=st.slider("Pick up a number,0,100,10") #min max default

#5 Calculate and display the result
st.subheader("Result")
squared_number = number * number
st.write(f"The square of the **{number}** is **{squared_number}**.")

