```md
# Garantia Digital – Salesforce Analyzer

Projeto em Python para conectar em uma org Salesforce, extrair registros do objeto personalizado **Garantia__c**, aplicar regras de negócio e exportar os dados para um arquivo CSV.

Este projeto simula um cenário real de integração e análise de dados, muito comum em contextos de automação, relatórios e apoio a decisões de negócio.

---

## 📂 Estrutura do Projeto

```

garantiadigital-salesforce-analyzer
├── src
│   ├── auth.py        # Responsável pela autenticação no Salesforce
│   └── main.py        # Script principal (consulta, regra de negócio e exportação)
├── reports
│   └── garantias.csv  # Arquivo CSV gerado automaticamente
├── requirements.txt   # Dependências do projeto
├── .env.example       # Exemplo de variáveis de ambiente
├── .gitignore         # Arquivos ignorados pelo Git
└── README.md          # Documentação do projeto

````

---

## ⚙️ Pré-requisitos

- Python 3.9+
- Acesso a uma org Salesforce (Sandbox ou Produção)
- Objeto personalizado **Garantia__c** configurado na org
- Campos utilizados:
  - `Name`
  - `Status_da_garantia__c`
  - `Data_de_emissao__c`
  - `Data_de_vencimento__c`
  - Relacionamento com `Servico__c` (`Servico__r.Name`)

---

## 🚀 Instalação

1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   cd garantiadigital-salesforce-analyzer
````

2. (Opcional, recomendado) Crie um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / macOS
   venv\Scripts\activate      # Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente:

   ```bash
   cp .env.example .env
   ```

   Preencha o arquivo `.env` com suas credenciais do Salesforce.

---

## ▶️ Como Executar

Execute o script principal:

```bash
python src/main.py
```

Ao final da execução, o arquivo abaixo será gerado automaticamente:

```
reports/garantias.csv
```

---

## 📊 Regras de Negócio

* A garantia é classificada como **ACTIVE** quando a data de vencimento é igual ou maior que a data atual.
* A garantia é classificada como **EXPIRED** quando a data de vencimento é anterior à data atual.
* Caso a data de vencimento esteja vazia ou inválida, o status será **UNKNOWN**.

---

## 🧠 Tecnologias Utilizadas

* Python
* simple-salesforce
* python-dotenv
* Salesforce SOQL
* CSV para exportação de dados

---

## 📌 Objetivo do Projeto

* Demonstrar integração com Salesforce via API
* Aplicar regras de negócio fora da plataforma
* Automatizar extração e geração de relatórios
* Servir como projeto de portfólio técnico

---

## 📄 Licença

Este projeto está licenciado sob a licença MIT.

```