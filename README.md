# Organizador de Estudos

Sistema web desenvolvido como MVP para ajudar estudantes a organizar suas atividades de estudo.

## Tecnologias utilizadas

- Python
- Django
- SQLite
- HTML e CSS

## Funcionalidades implementadas

- Cadastro de usuários;
- Login e logout;
- Criação de tarefas;
- Listagem de tarefas;
- Marcação de tarefas como concluídas;
- Exclusão de tarefas.

## Organização do projeto

O sistema utiliza a arquitetura MVT do Django:

- **Models:** representam os dados e sua estrutura no banco de dados.
- **Views:** controlam as operações e regras da aplicação.
- **Templates:** apresentam as páginas para o usuário.
- **Forms:** realizam a validação dos dados enviados.

## Segurança

O sistema utiliza autenticação para proteger as páginas de tarefas, validação de formulários do Django e proteção CSRF nos formulários enviados por POST. As operações de alteração e exclusão verificam se a tarefa pertence ao usuário autenticado.

## Execução local

1. Ative o ambiente virtual.
2. Instale as dependências do projeto.
3. Execute as migrações com `python manage.py migrate`.
4. Inicie o servidor com `python manage.py runserver`.
