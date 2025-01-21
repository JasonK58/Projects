FROM python:3.13-slim

RUN apt-get update

WORKDIR /code

COPY backend/requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

COPY backend/src /code

CMD ["fastapi", "run", "main.py"]