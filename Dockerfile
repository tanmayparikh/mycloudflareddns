FROM python:3.10-slim

ENV PYTHONBUFFERED=1

WORKDIR /src
COPY app.py app.py
COPY requirements.txt requirements.txt

RUN apt update
RUN pip install -r requirements.txt

CMD ["python", "/src/app.py"]