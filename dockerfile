FROM python:latest

WORKDIR /app

COPY ./token ./token
COPY ./src ./src

RUN pip install python-telegram-bot
RUN pip install git+https://github.com/Tch1b0/itchio-lib.git#egg=itchio

CMD ["python", "./src"]