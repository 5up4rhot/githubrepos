# syntax=docker/dockerfile:1
FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /gitrepos
COPY requirements.txt /gitrepos/
RUN pip install -r requirements.txt
COPY gitrepos /gitrepos/