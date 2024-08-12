import streamlit as st

# Title of the Web App
st.title("Welcome to My Streamlit Website")

# Subtitle
st.header("A Simple Streamlit App")

# Text
st.write("This is a simple website made using Streamlit. It allows you to quickly create web applications using just Python.")

# Input Fields
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")

# Slider
age = st.slider("Select your age:", 0, 100, 25)
st.write(f"You are {age} years old.")

# Checkbox
if st.checkbox("Show Additional Info"):
    st.write("Streamlit is amazing for quick prototyping and deploying data-driven apps!")

# Button
if st.button("Click Me!"):
    st.write("Button clicked!")

# Select Box
option = st.selectbox("Choose a favorite color:", ["Red", "Blue", "Green"])
st.write(f"Your favorite color is {option}.")

# Image Display
st.image("download.jpeg", caption="Sample Image", use_column_width=True)

# Data Display
import pandas as pd
data = {"Name": ["yamini", "Vandana", "rohini"], "Age": [24, 27, 22]}
df = pd.DataFrame(data)
st.write("Here is a simple data table:")
st.dataframe(df)

# End of the App
st.write("Thanks for visiting!")
