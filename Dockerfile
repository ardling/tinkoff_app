FROM python:3.8-slim as builder

COPY . /app/
RUN pip install /app/

EXPOSE 8000

CMD ["uvicorn", "test_app.fastapi:app"]