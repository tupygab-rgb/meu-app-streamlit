import streamlit as st

#Títulos
st.title("Calculadora de Calorias e Macros do TUPY")
st.header("Preencha seus dados abaixo para começar!")

#Inputs
nome = st.text_input("Nome: ")
idade = st.number_input("Idade: ", min_value=0, max_value=150, step=1.0)



