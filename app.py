import streamlit as st

# Title
st.title("Simple Greeting App")

# User name input
name = st.text_input("Enter your name:")

# Greeting message
if name:
    st.write(f"Hello, {name}! Welcome to the app 😊")

# Age slider
age = st.slider("Select your age:", 1, 100, 18)

# Display selected age
st.write(f"Your age is: {age}")

# Celebration button
if st.button("Celebrate!"):
    st.balloons()
    st.success("🎉 Congratulations! Celebration started!")