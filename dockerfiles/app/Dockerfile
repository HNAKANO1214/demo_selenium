FROM python:3.12
WORKDIR /app
RUN pip install --upgrade pip
COPY /requirements/ /app/requirements/
RUN pip install --no-cache-dir -r requirements/local.txt
COPY . /app/