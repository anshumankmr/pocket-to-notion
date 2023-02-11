FROM python:3.8-slim-buster

RUN apt-get update

COPY requirements.txt ./pocket-to-notion/requirements.txt
WORKDIR /pocket-to-notion
RUN pip3 install -r requirements.txt
ENV DEBUG=False
ENV PORT 8080
ENV HOST 0.0.0.0
ENV NOTION_KEY=
ENV NOTION_DATABASE_ID=
ENV CONSUMER_KEY=""
ENV ACCESS_TOKEN=""

COPY . .

CMD [ "python3" , "./src/index.py"]
