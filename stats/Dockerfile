FROM python:3.10

WORKDIR /app

COPY req.txt ./req.txt

RUN pip install --no-cache-dir --upgrade -r /app/req.txt

COPY . /app

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]