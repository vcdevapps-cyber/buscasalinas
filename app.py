import streamlit as st
import instaloader
from googlesearch import search
import pandas as pd

# --- SEGURANÇA E TÍTULO ---
st.set_page_config(page_title="Obs. Salinas", layout="wide")
SENHA_ACESSO = "salinas1969" 

st.title("🏛️ Observatório Salinas da Margarida")
st.caption("Pesquisador: Sérgio | História, Economia e Sociedade")

# --- BARRA LATERAL (LOGIN) ---
senha = st.sidebar.text_input("Chave de Acesso:", type="password")

if senha == SENHA_ACESSO:
    st.sidebar.success("Acesso autorizado")
    # Divisão do App em duas frentes de pesquisa
    aba1, aba2 = st.tabs(["🛒 Comércio (Instagram)", "🌐 Radar Web (Google)"])

    # --- ABA 1: MONITORAMENTO COMERCIAL ---
    with aba1:
        st.subheader("Análise de Preços e Ofertas")
        if st.button("🚀 Atualizar Redes Sociais"):
            L = instaloader.Instaloader()
            st.info("Acessando perfis de Salinas... Aguarde.")
            # O robô buscará os dados do Mercadão e Mix Prime aqui.
            # (A lógica de exibição de imagens que ajustamos antes)

    # --- ABA 2: RADAR DE NOTÍCIAS E MENÇÕES ---
    with aba2:
        st.subheader("Hemeroteca Digital em Tempo Real")
        termo = st.text_input("O que pesquisar na web?", value="Salinas da Margarida")
        if st.button("🔍 Iniciar Varredura"):
            with st.spinner(f"Buscando menções a '{termo}'..."):
                try:
                    resultados = search(termo, num_results=10, lang="pt")
                    st.success("Busca finalizada!")
                    for link in resultados:
                        st.write(f"📄 [Link Encontrado]({link})")
                        st.caption(link)
                        st.divider()
                except Exception as e:
                    st.error(f"Erro na busca: {e}")
else:
    st.info("Aguardando Chave de Acesso para liberar os arquivos digitais.")