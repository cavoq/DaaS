FROM python:3.10-alpine

COPY . /DaaS
WORKDIR /DaaS

RUN pip install -r requirements.txt

ENV PORT=5000

EXPOSE $PORT

CMD ["python3.10", "server.py", "container"]