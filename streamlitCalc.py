import math
import streamlit as st

st.set_page_config(page_title="Not so simple Calculator", page_icon="🧮")
st.write("# Not so simple Calculator")
st.divider()

#Input Area
col1, col2, col3 = st.columns(3)
with col1:
    num1 = st.number_input("Enter first number", value=1.0) 
with col2:
    num2 = st.number_input("Enter second number", value=1.0)
with col3:
    operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])


#calculate button
if st.button("Calculate"):
    result = None
    explanation = ""
    try:
        if operation == "Add":
            result = num1 + num2
            explanation = f"{num1} + {num2} = {result}"
            
        elif operation == "Subtract":
            result = num1 - num2
            explanation = f"{num1} - {num2} = {result}" 
        elif operation == "Multiply":
            result = num1 * num2
            explanation = f"{num1} * {num2} = {result}"
        elif operation == "Divide":
            result = num1 / num2 if num2 != 0 else "Error: Division by zero"
            explanation = f"{num1} / {num2} = {result}"

        # Display result and explanation
        if result is not None:
            st.success(f"Result: {result}")
            st.info(f"Explanation: {explanation}")
        
        # store calculation in session state
        if 'calculations' not in st.session_state:
            st.session_state.calculations = []
            st.session_state.calculations.append(explanation)
        else:
            st.session_state.calculations.append(explanation)

    except Exception as e:
        st.error(f"An error occurred: {e}")


#History of calculations
st.divider()
st.subheader("Calculation History")

if 'calculations' in st.session_state and st.session_state.calculations:
    # for calc in st.session_state.calculations:
    #     st.write(calc)
    for i, calc in enumerate(reversed(st.session_state.calculations[-5:]), 1):
        st.write(f"{i}: {calc}")
else:
    st.info("No calculations yet.") 

# def main():
#     st.title("Not so simple Calculator")

#     # Input fields for numbers
#     num1 = st.number_input("Enter first number", value=0)
#     num2 = st.number_input("Enter second number", value=0)

#     # Dropdown for selecting operation
#     operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])

#     # Button to calculate result
#     if st.button("Calculate"):
#         if operation == "Add":
#             result = num1 + num2
#         elif operation == "Subtract":
#             result = num1 - num2
#         elif operation == "Multiply":
#             result = num1 * num2
#         elif operation == "Divide":
#             result = num1 / num2 if num2 != 0 else "Error"

#         st.write(f"Result: {result}")

# if __name__ == "__main__":
#     main()