FROM python:3.6-slim-stretch

# docker build -t connexion-example .
# docker run -d -p 8080:8080 -v "$PWD":/usr/src/app connexion-example
# ./test.sh

ENV PYTHONUNBUFFERED 1
ENV USER nobody

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY Pipfile /usr/src/app
COPY Pipfile.lock /usr/src/app

RUN pip install --no-cache-dir pipenv && \
    pipenv install --system --deploy --ignore-pipfile

COPY . .

CMD ["python3", "/usr/src/app/app.py"]
