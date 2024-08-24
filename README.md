PokeMafe é uma aplicação web desenvolvida com Django que permite aos usuários gerenciar informações sobre treinadores de Pokémon e seus Pokémon. A aplicação inclui um sistema de CRUD (Criar, Ler, Atualizar, Deletar) para duas entidades principais e se integra com a PokéAPI para buscar dados atualizados sobre Pokémon.

Visão Geral
O PokeMafe é um projeto Django que fornece uma interface para gerenciar informações sobre treinadores e Pokémon. Utilizando a PokéAPI, a aplicação pode buscar dados atualizados sobre Pokémon, facilitando o gerenciamento e a visualização dessas informações.

Funcionalidades
Gerenciamento de Treinadores:
Adicione, edite e exclua treinadores.
Liste todos os treinadores cadastrados.
Gerenciamento de Pokémon:
Adicione, edite e exclua Pokémon.
Liste todos os Pokémon cadastrados.
Integre com a PokéAPI para obter dados atualizados, como o número da Pokédex e os tipos dos Pokémon.


Instalação
Para instalar e executar o projeto localmente, siga estas etapas:

Clone o repositório: git clone https://github.com/mariwannar/PokeMafe.git

Navegue até o diretório do projeto: cd PokeMafe

Crie um ambiente virtual: python -m venv env

Ative o ambiente virtual:

No Windows: .\env\Scripts\activate
No macOS e Linux: source env/bin/activate

Instale as dependências: pip install freeze > requirements.txt

Configure o banco de dados:

Execute as migrações: python manage.py migrate

Crie um superusuário para acessar o painel administrativo: python manage.py createsuperuser

Inicie o servidor de desenvolvimento: python manage.py runserver

Acesse a aplicação: Abra o navegador e vá para http://127.0.0.1:8000/api.

Após iniciar o servidor, você pode utilizar a aplicação para:

Gerenciar Treinadores:
Acesse a página de treinadores para adicionar, editar ou excluir treinadores.
Gerenciar Pokémon:
Acesse a página de Pokémon para adicionar, editar ou excluir Pokémon.
A aplicação integra-se com a PokéAPI para buscar dados atualizados sobre Pokémon, como o número da Pokédex.