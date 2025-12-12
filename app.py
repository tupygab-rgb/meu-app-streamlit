import streamlit as st

# --- CSS para mudar a borda dos inputs ---
st.markdown("""
    <style>
        /* Muda a borda quando o campo está focado */
        input:focus, select:focus, textarea:focus {
            border: 2px solid #4CAF50 !important; /* borda verde */
            box-shadow: 0 0 5px #4CAF50 !important;
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












