FROM python:3.9

WORKDIR /code

RUN apt-get update -y \
    && apt-get upgrade -y

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv \
    && pipenv install --dev  --system --deploy --ignore-pipfile

COPY . .

CMD ["waitress-serve", "--port=8080", "--call", "app:create_app"]