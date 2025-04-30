# 👾 API LevelCode

Uma API RESTful desenvolvida com **Flask** para **plataforma de aprendizado em programação**

## 🚀 Tecnologias Utilizadas

- [Flask](https://flask.palletsprojects.com/)
- [SQLite](https://www.sqlite.org/index.html)
- [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/)
- [Flask-Limiter](https://flask-limiter.readthedocs.io/)
- [Werkzeug](https://werkzeug.palletsprojects.com/)

---

## 🔧 Funcionalidades

- ✅ Registro e login de usuários
- ✅ Registro de Cursos, Modulos, Aulas, Desafios, Conquistas, 
- ✅ Geração de tokens JWT para autenticação, com roles para permissão de usuarios embutidos a funções
- ✅ Usuario consegue se inscrever em cursos, fazer aulas, que dao xp, e vao subindo o seu nivel te dando ranks que comprovam que voce é experiente na plataforma

---

## 📦 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/dulobodev/API_LevelCode.git
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute o servidor:
```bash
python app.py
```
---


## 📮 Endpoints da API

### 🔐 Autenticação (Admin e Usuário)

| Método | Rota              | Descrição                        |
|--------|-------------------|----------------------------------|
| POST   | `/admin/login`    | Login de administrador           |
| POST   | `/user/login`     | Login de usuário (gera JWT)      |
| POST   | `/admin/register` | Registro de administrador        |
| POST   | `/user/register`  | Registro de usuário              |

---

### 🛡️ Permissões e Papéis (Admin)

| Método | Rota                | Descrição                         |
|--------|---------------------|-----------------------------------|
| POST   | `/permissions`      | Registrar permissões              |
| POST   | `/roles`            | Registrar papel (role)            |
| GET    | `/roles_get`        | Listar papéis                     |

---

### 🎓 Cursos

| Método | Rota               | Descrição                              |
|--------|--------------------|----------------------------------------|
| POST   | `/curso/register`  | Registrar curso                        |
| POST   | `/curso/concluir`  | Concluir aula (JWT + permissão admin) |
| GET    | `/curso/get`       | Listar cursos                          |

---

### 📚 Módulos

| Método | Rota                | Descrição                              |
|--------|---------------------|----------------------------------------|
| POST   | `/modulo/register`  | Registrar módulo (JWT + permissão)     |
| GET    | `/modulo/get`       | Listar módulos                         |

---

### 🧠 Aulas

| Método | Rota              | Descrição          |
|--------|-------------------|--------------------|
| POST   | `/aula/register`  | Registrar aula     |
| GET    | `/aula/get`       | Listar aulas       |

---

### 🏅 Conquistas

| Método | Rota                   | Descrição                        |
|--------|------------------------|----------------------------------|
| POST   | `/conquista/register`  | Registrar conquista              |
| POST   | `/conquista/adicionar` | Adicionar conquista ao usuário   |
| GET    | `/conquista/get`       | Listar conquistas                |

---

### 🎯 Desafios

| Método | Rota                 | Descrição             |
|--------|----------------------|-----------------------|
| POST   | `/desafio/register`  | Registrar desafio     |
| GET    | `/desafio/get`       | Listar desafios       |

---

### 🏆 Rankings

| Método | Rota                | Descrição              |
|--------|---------------------|------------------------|
| POST   | `/ranking/register` | Registrar ranking      |
| GET    | `/ranking/get`      | Listar rankings        |


## 🧪 Testando a API

Você pode testar com:

Postman

Insomnia

---

 ## 🤝 Contribuição
 Sinta-se à vontade para abrir issues, pull requests ou sugestões! Este projeto é uma base para sistemas seguros de envio de arquivos com Flask.

