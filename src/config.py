"""
Configurações centralizadas do projeto SATEPSI.

Este módulo gerencia todas as configurações do projeto, incluindo:
- Caminhos de arquivos e diretórios
- Configurações de e-mail
- Mapeamento de campos
- URLs e endpoints
- Funções auxiliares para gerenciamento de arquivos

Exemplo de uso:
    >>> from config import DATA_DIR, SATEPSI_URL
    >>> from config import get_timestamp_filename
    >>> 
    >>> # Obter caminho para um novo arquivo de dados
    >>> data_file = get_timestamp_filename("dados", "json")
    >>> print(f"Arquivo será salvo em: {data_file}")
"""

import os
from pathlib import Path
from typing import Dict, Any, List
from dotenv import load_dotenv
from datetime import datetime

# ── DIRETÓRIOS BASE ───────────────────────────────────────────────────────────
# Obtém o diretório raiz do projeto (dois níveis acima deste arquivo)
BASE_DIR = Path(__file__).parent.parent

# Diretórios principais do projeto
SRC_DIR = BASE_DIR / "src"      # Código fonte
DATA_DIR = BASE_DIR / "data"    # Arquivos de dados
DOCS_DIR = BASE_DIR / "docs"    # Documentação
TESTS_DIR = BASE_DIR / "tests"  # Testes
TOOLS_DIR = BASE_DIR / "tools"  # Ferramentas auxiliares

# ── ARQUIVOS DE CONFIGURAÇÃO ──────────────────────────────────────────────────
# Arquivos de configuração do projeto
ENV_FILE = BASE_DIR / ".env"           # Variáveis de ambiente
REQUIREMENTS_FILE = BASE_DIR / "requirements.txt"  # Dependências Python

# ── ARQUIVOS DE DADOS ─────────────────────────────────────────────────────────
# Arquivos de dados principais do SATEPSI
PREVIOUS_DATA_FILE = DATA_DIR / "previous_data.json"  # Histórico de dados
INSTRUMENTS_FILE = DATA_DIR / "satepsi_instruments.xlsx"  # Lista completa de instrumentos
TITLES_STATUS_FILE = DATA_DIR / "titulos_status.xlsx"  # Status dos títulos
TITLES_STATUS_TXT = DATA_DIR / "titulos_status.txt"  # Status dos títulos (texto)
INSTRUMENTS_EXPLAINED = DATA_DIR / "instrumentos_explicados.xlsx"  # Instrumentos com explicações

# ── ARQUIVOS DE DOCUMENTAÇÃO ──────────────────────────────────────────────────
# Arquivos de documentação do projeto
README_FILE = DOCS_DIR / "README.md"  # Documentação principal
INSTRUCTIONS_FILE = DOCS_DIR / "INSTRUCOES.md"  # Instruções de uso

# ── ARQUIVOS DE FERRAMENTAS ───────────────────────────────────────────────────
# Ferramentas auxiliares do projeto
CHROMEDRIVER_FILE = TOOLS_DIR / "chromedriver.exe"  # Driver do Chrome para Selenium
DOWNLOAD_CHROMEDRIVER_SCRIPT = TOOLS_DIR / "download_chromedriver.ps1"  # Script de download do ChromeDriver

# ── CONFIGURAÇÕES DO SATEPSI ──────────────────────────────────────────────────
# URL base do sistema SATEPSI
SATEPSI_URL = "https://satepsi.cfp.org.br/"

# Mapeamento de campos do SATEPSI para o formato interno
FIELD_MAP = {
    "Status": "Status",
    "Autores": "Autores",
    "Editora": "Editora",
    "Construto": "Construto",
    "Público-alvo": "PublicoAlvo",
    "Idade da amostra": "IdadeAmostra",
    "Aplicação": "Aplicacao",
    "Correção": "Correcao",
    "Data de aprovação": "DataAprovacao",
    "Prazo dos estudos de validade": "PrazoEstudos",
    "Observações": "Observacoes"
}

# ── CONFIGURAÇÕES DE E-MAIL ───────────────────────────────────────────────────
def load_email_config() -> Dict[str, Any]:
    """
    Carrega as configurações de e-mail do arquivo .env.
    
    Returns:
        Dict[str, Any]: Dicionário com as configurações de e-mail:
            - SMTP_HOST: Servidor SMTP
            - SMTP_PORT: Porta SMTP
            - SMTP_USER: Usuário SMTP
            - SMTP_PASS: Senha SMTP
            - EMAIL_FROM: E-mail de origem
            - EMAIL_TO: E-mail de destino
            
    Raises:
        ValueError: Se alguma configuração obrigatória estiver faltando
    """
    load_dotenv(ENV_FILE)
    
    config = {
        "SMTP_HOST": os.getenv("SMTP_HOST"),
        "SMTP_PORT": int(os.getenv("SMTP_PORT", "587")),
        "SMTP_USER": os.getenv("SMTP_USER"),
        "SMTP_PASS": os.getenv("SMTP_PASS"),
        "EMAIL_FROM": os.getenv("EMAIL_FROM"),
        "EMAIL_TO": os.getenv("EMAIL_TO"),
    }
    
    # Verifica se todas as configurações necessárias estão presentes
    missing = [k for k, v in config.items() if not v]
    if missing:
        raise ValueError(f"Configurações de e-mail faltando: {', '.join(missing)}")
    
    return config

# ── FUNÇÕES AUXILIARES ────────────────────────────────────────────────────────
def ensure_directories() -> None:
    """
    Garante que todos os diretórios necessários existam.
    
    Cria os seguintes diretórios se não existirem:
    - src/: Código fonte
    - data/: Arquivos de dados
    - docs/: Documentação
    - tests/: Testes
    - tools/: Ferramentas auxiliares
    """
    for directory in [SRC_DIR, DATA_DIR, DOCS_DIR, TESTS_DIR, TOOLS_DIR]:
        directory.mkdir(exist_ok=True)

def get_timestamp_filename(prefix: str, extension: str) -> Path:
    """
    Gera um nome de arquivo com timestamp.
    
    Args:
        prefix (str): Prefixo do nome do arquivo
        extension (str): Extensão do arquivo (sem o ponto)
        
    Returns:
        Path: Caminho completo do arquivo
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return DATA_DIR / f"{prefix}_{timestamp}.{extension}"

# ── INICIALIZAÇÃO ─────────────────────────────────────────────────────────────
# Garante que todos os diretórios existam
ensure_directories()

# Carrega configurações de e-mail
try:
    EMAIL_CONFIG = load_email_config()
except ValueError as e:
    print(f"⚠️ Aviso: {e}")
    EMAIL_CONFIG = {} 