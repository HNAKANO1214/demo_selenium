FROM python:3.12
WORKDIR /app
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    cmake \
    git \
    sudo \
    wget \
    vim
RUN pip install --upgrade pip
RUN pip install poetry
ENV PATH /root/.local/bin:$PATH
RUN poetry config virtualenvs.create false
COPY /pyproject.toml /app/pyproject.toml
RUN poetry install --no-root
COPY . /app/