FROM python:3.10-slim-buster

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN pip install -r requirements.txt

ENTRYPOINT streamlit run app.py