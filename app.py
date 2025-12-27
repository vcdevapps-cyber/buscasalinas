import streamlit as st
import pandas as pd

# Tentar importar as ferramentas de busca de forma segura
try:
    from duckduckgo_search import DDGS
    import instaloader
    ferramentas_prontas = True
except Exception as e:
    st.error(f"Erro ao carregar bibliotecas: {e}")
    ferramentas_prontas = False

# --- CONFIGURAÇÃO ---
st.set_page_config(page_title="Obs. Salinas", layout="wide")
SENHA_ACESSO = "salinas1969" 

st.title("🏛️ Observatório Salinas da Margarida")
st.caption("Versão de Diagnóstico - Sérgio")

# --- LOGIN ---
senha = st.sidebar.text_input("Chave de Acesso:", type="password")

if senha == SENHA_ACESSO:
    st.sidebar.success("Acesso Autorizado")
    
    aba1, aba2 = st.tabs(["🛒 Comércio", "🌐 Radar Web"])

    with aba1:
        st.subheader("Instagram")
        if st.button("Tentar Coleta"):
            st.info("Esta função pode ser bloqueada pela nuvem. Teste a Aba Radar Web.")

    with aba2:
        st.subheader("Busca na Web")
        termo = st.text_input("Pesquisa:", value="Salinas da Margarida")
        
        if st.button("🔍 Procurar"):
            if ferramentas_prontas:
                try:
                    with DDGS() as ddgs:
                        resultados = [r for r in ddgs.text(termo, max_results=5)]
                        for r in resultados:
                            st.markdown(f"**[{r['title']}]({r['href']})**")
                            st.write(r['body'])
                            st.divider()
                except Exception as e:
                    st.error(f"Erro na busca: {e}")
            else:
                st.error("As ferramentas de busca não foram instaladas corretamente.")
else:
    st.info("Digite a senha 'salinas1969' na barra lateral esquerda para começar.")
