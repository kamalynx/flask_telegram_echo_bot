FROM python:3.9-slim-bullseye
WORKDIR /app
COPY ./ ./
RUN pip install pipenv && pipenv --three sync
CMD ["pipenv", "run", "python", "app.py"]
