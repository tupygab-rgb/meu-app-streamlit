import streamlit as st


#Títulos
st.title("Calculadora de Calorias e Macros do TUPY")
st.header("Preencha seus dados abaixo para começar!")

#Inputs
nome = st.text_input("Nome: ")
idade = st.number_input("Idade: ", min_value=10, max_value=150, step=1, value=None)
peso = st.number_input("Peso (kg): ", min_value=30.0, max_value=400.0, step=0.1, value=None)
altura = st.number_input("Altura (cm): ", min_value=100, max_value=300, step=1, value=None)
sexo = st.selectbox("Sexo Biológico: ", ["Masculino", "Feminino"])

#Calcular TMB
def calcular_tmb(idade, peso, altura, sexo):
    if sexo == "Masculino":
      tmb = 88.36 + (13.4*peso) + (4.8*altura) - (5.7*idade)
    else:
      tmb = 447.6 + (9.2*peso) + (3.1*altura) - (4.3*idade)
    return tmb
#Verificação se todos campos foram preenchidos para Calcular a TMB
if idade is not None and peso is not None and altura is not None:
    tmb = calcular_tmb(idade, peso, altura, sexo)
    st.write("Sua Gasto Calórico Base é:", tmb)
else:
    st.warning("Preencha todos campos acima")



















