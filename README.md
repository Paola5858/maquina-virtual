# Sistema de Gestão Escolar

Sistema web para gerenciar alunos, turmas e matrículas desenvolvido com Django.

## Funcionalidades

- Cadastro de alunos com validação de CPF
- Gerenciamento de turmas
- Controle de vínculos entre alunos e turmas
- Busca e paginação em todas as listagens
- Interface responsiva com Bootstrap 5

## Requisitos

- Python 3.8+
- MySQL 5.7+

## Instalação

1. Clone o repositório
2. Crie um ambiente virtual:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure o banco de dados no arquivo `setup/settings.py`

5. Execute as migrações:
```bash
python manage.py migrate
```

6. Crie um superusuário:
```bash
python manage.py createsuperuser
```

7. Inicie o servidor:
```bash
python manage.py runserver
```

## Estrutura

```
projeto/
├── escola/          # App principal
├── setup/           # Configurações do Django
├── templates/       # Templates HTML
└── logs/            # Logs da aplicação
```

## Tecnologias

- Django 4.x
- MySQL
- Bootstrap 5
