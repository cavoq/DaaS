FROM python:3.10-alpine

COPY . /DaaS
WORKDIR /DaaS

RUN apk add --no-cache build-base libffi-dev python3-dev

RUN pip install --upgrade pip \
    && pip install --upgrade setuptools \
    && pip install -r requirements.txt

ENV PORT=5000

EXPOSE $PORT

CMD ["python3.10", "server.py", "container"]