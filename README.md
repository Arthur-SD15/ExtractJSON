<h1 align="center">
  ExtractJSON
</h1>

<p align="center">
  <a href="#-Projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-Pré-requesitos">Pré-requesitos</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-Executar Projeto">Executar</a>
</p>

## 💻 Projeto

O projeto desenvolvido neste repositório é uma aplicação web que visa atender à necessidade de extrair informações de grandes arquivos JSON com base em seus atributos. A aplicação permite a listagem e exportação automatizada desses dados para uma planilha, de acordo com as configurações definidas pelo usuário.

Para a implementação da aplicação, foram utilizados React.js e Next.js. A estilização foi realizada com Tailwind CSS, já a comunicação com o back-end é feita por meio da API Fetch, garantindo uma integração eficiente entre o cliente e o servidor.

No back-end, foram empregados conceitos de manipulação de dados e desenvolvimento de APIs com Flask. O Flask foi escolhido devido à sua capacidade de criar APIs RESTful de forma eficiente, adaptando-se perfeitamente ao processamento e gerenciamento de arquivos JSON.

A aplicação oferece funcionalidades de upload, processamento e exportação de dados. Para processar arquivos JSON, utiliza-se a biblioteca padrão do Python para manipulação de JSON, permitindo a leitura e extração de informações específicas. A exportação dos dados filtrados para o formato Excel (.xlsx) é realizada com a biblioteca pandas, facilitando a análise e o compartilhamento das informações.


## 📝 Pré-requesitos

Antes de baixar o projeto você vai precisar ter instalado na sua máquina as seguintes ferramentas:

- [Git](https://git-scm.com)
- [NodeJS](https://nodejs.org/en/)
- [NPM](https://www.npmjs.com/)
  - [NextJS](https://nextjs.org/)
  - [React](https://react.dev/)
- [Python](https://www.python.org/)
- [Pip](https://pip.pypa.io/en/stable/installation/)
  - [Flask](https://flask.palletsprojects.com/en/3.0.x/)
  - [Pandas](https://pandas.pydata.org/)


## 🗂 Executar Projeto

```bash
# Clonar Projeto.
$ git clone https://github.com/Arthur-SD15/ExtractJSON.git

# Entrar na pasta backend.
$ cd backend

# Criar um ambiente virtual Python.
$ python3 -m venv venv

# Ativar o ambiente virtual no Linux/Mac.
$ source venv/bin/activate

# Ativar o ambiente virtual no Windows.
$ .\venv\Scripts\activate

# Instalar a biblioteca pandas.
$ pip install pandas

# Crie o arquivo requirements.txt.
# Instalar as dependências listadas no arquivo requirements.txt.
$ pip install -r requirements.txt

# Instalar a extensão Flask-CORS.
$ pip install flask-cors

# Executar.
$ python3 app.py

# Novo terminal.
# Entrar na pasta frontend.
$ cd frontend

# Baixar as dependências.
$ npm install

# Executar.
$ npm run dev

 ```

