FROM python:3.9
WORKDIR /code

ENV FLASK_RUN_HOST=0.0.0.0

RUN apt-get update -y \
    && apt-get upgrade -y

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv \
    && pipenv install --dev  --system --deploy --ignore-pipfile

EXPOSE 5000
COPY . .
CMD ["flask","--app", "main", "run"]