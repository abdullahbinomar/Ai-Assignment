# calculator_app.py

import streamlit as st

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero"

def main():
    st.title("Simple Calculator")
    st.write("Enter two numbers and select an operation:")

    n1 = st.number_input("Enter first number:", step=0.1)
    n2 = st.number_input("Enter second number:", step=0.1)

    operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])

    if operation == "Add":
        result = add(n1, n2)
    elif operation == "Subtract":
        result = subtract(n1, n2)
    elif operation == "Multiply":
        result = multiply(n1, n2)
    elif operation == "Divide":
        result = divide(n1, n2)

    st.write(f"Result: {result}")

if __name__ == "__main__":
    main()
