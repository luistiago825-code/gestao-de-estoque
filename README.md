# Sistema de Gestão Comercial e Estoque 📱

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PySide6](https://img.shields.io/badge/PySide6-41CD52?style=for-the-badge&logo=qt&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

Um sistema de gerenciamento comercial (MVP) focado no controle de estoque de dispositivos móveis, com arquitetura pronta para expansão de módulos de Fluxo de Caixa (PDV), Clientes e Ordens de Serviço (OS). Desenvolvido com **Python**, **PySide6** (Interface Gráfica Moderna) e **SQLite** (Banco de Dados Relacional).

---

## 📌 Funcionalidades (MVP)

- **Gestão de Estoque Funcional:** 
  - Cadastro detalhado de produtos (Marca, Modelo, Armazenamento, RAM, Preço, Quantidade).
  - Validação de entrada de dados.
  - Visualização em tempo real na interface através de tabelas dinâmicas.
- **Banco de Dados Local:** Utiliza SQLite para garantir persistência e integridade dos dados sem necessidade de conexão com a internet.
- **Interface UI/UX Moderna:** Desenvolvido com PySide6 (Qt for Python), apresentando um design responsivo, organizado por abas e estilizado com QSS para uma aparência limpa e profissional.

## 🛠️ Tecnologias Utilizadas

- **Linguagem Base:** Python 3.x
- **Interface Gráfica:** PySide6
- **Banco de Dados:** SQLite (nativo do Python)

## 🚀 Como Executar o Projeto

Siga as instruções abaixo para rodar o projeto localmente em sua máquina.

### 1. Pré-requisitos
Certifique-se de ter o [Python](https://www.python.org/downloads/) instalado (versão 3.8 ou superior).

### 2. Clonar o Repositório
```bash
git clone https://github.com/luistiago825-code/gestao-de-estoque.git
cd gestao-de-estoque.git
```

### 3. Instalar as Dependências
Como o projeto utiliza o PySide6 para a interface gráfica, instale a biblioteca via pip:
```bash
pip install PySide6
```
*(Você também pode usar o comando `pip install -r requirements.txt` se criar esse arquivo).*

### 5. Executar a Aplicação
```bash
python main.py
```
O banco de dados `gestao_comercial.db` será gerado automaticamente na primeira execução e a interface gráfica será aberta.

## 📂 Estrutura do Código
- `main.py`: Arquivo principal contendo toda a lógica de inicialização do banco de dados, configuração da interface gráfica (MainWindow) e as regras de negócio do módulo de estoque.
- `gestao_comercial.db`: Arquivo do banco de dados gerado automaticamente na primeira execução (não incluído no repositório por padrão).

*Desenvolvido como projeto de portfólio para demonstrar habilidades em Python, construção de interfaces modernas (GUI) e modelagem de banco de dados relacional.*
