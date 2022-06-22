### Descrição do Produto: Desenvolvimento de uma API REST para gerenciamento de livros em uma biblioteca. Os livros podem ter categorias  (Ex: romance, ação, etc...). As propriedades de cada livro são: título, número de páginas, data de publicação, descrição, status (publicado, não  publicado, etc...), categorias, thumbnail e autor(es). 

#### Requisitos:
1. Requisito/funcionalidade:Login / O Web Service cuja interface será definida por tal REST API deve permitir dois tipos usuários:

- Tipo de usuário visitante, que pode buscar os dados das obras.

- Tipo de usuário administrador, que pode, além de buscar e ler, editar e os dados das obras.
Obs: um usuário do tipo administrador só pode ser criado a partir de outro administrador previamente cadastrado.

2. Requisito/funcionalidade: Favoritos / Os usuários podem favoritar e desfavoritar obras e buscar somente pelas obras favoritadas.

3. Requisito/funcionalidade: Buscas Populares / O Web Service deve permitir que os usuários busquem pelas obras mais visualizadas ou favoritadas do dia ou desde quando a aplicação foi iniciada.

4. Requisito/funcionalidade: Ocultar visualização / Um usuário administrador pode esconder um certo livro, de modo que ela não apareça nas buscas dos usuários visitantes.

5. Requisito/funcionalidade: Visualizar dados dos favoritos / O Web Service deve manter estatísticas das obras e autores mais visualizados e favoritados, para posterior análise dos dados para auxiliar a estratégia da livraria quanto a exposição física de seu acervo.

### Tecnologia empregada no desenvolvimento: Será utilizado Python com o framework Django

### Banco de Dados: PostgreSQL

### Local de deploy: