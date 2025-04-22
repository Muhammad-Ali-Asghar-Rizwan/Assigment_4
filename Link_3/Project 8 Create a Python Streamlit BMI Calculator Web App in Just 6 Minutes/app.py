# BMI CALCULATOR
import  streamlit as st
import time

st.set_page_config(page_title="BMI Calculator", page_icon="🚨" , layout="wide" )

st.title("BMI Calculator")
st.markdown("""
            ## apna body mass index (bmi ) calculator kren Nechay apna **weight and height ** enter kren
            """)
col1 , col2 = st.columns(2)

with col1:
    weight = st.number_input("Weight (kg)" , min_value=1.0 ,  format="%.2f",)

with col1:
    height = st.number_input("Height (m)" , min_value=1.0 ,  format="%.2f",)
    
    
if height > 0 and weight > 0:
    bmi = weight / (height ** 2) #bmi formula
    st.subheader("APKA BMI HAI") 
    st.markdown(f"{bmi:.2f}" , unsafe_allow_html=True)
    
    
    
    if bmi < 18.5:
        st.error("underweight")
    elif 18.5 <= bmi < 24.9:
     st.success("normal weight")
    elif 25 <= bmi < 29.9:
     st.warning("overweight")
    else:
        st.error("Obsity")