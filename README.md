
# Tres Everywhere 

O projeto "Trees Everywhere" tem por objetivo criar um banco de dados de árvores plantadas por voluntários espalhados pelo mundo.



## Stack utilizada

**Front-end:** Bootstrap e HTML5

**Back-end:** Django



## Rodando localmente

Clone o projeto

```bash
  git clone https://link-para-o-projeto
```

Entre no diretório do projeto

```bash
  cd trees
```

Instale as dependências

```bash
  pip install -r requirements.txt
```
Aplique as migrações

```bash
  python manage.py migrate
```

Inicie o servidor

```bash
  python manage.py runserver
```
Crie um super user

```bash
  python manage.py createsuperuser
```

## Rodando a aplicação
**Backend:** http://127.0.0.1:8000

**Admin:** http://127.0.0.1:8000/Admin

**API:** http://127.0.0.1:8000/api/planted_trees/

**Login:** http://127.0.0.1:8000/login/
## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo [LICENSE](https://choosealicense.com/licenses/mit/) para mais informações.

