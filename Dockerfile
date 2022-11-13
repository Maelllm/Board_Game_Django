FROM python:3.10

RUN apt update
RUN mkdir /board_game_django

WORKDIR /board_game_django


COPY ./src ./
COPY requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r ./requirements.txt

CMD ["python", "manage.py", "runserver", "0:8008"]




