# 📄 capelao.bet

## 📌 Descrição Geral

**capelao.bet** é uma aplicação web que simula um sistema de apostas em eventos (e também o jogo do bicho), com interface para usuários, administradores e controle de apostas. O projeto segue o padrão MVC (Model-View-Controller), organizado em Python, utilizando bibliotecas leves e estrutura modular.

---

## ✅ Funcionalidades Implementadas

### 👥 Usuários
- Cadastro e autenticação de usuários.
- Tela principal de navegação.
- Acesso a eventos disponíveis para aposta.

### 🐒 Apostas
- Criação de apostas com base nos eventos.
- Armazenamento e listagem de apostas feitas.

### 🛠️ Administração
- Interface de administração (`admin.html`) com visualização de usuários, apostas e resultados.
- Funções para sorteio e geração de resultados.
- Cadastro e gerenciamento de eventos.

### 📊 Eventos
- Registro de novos eventos.
- Controle de eventos ativos e já finalizados.

---

## ⚙️ Instruções para Execução

### ✅ Pré-requisitos

- Python 3.8 ou superior instalado
- Instalar as dependências necessárias (se aplicável)

### 📁 Estrutura Principal

```
capelao.bet-main/
│
├── main.py                 # Arquivo principal para execução
├── config.py               # Configurações do sistema
├── controller/             # Controladores de lógica da aplicação
├── models/                 # Estrutura dos dados (apostas, eventos, usuários)
├── view/                   # Interface do usuário (HTML/CSS/JS)
```

### ▶️ Passos para executar o projeto

1. **Clonar ou descompactar o projeto**  
   Se ainda não o fez:
   ```bash
   unzip capelao.bet-main.zip
   cd capelao.bet-main
   ```

2. **(Opcional) Criar ambiente virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Instalar dependências (se houver `requirements.txt`)**
   ```bash
   pip install -r requirements.txt
   ```

4. **Executar o projeto**
   ```bash
   python main.py
   ```

5. **Acessar no navegador**
   ```
   http://localhost:5000/
   ```

---

