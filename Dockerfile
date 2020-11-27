FROM python:3.8-slim as builder

COPY Pipfile* /tmp/
RUN pip install pipenv && \
    cd /tmp/ && \
    pipenv lock --requirements > requirements.txt \
    cat requirements.txt

FROM python:3.8-slim
COPY --from=builder /tmp/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY . /tmp/app
RUN pip install --no-cache-dir /tmp/app/

EXPOSE 8000

CMD ["gunicorn", "--workers=4", "--threads=4", \
     "--worker-class=uvicorn.workers.UvicornH11Worker", \
     "--bind=0.0.0.0:8000", \
     "test_app.fastapi:app"]