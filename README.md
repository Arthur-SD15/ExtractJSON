<h1 align="center">
  ExtractJSON
</h1>

<p align="center">
  <a href="#-Projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-Configurar">Configurar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-Executar Projeto">Executar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-ExtractJSON-API">ExtractJSON-API</a>
</p>

## 💻 Projeto

O projeto desenvolvido neste repositório é uma aplicação web que visa atender à necessidade de extrair informações de grandes arquivos JSON com base em seus atributos. A aplicação permite a listagem e exportação automatizada desses dados para uma planilha, de acordo com as configurações definidas pelo usuário.

Para a implementação da aplicação, foram utilizados React.js e Next.js. A estilização foi realizada com Tailwind CSS, já a comunicação com o back-end é feita por meio da API Fetch, garantindo uma integração eficiente entre o cliente e o servidor.

A aplicação oferece funcionalidades de upload, processamento e exportação de dados. Para processar arquivos JSON, utiliza-se a biblioteca padrão do Python para manipulação de JSON, permitindo a leitura e extração de informações específicas. A exportação dos dados filtrados para o formato Excel (.xlsx) é realizada com a biblioteca pandas, facilitando a análise e o compartilhamento das informações.


## ⚙️ Configurar

Antes de exportar, é necessário configurar quais campos são necessários no JSON, seguindo uma ordem de hierarquia.

Para configurar os atributos e possibilitar a listagem das informações, é necessário preencher os níveis de atributos de baixo para cima. Certifique-se de definir todos os níveis necessários para extrair as informações do JSON corretamente. Você deve adicionar o número do índice no caminho quando você deseja acessar um item de um array em uma estrutura JSON.

```json
[
    {
      "id": "b87718c3-1101-4d04-9488-952d3afb2f16",
      "code": null,
      "summary": null,
      "researchProject": null,
      "students": [
        {
          "id": "fa39709c-283f-4f07-81fb-a4369b3817c4",
          "student": {
            "id": "d881cfb0-6243-4253-b4ed-7b28f9f945d5",
            "institutionId": "12a1c659-9688-41f9-8236-8bd97a559047",
            "institution": {
              "id": "12a1c659-9688-41f9-8236-8bd97a559047",
              "name": null,
              "address": {
                "id": "dbd488e2-df6c-420d-b4e9-b795244c7fd4",
                "number": "000",
                "street": "XXXXXXXXXXXXXXXX",
                "neighborhood": "XXXXXXXXXXX",
                "city": "Campo Grande",
                "state": "MS",
                "postalCode": "00000-00",
                "country": "BR",
                "additionalAddress": null
              },
              "academics": [{
                "id": "d881cfb0-6243-4253-b4ed-7b28f9f945d5",
                "name": "XXXXXXXXXXXXXXXX"
              },
              {
                "id": "d881cfb0-6243-4253-b4ed-7b28f9f945d5",
                "name": "XXXXXXXXXXXXXXXX"
              }]
            }
          }
        }
      ]
    }
]
```

Para acessar a cidade, você deve preencher os seguintes níveis de atributos:

- students
- student
- institution
- address
- city

Se você está lidando com um array em qualquer nível da sua estrutura JSON e deseja acessar algum item desse array, você deve usar o índice.

- students
- student
- institution
- academics
- 0
- name


## 🗂 Executar Projeto

```bash
# Entrar na pasta frontend.
$ cd frontend

# Baixar as dependências.
$ npm install

# Executar.
$ npm run dev
 ```


## 🌐 ExtractJSON-API

Visite em: https://github.com/Arthur-SD15/ExtractJson-API
