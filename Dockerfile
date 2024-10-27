# Use a imagem oficial do Python como base
FROM python:3.13

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo de requisitos e instale as dependências
COPY pehgoCo/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o código da aplicação para o contêiner
COPY pehgoCo/ ./
# Exponha a porta que o Django usará
EXPOSE 8000

#RUN python manage.py collectstatic --noinput

# Comando para rodar a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
