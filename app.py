import streamlit as st


#Títulos
st.title("Calculadora de Calorias e Macros do TUPY")
st.header("Preencha seus dados abaixo para começar!")

#Inputs
nome = st.text_input("Nome: ")
idade = st.number_input("Idade: ", min_value=10, max_value=150, step=1, value=None)
peso = st.number_input("Peso (kg): ", min_value=30.0, max_value=400.0, step=0.1, value=None)
altura = st.number_input("Altura (cm): ", min_value=100, max_value=300, step=1, value=None)
sexo = st.selectbox("Sexo Biológico: ", ["Selecione...","Masculino", "Feminino"])

#inicializar tmb
tmb = None
gcd = None
resultado = None
#Calcular TMB
def calcular_tmb(idade, peso, altura, sexo):
    if sexo == "Masculino":
      tmb = 88.36 + (13.4*peso) + (4.8*altura) - (5.7*idade)
    else:
      tmb = 447.6 + (9.2*peso) + (3.1*altura) - (4.3*idade)
    return tmb
#Verificação se todos campos foram preenchidos para Calcular a TMB
if sexo != "Selecione..." and idade is not None and peso is not None and altura is not None:
    tmb = calcular_tmb(idade, peso, altura, sexo)
    st.subheader(f"Sua Gasto Calórico Base é💥: {tmb:.0f} Kcal")
else:
    st.warning("Preencha todos campos acima para continuar.")

#Perguntar nível de atividade física e calcular Gasto Calórico Diário
if tmb is not None:
    st.write("Agora, vamos calcular seu gasto calórico de acordo com seu nível de atividade💪:")
    atividade = st.selectbox("Nível de atividade física:", ["Selecione...", "Sedentário", "Levemente ativo", "Moderadamente ativo", "Muito ativo", "Extremamente ativo"])

    fator = {"Sedentário": 1.2, "Levemente ativo": 1.375, "Moderadamente ativo": 1.55, "Muito ativo": 1.725, "Extremamente ativo": 1.9} 
    #Calculo GCD
    if atividade != "Selecione...":
        gcd = tmb * fator[atividade] 
        st.subheader(f"Seu Gasto Calórico Diário estimado é🔥: {gcd:.0f} Kcal")
        #Objetivos
        objetivo = st.selectbox("Qual seu Objetivo?",["Selecione...","Perder Peso", "Manter o Peso", "Ganhar Peso"])
        if objetivo != "Selecione...":
           if objetivo == "Perder Peso":
               resultado = gcd - 500
           elif objetivo == "Manter o Peso":
               resultado = gcd
           elif objetivo == "Ganhar Peso":
               resultado = gcd + 500
        if resultado is not None:
            st.success(f"Beleza! Então você deve consumir {resultado:.0f} Kcal por dia🥗")








































