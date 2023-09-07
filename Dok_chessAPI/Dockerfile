
FROM python:latest

LABEL Maintainer = "KANI_A"
WORKDIR /app
COPY . /app

RUN pip install -r ./app/resources/requirements.txt


EXPOSE 8000

ENV FLASK_APP=./app/src/chess_moves.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
