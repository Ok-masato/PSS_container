FROM python:3.6

RUN mkdir -p /work
COPY requirements.txt /work
WORKDIR /work

EXPOSE 80

RUN pip install --upgrade pip
RUN pip install -r requirements.txt