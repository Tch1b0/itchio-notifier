FROM python:latest

WORKDIR /app

COPY ./token ./token
COPY ./src ./src

RUN pip install python-telegram-bot
RUN pip install itchio

CMD ["python", "./src"]