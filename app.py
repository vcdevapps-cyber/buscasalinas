import streamlit as st
import pandas as pd

# --- TENTATIVA DE IMPORTAÇÃO SEGURA ---
try:
    from duckduckgo_search import DDGS
    import instaloader
    ferramentas_prontas = True
except ImportError:
    ferramentas_prontas = False

# --- CONFIGURAÇÃO ---
st.set_page_config(page_title="Obs. Salinas", layout="wide")
SENHA_ACESSO = "salinas1969" 

st.title("🏛️ Observatório Salinas da Margarida")
st.caption("Pesquisa: Sérgio | História e Economia Local")

# --- LOGIN NA BARRA LATERAL ---
senha = st.sidebar.text_input("Chave de Acesso:", type="password")

if senha == SENHA_ACESSO:
    st.sidebar.success("Acesso Autorizado")
    aba1, aba2 = st.tabs(["🛒 Comércio", "🌐 Radar Web"])

    with aba1:
        st.subheader("Instagram (Supermercados)")
        st.info("Esta função é experimental na nuvem devido aos bloqueios da Meta.")
        if st.button("Consultar Redes Sociais"):
            st.warning("O Instagram costuma bloquear servidores. Use a Aba Radar Web para notícias.")

    with aba2:
        st.subheader("Busca Global (Google/DuckDuckGo)")
        if not ferramentas_prontas:
            st.error("⚠️ O servidor ainda não instalou as ferramentas de busca. Verifique o arquivo requirements.txt no GitHub.")
        else:
            termo = st.text_input("O que pesquisar?", value="Salinas da Margarida")
            if st.button("🔍 Iniciar Varredura"):
                with st.spinner("Buscando fontes..."):
                    try:
                        with DDGS() as ddgs:
                            results = [r for r in ddgs.text(termo, max_results=5)]
                            for r in results:
                                st.markdown(f"**[{r['title']}]({r['href']})**")
                                st.write(r['body'])
                                st.divider()
                    except Exception as e:
                        st.error(f"Erro na varredura: {e}")
else:
    st.info("Digite a senha para acessar seu laboratório de pesquisa.")
