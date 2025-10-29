import streamlit as st

# Simple Streamlit display
st.write("# Welcome to My Streamlit App")

# widget to take user input
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0, max_value=120)
if st.button("Submit"):
    st.write(f"Hello, {name}! You are {age} years old.")

# sidebar for navigation
st.sidebar.title("Navigation")
selected_page = st.sidebar.selectbox("Go to", ["Home", "About", "Contact"])
st.sidebar.write(f"You selected: {selected_page}")
options = st.sidebar.radio("Choose an option:", ["Option 1", "Option 2", "Option 3"])
st.sidebar.write(f"You selected: {options}")


#Layout with columns
col1, col2 = st.columns(2)
with col1:
    st.header("Column 1")
    st.write("This is the first column.")

with col2:
    st.header("Column 2")
    st.write("This is the second column.")
    #Feedback and messages
    if st.button("Show Success Message"):
        st.success("This is a success message!")
    if st.button("Show Error Message"):
        st.error("This is an error message!")      
    if st.button("Show Warning Message"):
        st.warning("This is a warning message!")
