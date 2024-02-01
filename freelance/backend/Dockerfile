FROM python:3.9.15-slim-buster

# 
WORKDIR /code
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app
#COPY ./.env .env
ENV PYTHONPATH=/app

CMD ["gunicorn", "app.main:app","--worker-class","uvicorn.workers.UvicornWorker","-b","0.0.0.0:8000"]
