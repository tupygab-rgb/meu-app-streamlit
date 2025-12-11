import streamlit as st

st.title("Questionário Interativo")

# Entradas básicas
nome = st.text_input("Qual seu nome?")
idade = st.number_input("E sua idade?", min_value=0, max_value=120, step=1)
peso = st.number_input("Quantos quilinhos você tá pesando?", min_value=0.0, step=0.1)

# Escolha do gênero
genero = st.selectbox("Você é:", ["Selecione...", "homi", "muié"])

# Só continua quando tudo estiver preenchido
if nome and idade > 0 and peso > 0 and genero != "Selecione...":

    st.subheader("Resultado")

    if genero == "homi":
        st.write(
            f"eai parceiro, tranquilo? Fiquei sabendo que seu nome é **{nome}**, "
            f"que você tem **{idade}** aninhos e tá pesando seus **{peso} kg**. "
            "Tá tudo certinho?"
        )

    elif genero == "muié":
        st.write(
            f"eai parceira, tranquila? Fiquei sabendo que seu nome é **{nome}**, "
            f"que você tem **{idade}** aninhos e tá pesando seus **{peso} kg**. "
            "Tá tudo certinho?"
        )

    # Pergunta final
    questionario = st.radio("Responda:", ["sim", "não"])

    if questionario == "sim":
        st.write("Perfeito então 😁")
    else:
        resposta = st.text_input("Poxa! Me diga como posso te ajudar então:")
        if resposta:
            st.write(
                "Mas só me diga, porque infelizmente não posso fazer nada pra ajudar… "
                "sou só um comecinho de programação e meu desenvolvedor ainda tá aprendendo kkkkk 😂"
            )
