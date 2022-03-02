FROM python:3.9-alpine

COPY . /KwcyDOSApI
WORKDIR /KwcyDOSApI

RUN pip install -r requirements.txt

ENV HOST="0.0.0.0" 
ENV PORT=5000

EXPOSE $PORT

CMD ["python3.9", "server.py"]