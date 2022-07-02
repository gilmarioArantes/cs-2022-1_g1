### ***cs-2022-1_g1***
Repositório definido para a manutenção do controle de versão dos artefatos gerados pelo **Grupo 1** na construção de uma API REST, durante o curso da disciplina **Construção de Software**, do quinto período do curso de **Engenharia de Software**, do **INF/UFG**, no semestre 2022/1.

### ***Descrição do Produto***: 

Desenvolvimento de uma API REST para gerenciamento de livros em uma biblioteca. Os livros podem ter categorias  (Ex: romance, ação, etc...). As propriedades de cada livro são: título, número de páginas, data de publicação, descrição, status (publicado, não  publicado, etc...), categorias, thumbnail e autor(es). 

### ***Requisitos***:
1. Requisito/funcionalidade:

> Login / O Web Service cuja interface será definida por tal REST API deve permitir dois tipos usuários; 
> 
> * Tipo de usuário visitante, que pode buscar os dados das obras. 
> * Tipo de usuário administrador, que pode, além de buscar e ler, editar e os dados das obras.
>
>Obs: um usuário do tipo administrador só pode ser criado a partir de outro administrador previamente cadastrado.

2. Requisito/funcionalidade: 

> Favoritos / Os usuários podem favoritar e desfavoritar obras e buscar somente pelas obras favoritadas.

3. Requisito/funcionalidade: 

> Buscas Populares / O Web Service deve permitir que os usuários busquem pelas obras mais visualizadas ou favoritadas do dia ou desde quando a aplicação foi iniciada.

4. Requisito/funcionalidade: 

> Ocultar visualização / Um usuário administrador pode esconder um certo livro, de modo que ela não apareça nas buscas dos usuários visitantes.

5. Requisito/funcionalidade: 

> Visualizar dados dos favoritos / O Web Service deve manter estatísticas das obras e autores mais visualizados e favoritados, para posterior análise dos dados para auxiliar a estratégia da livraria quanto a exposição física de seu acervo.

### ***Tecnologia empregada no desenvolvimento:*** 

> Será utilizado Python com o framework Django.

### ***Banco de Dados:***

> PostgreSQL.

### ***Local de deploy***:

> Servidor local dos integrantes: http://livraria.ddns.net:8000

### Participantes:

|#|Nome|Usuário|Papel|
|---|---|---|---|
|1|ADRIEL LENNER VINHAL MORI|[adrielmori](https://github.com/adrielmori)| Líder - 3. Buscar Populares |
|2|GABRIEL PIRES DE CAMPOS REZENDE|[Gabriel-Rezende](https://github.com/Gabriel-Rezende)|  1. Login  |
|3|KARLOS DANIEL PIRES DA SILVA|[karlosdaniel451](https://github.com/karlosdaniel451)|  5. Visualizar dados dos favoritos  |
|4|NATHAN LUIS COELHO CAMPOS|[NathanCamposss](https://github.com/NathanCamposss)|  4. Ocultar visualização  |
|5|PAULO ROBERTO VIEIRA|[PauloRobertoVieira](https://github.com/PauloRobertoVieira)|  2. Favoritos  |


### Cronograma:
|Sprint|Atividade|Responsável|Início|Fim|Situação|Avaliação|
|---|---|---|---|---|---|---|
|1|Formação de Grupos. Definição de Temas|Equipe|03/06/2022|17/06/2022|Concluída|22/06/2022|
|2|Implementação do Requisito 01|Equipe|18/06/2022|01/07/2022|Em Andamento|06/07/2022|
|3|Implementação do Requisito 02|Equipe|02/07/2022|15/07/2022|A fazer|20/07/2022|
|4|Implementação do Requisito 03|Equipe|16/07/2022|29/07/2022|A fazer|03/08/2022|
|5|Implementação do Requisito 04|Equipe|30/07/2022|12/08/2022|A fazer|17/08/2022|
|6|Implementação do Requisito 05|Equipe|13/08/2022|26/08/2022|A fazer|31/08/2022|
