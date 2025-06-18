# SATEPSI Scraper

Sistema de monitoramento e extração de dados do SATEPSI (Sistema de Avaliação de Testes Psicológicos) do Conselho Federal de Psicologia.

## 📋 Descrição

Este projeto automatiza a extração e monitoramento de dados dos instrumentos psicológicos cadastrados no SATEPSI. Ele permite:

- Extrair dados diretamente do site do SATEPSI
- Processar e formatar os dados em diferentes formatos (JSON, Excel, Word)
- Monitorar alterações no status dos instrumentos
- Enviar notificações por e-mail quando houver mudanças

## 🚀 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/satepsi-scraper.git
cd satepsi-scraper
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente:
   - Crie um arquivo `.env` na raiz do projeto
   - Adicione as seguintes variáveis:

```env
# Configurações do servidor SMTP
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=seu@email.com
SMTP_PASS=sua_senha_de_app

# Configurações de e-mail
EMAIL_FROM=seu@email.com
EMAIL_TO=destinatario@email.com

# Configurações do SATEPSI
SATEPSI_URL=https://satepsi.cfp.org.br/
```

## 🛠️ Uso

### Execução Básica

Para executar o scraper e gerar relatórios:

```bash
python src/satepsi_scraper.py
```

### Configuração de E-mail

Para receber notificações por e-mail, configure as seguintes variáveis no arquivo `.env`:

```env
SMTP_HOST=seu.servidor.smtp.com
SMTP_PORT=587
SMTP_USER=seu@email.com
SMTP_PASS=sua_senha
EMAIL_FROM=seu@email.com
EMAIL_TO=destinatario@email.com
```

## 📁 Estrutura do Projeto

```
satepsi-scraper/
├── src/
│   ├── satepsi_scraper.py  # Script principal
│   └── config.py           # Configurações
├── data/                   # Dados extraídos
├── docs/                   # Documentação
├── tests/                  # Testes
├── tools/                  # Scripts auxiliares
├── .env                    # Configurações (não versionado)
├── .gitignore             # Arquivos ignorados pelo git
├── README.md              # Este arquivo
└── requirements.txt       # Dependências
```

## 📊 Formatos de Saída

O sistema gera os seguintes arquivos:

- `data/satepsi_data_YYYYMMDD_HHMMSS.json`: Dados em formato JSON
- `data/satepsi_data_YYYYMMDD_HHMMSS.xlsx`: Planilha Excel
- `data/satepsi_report_YYYYMMDD_HHMMSS.docx`: Relatório em Word

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## ⚠️ Aviso Legal

Este projeto é apenas para fins educacionais e de pesquisa. O uso deve respeitar os termos de serviço do SATEPSI e as leis de propriedade intelectual aplicáveis. # satepsi
