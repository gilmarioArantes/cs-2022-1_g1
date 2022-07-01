# API de Livros

A API está disponibilizada na seguinte URL: **http://livraria.ddns.net:8000**. Para teste do professor, fizemos um usuário administrador com as seguites credenciais:
- Usuário: gilmar.arantes
- Senha: GilmarArantes123@

A autenticação é feita por HTTP Basic Auth e necessita dos parâmetros 'username' e 'password' para que seja feita uma requisição autenticada. 

Exemplo de como fazer uma requisição com as credenciais acima utilizando Python:

Dê um "pip install requests" e, após isso execute o código abaixo:

`import requests

from requests.auth import HTTPBasicAuth

response = requests.get('http://livraria.ddns.net:8000/usuarios/', auth = HTTPBasicAuth('gilmar.arantes', 'GilmarArantes123@'))

print(response.text)`


## Usuários

Endpoints para CRUD de usuários. Esses usuários serão usados para autenticação nos Endpoints da API. Existem três tipos de usuários na aplicação:
- Administradores: podem acessar todos os Endpoints da plataforma;
- Usuários: têm permissão de leitura na maioria dos Endpoints, posteriormente também podendo ter livros favoritos. 
- Visitantes: têm permissão apenas de leitura nos Endpoints de Livros e Autores. Também podem criar um Usuário para eles acessarem como usuários.

Os níveis de permissão de cada Endpoint será tratado adiante mais especificamente.

### /usuarios/
Com um GET retorna a listagem de todos os Usuários cadastrados. Apenas Administradores podem usar esse Endpoint.

### /adicionar-usuario/
Com um POST adiciona um usuário. Apenas Administradores podem adicionar usuários Administradores, visitantes podem cadastrar usuários normais, assim como usuários também.
O parâmetro que define o Administrador é o "is_superuser".

Exemplo de corpo da requisição:

{
    'username': 'usuario2',
    'password': 'Testando123@',
    'email': 'usuario2@gmail.com',
    'is_superuser': false,
    'first_name': 'Nome',
    'last_name': 'Usuário',
}


### /usuarios/_id-do-usuario_/
Com um GET retorna dados sobre o usuário com o ID especificado. Um visitante não tem acesso a esse Endpoint. Um usuário comum só pode retornar dados sobre ele mesmo. Um administrador pode retornar dados de quem ele quiser.

### /deletar-usuario/_id-do-usuario_/
Com um DELETE deleta o usuário de ID especificado. Um visitante não pode usar esse endpoint. Um usuário comum só pode deletar ele mesmo. Um Administrador pode deletar quem ele quiser.

### /editar-usuario/_id-do-usuario_/
Com um PUT edita o usuário com ID especificado. O valor de um ou mais campos podem ser passados na requisição. Um usuário comum não deve ser capaz de editar administradores ou tornar usuários comuns administradores.

## Autores

Endpoints para CRUD de autores, que posteriormente serão atribuídos aos livros na hora de cadastrar os livros.

### /autores/ 
Com um GET retorna a listagem de todos os Autores cadastrados. Todos os usuários (Administradores, usuários e visitantes) podem usar esse Endpoint.

### /adicionar-autor/
Com um POST cadastra um Autor na plataforma. Apenas Administradores são autorizados a usar esse Endpoint.

Modelo de Requisição aceita:

{
    'nome': 'Ricardo Almeida',
    'data_nascimento': '2000-01-01',
}

### /autores/_uuid-do-autor_/
Com um GET retorna dados do autor de uuid especificado. Todos os usuários (Administradores, usuários e visitantes) conseguem utilizar esse Endpoint.

### /deletar-autor/_uuid-do-autor_/
Com um DELETE deleta o autor de uuid especificado. Apenas Administradores devem ser capazes de utilizar esse Endpoint.

### /editar-autor/_uuid-do-autor_/
Com um PUT faz update do autor de uuid especificado. Apenas Administradores devem ser capazes de utilizar esse endpoint. O corpo da requisição deve conter um ou mais campos de Autor. Por exemplo, uma requisição {'nome': 'Fulano de Tal'} irá atualizar o nome do Autor de uuid especificado para "Fulano de Tal".

## Livros
Endpoints para CRUD de livros.

### /livros/
Com um GET retorna todos os livros cadastrados. Endpoint acessível a todos os tipos de usuários (Administradores, visitantes e usuários comuns).

### /adicionar-livro/
Com um POST adiciona um livro conforme dados enviados no corpo da requisição. Apenas administradores podem adicionar livros.

Exemplo de corpo da requisição em Python:

{
    "titulo": "titulo1",
    "numero_paginas": 500,
    "data_publicacao": "2022-06-29",
    "descricao": "descricao",
    'thumbnail': open('teste.jpg', 'rb'),
    "local_publicacao": "Brasil",
    "categorias": ['Escrita e Publicação', 'Casamentos'],
    "autores": [
        _uuid-do-autor_
    ]}

### /livros/_uuid-do-livro_/
Com um GET retorna o livro com uuid especificado. Todos os usuários têm acesso a esse Endpoint.

### /deletar-livro/_uuid-do-livro_/
Com um DELETE deleta o livro com uuid especificado. Apenas administradores podem deletar livros.

### /editar-livro/_uuid-do-livro_/
Com um PUT edita o livro em questão. Apenas administradores podem editar livros.
