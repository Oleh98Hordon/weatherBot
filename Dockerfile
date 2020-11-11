FROM frolvlad/alpine-python3
LABEL maintainer "oleg98gordon@gmail.com"

RUN pip install --upgrade pip

RUN pip3 install --no-cache-dir telebot

COPY weatherbot /weatherbot

RUN pip3 install --no-cache-dir pytelegrambotapi --upgrade

ENTRYPOINT python3 /weatherbot/weatherBot.py
