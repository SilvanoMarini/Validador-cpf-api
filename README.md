# API Validadora de CPF

Este projeto oferece uma API simples para validar números de CPF. A API realiza a verificação do CPF para garantir que ele seja válido de acordo com as regras estabelecidas pela Receita Federal do Brasil. A validação inclui a verificação do formato e dos dígitos verificadores.

Funcionalidades

Validação de CPF: A API valida se um CPF informado é válido, levando em consideração o formato correto e os cálculos de dígitos verificadores.

Formato: A API verifica se o CPF está no formato XXX.XXX.XXX-XX ou apenas XXXXXXXXXXX.

Resposta: A resposta indica se o CPF é válido ou inválido, e pode fornecer uma mensagem de erro se o CPF estiver no formato incorreto.


Endpoints

1. Validação de CPF

URL: /api/validate-cpf

Método: GET

Parâmetros de consulta:

cpf (obrigatório): O número do CPF a ser validado.


Exemplo de requisição:

GET /api/validate-cpf?cpf=123.456.789-09

Resposta bem-sucedida (status 200):

{
  "cpf": "123.456.789-09",
  "valid": true,
  "message": "CPF válido."
}

Resposta de erro (status 400):

{
  "error": "CPF inválido."
}

Resposta de erro (status 400 - formato incorreto):

{
  "error": "Formato de CPF inválido."
}

Como rodar a API

Pré-requisitos

Python 3.7 ou superior

Passo a passo para rodar a API:

1. Clone este repositório:

git clone https://github.com/seu-usuario/validador-cpf-api.git


2. Acesse o diretório do projeto:

cd validador-cpf-api


3. Instale as dependências:

pip install -r requirements.txt

4. Inicie o servidor:

python app.py


5. A API estará disponível em http://127.0.0.1:5000.

Testando a API

Você pode testar a API usando ferramentas como Postman ou cURL. Por exemplo, para testar no terminal com curl:

curl "http://127.0.0.1:5000/api/validate-cpf?cpf=123.456.789-09"

Contribuindo

Se você deseja contribuir para este projeto, fique à vontade para enviar pull requests. Certifique-se de seguir as seguintes diretrizes:

1. Crie uma branch para sua feature (git checkout -b feature/nome-da-feature).


2. Commit suas alterações (git commit -am 'Adicionando nova feature').


3. Envie para o repositório remoto (git push origin feature/nome-da-feature).


4. Abra um pull request.


Licença

Este projeto está licenciado sob a MIT License.
