import streamlit as st

def display_diagnosis(diab_diagnosis):
    st.title("Diabetes Diagnosis Result")
    st.success(diab_diagnosis)

if __name__ == "__main__":
    display_diagnosis(diab_diagnosis)