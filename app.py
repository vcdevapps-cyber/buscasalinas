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

# Inicializar a "memória" do app para os resultados da busca
if 'resultados_web' not in st.session_state:
    st.session_state.resultados_web = []

st.title("🏛️ Observatório Salinas da Margarida")
st.caption("Pesquisa: Sérgio | História e Economia Local")

# --- LOGIN NA BARRA LATERAL ---
senha = st.sidebar.text_input("Chave de Acesso:", type="password")

if senha == SENHA_ACESSO:
    st.sidebar.success("Acesso Autorizado")
    aba1, aba2 = st.tabs(["🛒 Comércio", "🌐 Radar Web"])

    with aba1:
        st.subheader("Instagram (Supermercados)")
        st.info("Esta função é experimental. O Instagram costuma bloquear servidores de nuvem.")
        if st.button("Consultar Redes Sociais"):
            st.warning("Verifique o log se os dados não aparecerem.")

    with aba2:
        st.subheader("Busca Global (Google/DuckDuckGo)")
        if not ferramentas_prontas:
            st.error("⚠️ Ferramentas de busca não instaladas no servidor.")
        else:
            termo = st.text_input("O que pesquisar?", value="Salinas da Margarida")
            
            # Botão para disparar a busca
            if st.button("🔍 Iniciar Varredura"):
                with st.spinner("Buscando fontes..."):
                    try:
                        with DDGS() as ddgs:
                            # Guardamos os resultados na "memória" (session_state)
                            st.session_state.resultados_web = [r for r in ddgs.text(termo, max_results=7)]
                    except Exception as e:
                        st.error(f"Erro na varredura: {e}")

            # EXIBIÇÃO DOS RESULTADOS (Fora do botão, para não sumirem)
            if st.session_state.resultados_web:
                st.write(f"--- Resultados para: {termo} ---")
                for r in st.session_state.resultados_web:
                    st.markdown(f"### [{r['title']}]({r['href']})")
                    st.write(r['body'])
                    st.divider()
else:
    st.info("Digite a senha para acessar seu laboratório de pesquisa.")
