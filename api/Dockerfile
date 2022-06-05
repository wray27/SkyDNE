FROM python:3.9.5-slim-buster

COPY . .

RUN pip install -r requirements.txt

WORKDIR /netconf_api

ENTRYPOINT [ "python", "/netconf_api/index.py" ]