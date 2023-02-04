FROM python:3

RUN pip install pipenv
RUN apt-get update && apt-get install -y


WORKDIR /vincent

COPY . .

RUN pipenv install --deploy --ignore-pipfile

ENTRYPOINT ["pipenv","run","python3","bot.py"]