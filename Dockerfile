FROM python:3.12-alpine

RUN apk add --no-cache gcc musl-dev libffi-dev

WORKDIR /app

COPY Pipfile Pipfile.lock /app/

RUN pip install --upgrade pip && \
  pip install pipenv && \
  pipenv install --system --deploy

COPY . /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]

