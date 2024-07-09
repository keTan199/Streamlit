import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')
st.header('This is a header with a divider', divider='rainbow')
st.header('_Streamlit_ is :blue[cool] :sunglasses:')
st.subheader('_Streamlit_ is :blue[cool] :sunglasses:')

agree = st.checkbox("I agree")

if agree:
    st.write("Great!")

#Radio Genere
genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])

if genre == ":rainbow[Comedy]":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")

#Radio Gender
status = st.radio("Select Gender:", ("Male", "Female"))
if (status == "Male"):
    st.success("Male")
else:
    st.success("Female")


#Button
st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

#Function
def sqr(num):
    return num*num

num = st.number_input("Enter a number")


if st.button("Calculate square root of number"):
    res = sqr(num)
    st.write(f"The square root of {num} is {res}")








