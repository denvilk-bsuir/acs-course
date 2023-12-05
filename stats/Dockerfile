FROM python:3.10

WORKDIR /app

COPY ./req.txt ./req.txt
COPY ./entrypoint.sh /app/entrypoint.sh

RUN pip install --no-cache-dir --upgrade -r /app/req.txt

COPY . /app

RUN sed -i "s/\r$//g"  /app/entrypoint.sh
RUN chmod ug+x  /app/*
EXPOSE 8000

ENTRYPOINT [ "/app/entrypoint.sh" ]