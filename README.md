<div align="center">

<h1>🏫 Sistema de Gestão Escolar</h1>

<p>um CRUD completo feito com Django 5 pra gerenciar alunos, turmas e matrículas, com validação de CPF real e tudo que você espera de um sistema de verdade.</p>

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.x-092E20?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=flat&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=flat&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Status](https://img.shields.io/badge/status-concluído-success?style=flat)]()

</div>

---

## sobre o projeto

esse projeto nasceu como atividade do curso técnico em desenvolvimento de sistemas no SENAI, mas acabou indo além disso. a ideia era construir um sistema funcional de gestão escolar do zero, pensando não só em fazer funcionar, mas em fazer direito.

o sistema permite cadastrar alunos com validação de CPF pelo algoritmo oficial, criar turmas, vincular alunos a turmas e gerenciar tudo isso por uma interface limpa e responsiva. tem busca com filtros, paginação, feedback visual com mensagens de sucesso e erro, e um painel home que mostra os totais em tempo real.

foi o meu primeiro projeto Django com um nível de organização que eu me orgulho de mostrar.

---

## funcionalidades

- cadastro, edição e exclusão de alunos, turmas e matrículas
- validação completa de CPF com o algoritmo oficial dos dois dígitos verificadores
- validação de responsável obrigatório para alunos menores de 18 anos
- busca por nome, e-mail e CPF na listagem de alunos
- busca por nome e conteúdo na listagem de turmas
- paginação nas listagens
- painel home com contagem de alunos, turmas e matrículas
- feedback visual com alertas de sucesso e erro em todas as ações
- navbar com destaque da página ativa
- interface responsiva com Bootstrap 5

---

## stack

| camada | tecnologia |
|--------|-----------|
| linguagem | Python 3.12 |
| framework | Django 5.x |
| banco de dados | MySQL 8.0 |
| frontend | Bootstrap 5.3 + Bootstrap Icons |
| conector | mysqlclient |

---

## estrutura do projeto

```
📁 sistema-escolar/
├── 📁 escola/                  # app principal
│   ├── admin.py                # painel admin configurado
│   ├── apps.py
│   ├── forms.py                # formulários com validações customizadas
│   ├── models.py               # Aluno, Turma, TurmaAluno + validador de CPF
│   ├── urls.py                 # rotas do app com namespace
│   └── views.py                # CBVs com mixins de busca e paginação
├── 📁 setup/                   # configurações do projeto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── 📁 templates/               # templates organizados por entidade
│   ├── base.html
│   ├── home.html
│   ├── 📁 alunos/
│   ├── 📁 turma/
│   └── 📁 turma_aluno/
├── .env.example                # variáveis de ambiente necessárias
├── .gitignore
├── manage.py
└── requirements.txt
```

---

## como rodar localmente

### pré-requisitos

- Python 3.10+
- MySQL rodando localmente
- Git

### passo a passo

**1. clone o repositório**
```bash
git clone https://github.com/Paola5858/sistema-escolar.git
cd sistema-escolar
```

**2. crie e ative o ambiente virtual**
```bash
python -m venv venv

# windows
venv\Scripts\activate

# linux/mac
source venv/bin/activate
```

**3. instale as dependências**
```bash
pip install -r requirements.txt
```

**4. configure as variáveis de ambiente**
```bash
cp .env.example .env
```
abra o `.env` e preencha com seus dados locais:
```
SECRET_KEY=sua-chave-secreta-aqui
DB_NAME=escola
DB_USER=root
DB_PASSWORD=sua-senha-aqui
DB_HOST=localhost
DB_PORT=3306
```

**5. crie o banco de dados no MySQL**
```sql
CREATE DATABASE escola CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

**6. rode as migrações**
```bash
python manage.py migrate
```

**7. crie um superusuário (opcional, pra acessar o admin)**
```bash
python manage.py createsuperuser
```

**8. suba o servidor**
```bash
python manage.py runserver
```

acesse em `http://localhost:8000`

---

## decisões técnicas

algumas coisas que fiz com intenção e não por acidente:

**validação de CPF no model e no form** — coloquei a validação nos dois lugares de propósito. o model garante a integridade no banco independente de onde os dados entram. o form garante feedback imediato pro usuário na interface.

**class based views com mixins** — criei um `SearchListView` reutilizável que centraliza a lógica de busca e paginação. cada view de listagem herda dele e só define qual campo filtrar. evita repetição de código sem virar overengineering.

**`select_related` na listagem de matrículas** — `TurmaAluno` referencia `Aluno` e `Turma`. sem `select_related`, cada linha da tabela faria duas queries extras. com ele, tudo vem em uma query só.

**namespace nas urls** — usei `app_name = "escola"` pra que todas as urls fiquem no namespace `escola:`, facilitando manutenção e evitando conflitos se o projeto crescer.

---

## o que aprendi construindo isso

esse foi o projeto onde a ficha realmente caiu sobre como Django funciona de verdade, não só seguindo tutorial. entender o fluxo de uma `ModelForm` com `clean()` customizado, como o ORM resolve relacionamentos, e por que CBVs existem foram as viradas de chave desse projeto.

---

## contato

feito por **Paola Soares Machado**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Paola%20Soares%20Machado-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/paolasoaresmachado)
[![Gmail](https://img.shields.io/badge/Gmail-paolasesi351%40gmail.com-D14836?style=flat&logo=gmail&logoColor=white)](mailto:paolasesi351@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-Paola5858-181717?style=flat&logo=github&logoColor=white)](https://github.com/Paola5858)
