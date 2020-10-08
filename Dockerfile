# syntax = docker/dockerfile:experimental
FROM python:3.6.1-alpine
WORKDIR /project
ADD . /project
RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt
CMD ["python","run.py"]