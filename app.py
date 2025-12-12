import streamlit as st

#Títulos
st.title("Calculadora de Calorias e Macros do TUPY")
st.header("Preencha seus dados abaixo para começar!")

#Inputs
nome = st.text_input("Nome: ")
idade = st.number_input("Idade: ", min_value=10, max_value=150, step=1)
peso = st.number_input("Peso (kg): ", min_value=30.0, max_value=400.0, step=0.1)
altura = st.number_input("Altura (cm): ", min_value=100, max_value=300, step=1.0)
sexo = st.selectbox("Sexo Biológico: ", ["Masculino", "Feminino"])








