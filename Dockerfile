FROM python:3.8-slim as builder

COPY . /app/
RUN pip install --no-cache-dir /app/

EXPOSE 8000

CMD ["gunicorn", "--workers=4", "--threads=4", \
     "--worker-class=uvicorn.workers.UvicornH11Worker", \
     "--bind=0.0.0.0:8000", \
     "test_app.fastapi:app"]