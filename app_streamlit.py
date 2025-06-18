import streamlit as st
import pandas as pd
from pathlib import Path
import os
import subprocess

st.set_page_config(page_title="SATEPSI - Consulta de Testes", layout="wide")
st.title("Consulta de Testes SATEPSI")

# Função para atualizar o EMAIL_TO no .env
def update_email_to(new_email, env_path=".env"):
    if not os.path.exists(env_path):
        st.error(f"Arquivo {env_path} não encontrado!")
        return False
    lines = []
    found = False
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip().startswith("EMAIL_TO="):
                lines.append(f"EMAIL_TO={new_email}\n")
                found = True
            else:
                lines.append(line)
    if not found:
        lines.append(f"EMAIL_TO={new_email}\n")
    with open(env_path, "w", encoding="utf-8") as f:
        f.writelines(lines)
    return True

# Campo para inscrição de e-mail SEMPRE visível
st.markdown("---")
st.subheader("Receba atualizações mensais por e-mail")
with st.form("form_email"):
    user_email = st.text_input("Digite seu e-mail para receber atualizações:")
    submitted = st.form_submit_button("Inscrever e salvar no sistema")
    if submitted:
        if user_email and "@" in user_email:
            ok = update_email_to(user_email)
            if ok:
                st.success(f"E-mail {user_email} cadastrado com sucesso! Você receberá as próximas atualizações.")
            else:
                st.error("Erro ao atualizar o arquivo .env!")
        else:
            st.warning("Digite um e-mail válido.")

# Botão para rodar o scraper
st.markdown("---")
st.subheader("Atualizar dados agora")
if st.button("Iniciar nova atualização dos dados SATEPSI"):
    with st.spinner("Executando atualização, aguarde..."):
        result = subprocess.run(["python", "src/satepsi_scraper.py"], capture_output=True, text=True)
        if result.returncode == 0:
            st.success("Atualização concluída com sucesso!")
        else:
            st.error(f"Erro ao executar o scraper:\n{result.stderr}")

# Função para encontrar o arquivo Excel mais recente
def get_latest_excel(data_dir):
    files = list(Path(data_dir).glob("satepsi_data_*.xlsx"))
    if not files:
        st.warning("Nenhum arquivo de dados encontrado na pasta 'data/'. Clique no botão acima para atualizar.")
        return None
    latest = max(files, key=lambda f: f.stat().st_mtime)
    return latest

# Carregar dados
data_dir = Path("data")
latest_excel = get_latest_excel(data_dir)
if latest_excel:
    df = pd.read_excel(latest_excel)
    st.success(f"Dados carregados de: {latest_excel.name}")
    # Campo de pesquisa
    txt = st.text_input("Pesquisar por qualquer campo:")
    # Filtrar dados
    def search_df(df, query):
        if not query:
            return df
        query = query.lower()
        mask = df.apply(lambda row: row.astype(str).str.lower().str.contains(query).any(), axis=1)
        return df[mask]
    filtered_df = search_df(df, txt)
    st.write(f"Exibindo {len(filtered_df)} de {len(df)} testes.")
    st.dataframe(filtered_df, use_container_width=True) 