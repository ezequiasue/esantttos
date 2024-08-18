# Use a imagem base do Python
FROM python:3.12-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install --no-install-recommends -y \
    curl \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Instalar o Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:${PATH}"

# Configurar o diretório de trabalho
WORKDIR /app

# Copiar arquivos de dependências
COPY poetry.lock pyproject.toml ./

# Instalar dependências do projeto
RUN poetry install --no-dev

# Copiar o restante do código do projeto
COPY . .

# Configurar PYTHONPATH
ENV PYTHONPATH="/app/.venv/lib/python3.12/site-packages"

# Comando padrão para iniciar o Django
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
