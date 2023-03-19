FROM python:3.10-alpine

COPY . /denialofserviceAPI
WORKDIR /denialofserviceAPI

RUN pip install -r requirements.txt

ENV HOST="0.0.0.0"
ENV PORT=5000

EXPOSE $PORT

CMD ["python3.10", "server.py", "container"]