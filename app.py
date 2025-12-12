import streamlit as st

st.markdown("""
    <style>
    input:focus, textarea:focus, select:focus {
        outline: none !important;        /* remove o contorno */
        border: 2px solid #4CAF50 !important; /* coloca borda verde suave */
        box-shadow: none !important;     /* remove o glow vermelho */
    }
    </style>
""", unsafe_allow_html=True)

#Títulos
st.title("Calculadora de Calorias e Macros do TUPY")
st.header("Preencha seus dados abaixo para começar!")

#Inputs
nome = st.text_input("Nome: ")
idade = st.number_input("Idade: ", min_value=10, max_value=150, step=1, value=None)
peso = st.number_input("Peso (kg): ", min_value=30.0, max_value=400.0, step=0.1, value=None)
altura = st.number_input("Altura (cm): ", min_value=100, max_value=300, step=1, value=None)
sexo = st.selectbox("Sexo Biológico: ", ["Masculino", "Feminino"])













