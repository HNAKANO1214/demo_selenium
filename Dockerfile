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
COPY requirements/ /app/requirements/
RUN pip install --no-cache-dir -r requirements/local.txt
COPY . /app/