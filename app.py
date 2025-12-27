import streamlit as st
import pandas as pd
from duckduckgo_search import DDGS # Nova biblioteca mais estável
import instaloader

# --- SEGURANÇA ---
st.set_page_config(page_title="Obs. Salinas", layout="wide")
SENHA_ACESSO = "salinas1969" 

st.title("🏛️ Observatório Salinas da Margarida")
st.caption("Pesquisa Histórica e Econômica | Sérgio")

senha = st.sidebar.text_input("Chave de Acesso:", type="password")

if senha == SENHA_ACESSO:
    aba1, aba2 = st.tabs(["🛒 Comércio (Instagram)", "🌐 Radar Web (Busca)"])

    # --- ABA 1: INSTAGRAM ---
    with aba1:
        st.subheader("Monitoramento de Supermercados")
        if st.button("🚀 Atualizar Redes Sociais"):
            st.warning("Nota: O Instagram pode bloquear acessos vindos da nuvem. Se falhar, use o Radar Web abaixo.")
            try:
                L = instaloader.Instaloader()
                # Tentativa de coleta simplificada para evitar bloqueio
                st.info("Acessando perfis locais...")
                # (Lógica de exibição que já criamos)
            except Exception as e:
                st.error("O Instagram bloqueou a conexão do servidor. Tente novamente mais tarde.")

    # --- ABA 2: RADAR WEB (MAIS ESTÁVEL) ---
    with aba2:
        st.subheader("Hemeroteca Digital em Tempo Real")
        termo = st.text_input("O que pesquisar na web?", value="Salinas da Margarida")
        
        if st.button("🔍 Iniciar Varredura"):
            with st.spinner(f"Buscando menções a '{termo}'..."):
                try:
                    with DDGS() as ddgs:
                        # Busca notícias e sites sobre o tema
                        results = [r for r in ddgs.text(termo, max_results=10)]
                        
                        if results:
                            st.success(f"Encontrei {len(results)} registros!")
                            for r in results:
                                with st.container():
                                    st.markdown(f"### [{r['title']}]({r['href']})")
                                    st.write(r['body'])
                                    st.divider()
                        else:
                            st.warning("Nenhum resultado novo encontrado.")
                except Exception as e:
                    st.error(f"Erro na varredura: {e}")
else:
    st.info("Aguardando Chave de Acesso.")
