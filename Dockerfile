FROM python:3.5-alpine

ADD . /app
WORKDIR /app

RUN pip install -U discord.py
RUN pip install requests==2.11.1
CMD python app.py