# Sistema de recrutamento a partir de curriculos Pegho
O sistema foi desenvolvido para a empresa Pegho para que facilite o gerenciamento de curriculos de candidatos.

## Descrição do projeto
A aplicação permite a inserção, edição, exclusão e requerimento (geral ou especifico) dos curriculos, bem como as informações especificas presentes nele. Foram desenvolvidas duas versões: uma utilizando os templates com interface django, e outra utilizando DRF para 
a api.
### Tecnologias utilizadas
* No projeto, para seu desenvolvimento foram utilizados: O framework Django para o desenvolvimento do backend do projeto, HTML e CSS para os templates para acesso das informações(parte de templates), uso do DRF para o desenvolvimento a partir de apis e Docker para
a conteinerização da aplicação.
* Desafios encontrados durante o desenvolvimento da aplicação: Uso pela primeira vez do framework Django, aprender a utilizar docker de maneira correta, descobrir como relacionar os dados com o curriculo.
## Execução da aplicação:
Para executar o projeto, utilizar:
* Para a instalação dos requerimentos:
```
pip install -r requirements.txt
```
* Para a migração de dados:
```
py manage.py migrate
```
* Para a criação do admin:
```
python manage.py createsuperuser
```
* Para a execução do servidor local:
```
py manage.py runserver
```
* Para a execução a partir de docker:
```
docker compose --build
```
Para abrir a aplicação utilize [http://127.0.0.1:8000/recrutamento](http://127.0.0.1:8000/recrutamento) para aplicação com templates e [http://127.0.0.1:8000/api](http://127.0.0.1:8000/api) para a aplicação utilizando API.
Para acessar a página admin, utilize [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).
